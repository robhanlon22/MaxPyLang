"""Helpers for building and updating Max object xlets."""

from __future__ import annotations

import operator
from typing import TYPE_CHECKING, cast

from maxpylang.tools import typechecks as tc
from maxpylang.tools.misc import write_stdout
from maxpylang.xlet import Inlet, Outlet

if TYPE_CHECKING:
    from maxpylang.maxobject import MaxObject

ObjectInfo = dict[str, object]
Comparator = dict[str, object]
_COMPARATORS = {
    "<": operator.lt,
    "<=": operator.le,
    "==": operator.eq,
    "!=": operator.ne,
    ">=": operator.ge,
    ">": operator.gt,
}


def _parse_comparator(base_num: int, comparator: str) -> bool:
    """Evaluate a simple comparison string against `base_num`."""
    for symbol, func in _COMPARATORS.items():
        if not comparator.startswith(symbol):
            continue
        target = int(float(comparator[len(symbol) :].strip()))
        return bool(func(base_num, target))
    message = f"unsupported comparator: {comparator}"
    raise ValueError(message)


def make_xlets_from_self_dict(self: MaxObject) -> None:
    """Build inlet and outlet objects from the backing dictionary."""
    box = cast("dict[str, object]", self._dict["box"])
    num_inlets = cast("int", box["numinlets"])
    num_outlets = cast("int", box["numoutlets"])

    self._ins = [Inlet(self, index) for index in range(num_inlets)]
    out_types = cast("list[object]", box.get("outlettype", [None] * num_outlets))
    normalized_types = [
        "any" if out_type == "" else out_type for out_type in list(out_types)
    ]
    self._outs = [
        Outlet(self, index, types=out_type)
        for index, out_type in zip(range(num_outlets), normalized_types)
    ]


def update_ins_outs(
    self: MaxObject,
    inout_info: dict[str, object],
    default_info: dict[str, object],
) -> None:
    """Update inlet and outlet counts from object metadata."""
    del default_info
    if not self._args or not inout_info:
        return

    for xlet_type in ("numinlets", "numoutlets"):
        if xlet_type not in inout_info:
            continue
        current_xlets = self._ins if xlet_type == "numinlets" else self._outs
        curr_count = len(current_xlets)
        new_count = self.parse_io_num(
            cast("list[dict[str, object]]", inout_info[xlet_type]),
            curr_count,
        )
        diff = new_count - curr_count
        if diff > 0:
            self.add_xlets(diff, xlet_type)
        elif diff < 0:
            self.remove_xlets(abs(diff), xlet_type)
        if diff != 0:
            self.update_xlet_typing(inout_info, xlet_type, new_count)

    self.update_dict_io_nums()
    if self._name == "vst~":
        self.update_vst()


def parse_io_num(self: MaxObject, info: list[ObjectInfo], default_num: int) -> int:
    """Parse xlet-count metadata into a final inlet or outlet count."""
    total = 0
    for term in info:
        argtype = term["argtype"]
        if argtype == "n":
            args = [int(float(arg)) for arg in self._args if tc.check_number(arg)]
        else:
            args = list(self._args)

        index = term["index"]
        if index == "all":
            base_num = len(args)
        else:
            index_value = cast("int", index)
            if len(args) <= index_value:
                return default_num
            base_num = int(args[index_value])

        if "acc_vals" in term:
            accepted_values = cast("list[int]", term["acc_vals"])
            if base_num not in accepted_values:
                base_num = min(accepted_values, key=lambda value: abs(value - base_num))

        if "comparitor" in term and not _parse_comparator(
            base_num,
            cast("str", term["comparitor"]),
        ):
            return default_num

        total += base_num
        if "add_amt" in term:
            total += cast("int", term["add_amt"])

    return total


def add_xlets(self: MaxObject, num: int, xlet_type: str) -> None:
    """Add inlet or outlet objects."""
    if xlet_type == "numinlets":
        self._ins.extend(Inlet(self, len(self._ins) + index) for index in range(num))
        return
    self._outs.extend(Outlet(self, len(self._outs) + index) for index in range(num))


def remove_xlets(self: MaxObject, num: int, xlet_type: str) -> None:
    """Remove inlet or outlet objects and detach their patchcords."""
    if xlet_type == "numinlets":
        removed_inlets = self._ins[-num:]
        del self._ins[-num:]
        for inlet in removed_inlets:
            for outlet in list(inlet.sources):
                source_index = inlet.sources.index(outlet)
                if source_index < len(inlet.midpoints):
                    del inlet.midpoints[source_index]
                inlet.sources.remove(outlet)
                if inlet in outlet.destinations:
                    outlet.destinations.remove(inlet)
                write_stdout("Patchcord removed")
        return

    removed_outlets = self._outs[-num:]
    del self._outs[-num:]
    for outlet in removed_outlets:
        for inlet in list(outlet.destinations):
            source_index = inlet.sources.index(outlet)
            if source_index < len(inlet.midpoints):
                del inlet.midpoints[source_index]
            inlet.sources.remove(outlet)
            if inlet in outlet.destinations:
                outlet.destinations.remove(inlet)
            write_stdout("Patchcord removed")


def update_dict_io_nums(self: MaxObject) -> None:
    """Sync inlet and outlet counts into the backing dictionary."""
    self._dict["box"]["numinlets"] = len(self._ins)
    self._dict["box"]["numoutlets"] = len(self._outs)


def update_xlet_typing(
    self: MaxObject,
    info: dict[str, object],
    xlet_type: str,
    num_xlets: int,
) -> None:
    """Update inlet and outlet type metadata."""
    type_info = cast("list[dict[str, object]]", info[xlet_type])[0]["type"]
    new_types = self.parse_io_typing(type_info, num_xlets)

    if xlet_type == "numoutlets":
        self._dict["box"]["outlettype"] = new_types.copy()

    normalized_types = [
        "any" if type_name == "" else type_name for type_name in new_types
    ]
    for index in range(num_xlets):
        if xlet_type == "numinlets":
            self._ins[index].__dict__["_types"] = normalized_types[index]
        else:
            self._outs[index].__dict__["_types"] = normalized_types[index]


def parse_io_typing(self: MaxObject, type_info: object, num_xlets: int) -> list[object]:
    """Parse xlet typing metadata into a per-xlet type list."""
    if isinstance(type_info, str) or type_info is None:
        if type_info == "trigger_out":
            return self.get_trigger_out_types()
        if type_info == "unpack_out":
            return self.get_unpack_out_types()
        return [type_info] * num_xlets

    info_dict = cast("dict[str, object]", type_info)
    new_types: list[object] = [info_dict["default"]] * num_xlets

    if "first" in info_dict:
        num_firsts, first_types = cast("tuple[int, object]", info_dict["first"])
        first_type_list = (
            [first_types] * num_firsts
            if isinstance(first_types, str)
            else cast("list[object]", first_types)
        )
        for index in range(num_firsts):
            new_types[index] = first_type_list[index]

    if "last" in info_dict:
        num_lasts, last_types = cast("tuple[int, object]", info_dict["last"])
        last_type_list = (
            [last_types] * num_lasts
            if isinstance(last_types, str)
            else cast("list[object]", last_types)
        )
        for index in range(num_lasts):
            new_types[-(index + 1)] = last_type_list[-(index + 1)]

    return new_types
