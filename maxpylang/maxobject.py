"""Expose the `MaxObject` facade."""

from __future__ import annotations

import sys
from typing import TYPE_CHECKING, Any, Union

from .tools import constants as _constants
from .tools import misc
from .tools.objfuncs import args as _args
from .tools.objfuncs import attribs as _attribs
from .tools.objfuncs import exposed as _exposed
from .tools.objfuncs import instantiation as _instantiation
from .tools.objfuncs import makexlets as _makexlets
from .tools.objfuncs import misc as _obj_misc
from .tools.objfuncs import reffile as _reffile
from .tools.objfuncs import specialobjs as _specialobjs
from .tools.objfuncs import text as _text

if TYPE_CHECKING:
    from collections.abc import Mapping, Sequence

    from .xlet import Inlet, Outlet

Atom = Union[str, int, float]
ObjectValue = Any
ObjectDict = dict[str, Any]
ObjectArgs = list[Atom]
ObjectInfoList = list[dict[str, Any]]


def _write_stdout(*parts: object) -> None:
    """Write a single line to stdout."""
    sys.stdout.write(" ".join(str(part) for part in parts) + "\n")


class MaxObject:
    """Represent a Max object within a patch."""

    arg_warning = True
    known_objs = misc.get_objs()
    common_box_attribs = _constants.common_box_attribs
    obj_info_folder = _constants.obj_info_folder
    unknown_obj_dict = _constants.unknown_obj_dict

    def __init__(
        self,
        text: object,
        *,
        from_dict: bool = False,
        abstraction: bool = False,
        inlets: int | None = None,
        outlets: int | None = None,
        **extra_attribs: object,
    ) -> None:
        """Initialize an object from text or a saved box dictionary."""
        self._ref_file: str | None = None
        self._dict: ObjectDict = {}
        self._name = ""
        self._args: ObjectArgs = []
        self._text_attribs: ObjectDict = {}
        self._ins: list[Inlet] = []
        self._outs: list[Outlet] = []
        self._ext_file: str | None = None

        if from_dict:
            self.build_from_dict(text)
        else:
            self.build_from_specs(
                str(text),
                dict(extra_attribs),
                abstraction=abstraction,
                inlets=inlets,
                outlets=outlets,
            )

    @property
    def name(self) -> str:
        """Return the Max class name."""
        return self._name

    @property
    def ins(self) -> list[Inlet]:
        """Return the inlet list."""
        return self._ins

    @property
    def outs(self) -> list[Outlet]:
        """Return the outlet list."""
        return self._outs

    @property
    def ref_file(self) -> str | None:
        """Return the resolved reference file marker."""
        return self._ref_file

    @property
    def ext_file(self) -> str | None:
        """Return the linked external file, if any."""
        return self._ext_file

    @property
    def raw_dict(self) -> ObjectDict:
        """Return the backing box dictionary."""
        return self._dict

    @property
    def box_id(self) -> str:
        """Return the current box identifier."""
        return str(self._dict["box"]["id"])

    def set_box_id(self, box_id: str) -> None:
        """Update the box identifier stored in the backing dictionary."""
        self._dict["box"]["id"] = box_id

    def move(self, x: float, y: float) -> None:
        """Move the object to a new patcher position."""
        _exposed.move(self, x, y)

    def edit(
        self,
        text_add: str = "append",
        text: str | None = None,
        **extra_attribs: object,
    ) -> None:
        """Edit the object text and extra attributes."""
        _exposed.edit(self, text_add=text_add, text=text, **extra_attribs)

    def link(self, link_file: str | None = None) -> None:
        """Link a js file or abstraction file to the object."""
        _exposed.link(self, link_file=link_file)

    def inspect(self) -> None:
        """Inspect the object."""
        _exposed.inspect(self)

    def build_from_specs(
        self,
        text: str,
        extra_attribs: ObjectDict,
        *,
        abstraction: bool = False,
        inlets: int | None = None,
        outlets: int | None = None,
    ) -> None:
        """Build the object from in-box text."""
        _instantiation.build_from_specs(
            self,
            text,
            extra_attribs,
            abstraction=abstraction,
            io_counts=(inlets, outlets),
        )

    def build_from_dict(self, given_dict: object) -> None:
        """Build the object from a serialized box dictionary."""
        _instantiation.build_from_dict(self, given_dict)

    def parse_text(self, text: str) -> tuple[str, ObjectArgs, ObjectDict]:
        """Parse object text into name, args, and attributes."""
        return _text.parse_text(self, text)

    def update_text(self) -> None:
        """Refresh the stored box text from object state."""
        _text.update_text(self)

    def get_text(self) -> str:
        """Return the current in-box text."""
        return _text.get_text(self)

    def get_ref(self, name: str) -> str:
        """Resolve the reference file for an object name."""
        return _reffile.get_ref(self, name)

    def check_aliases(self, name: str) -> str:
        """Resolve supported aliases for an object name."""
        return _reffile.check_aliases(self, name)

    def get_info(self, ref_file: str | None = None) -> ObjectDict:
        """Return parsed reference metadata for the object."""
        return _reffile.get_info(self, ref_file=ref_file)

    def make_xlets_from_self_dict(self) -> None:
        """Build inlet and outlet objects from the backing dictionary."""
        _makexlets.make_xlets_from_self_dict(self)

    def update_ins_outs(
        self,
        inout_info: dict[str, Any],
        default_info: dict[str, Any],
    ) -> None:
        """Update inlet and outlet counts from parsed metadata."""
        _makexlets.update_ins_outs(self, inout_info, default_info)

    def parse_io_num(self, info: ObjectInfoList, default_num: int) -> int:
        """Parse metadata into an inlet or outlet count."""
        return _makexlets.parse_io_num(self, info, default_num)

    def add_xlets(self, num: int, xlet_type: str) -> None:
        """Add inlet or outlet objects."""
        _makexlets.add_xlets(self, num, xlet_type)

    def remove_xlets(self, num: int, xlet_type: str) -> None:
        """Remove inlet or outlet objects."""
        _makexlets.remove_xlets(self, num, xlet_type)

    def update_dict_io_nums(self) -> None:
        """Sync inlet and outlet counts back into the box dict."""
        _makexlets.update_dict_io_nums(self)

    def update_xlet_typing(
        self,
        info: dict[str, Any],
        xlet_type: str,
        num_xlets: int,
    ) -> None:
        """Update inlet or outlet typing information."""
        _makexlets.update_xlet_typing(self, info, xlet_type, num_xlets)

    def parse_io_typing(self, type_info: object, num_xlets: int) -> list[object]:
        """Parse metadata into per-xlet types."""
        return _makexlets.parse_io_typing(self, type_info, num_xlets)

    def args_valid(
        self,
        name: str,
        args: ObjectArgs,
        arg_info: dict[str, Any],
    ) -> bool:
        """Validate object args against reference metadata."""
        return _args.args_valid(self, name, args, arg_info)

    def get_typed_args(self, args: list[str]) -> ObjectArgs:
        """Cast parsed string args into typed Python values."""
        return _args.get_typed_args(self, args)

    def add_extra_attribs(self, extra_attribs: ObjectDict) -> None:
        """Apply extra attributes to the backing dictionary."""
        _attribs.add_extra_attribs(self, extra_attribs)

    def get_all_valid_attribs(
        self,
        text_attribs: ObjectDict,
        extra_attribs: ObjectDict,
        attrib_info: Sequence[Mapping[str, Any]],
    ) -> tuple[ObjectDict, ObjectDict]:
        """Split valid text attributes from extra attributes."""
        return _attribs.get_all_valid_attribs(
            self,
            text_attribs,
            extra_attribs,
            attrib_info,
        )

    def remove_bad_attribs(
        self,
        attribs: ObjectDict,
        attrib_speclist: Sequence[Mapping[str, Any]],
    ) -> ObjectDict:
        """Drop attributes not supported by the object metadata."""
        return _attribs.remove_bad_attribs(self, attribs, attrib_speclist)

    def retain_attribs(self, other: MaxObject) -> None:
        """Copy compatible attributes from another object."""
        _attribs.retain_attribs(self, other)

    def get_extra_attribs(self) -> ObjectDict:
        """Return extra attributes stored on the object."""
        return _attribs.get_extra_attribs(self)

    def create_js(self, *, from_dict: bool | None = None) -> None:
        """Initialize js metadata from args or a saved dict."""
        _specialobjs.create_js(self, from_dict=from_dict)

    def get_js_filename(self) -> str | None:
        """Return the referenced js filename from the current args."""
        return _specialobjs.get_js_filename(self)

    def get_js_io(
        self,
        filename: str,
        log_var: str | None = None,
    ) -> tuple[str | int, str | int]:
        """Read inlet and outlet counts from a js file."""
        return _specialobjs.get_js_io(self, filename, log_var=log_var)

    def update_js_from_file(
        self,
        filename: str,
        log_var: str | None = None,
    ) -> None:
        """Refresh js metadata from a linked file."""
        _specialobjs.update_js_from_file(self, filename, log_var=log_var)

    def link_js(self, link_file: str | None = None) -> None:
        """Link the object to a js file."""
        _specialobjs.link_js(self, link_file=link_file)

    def create_abstraction(
        self,
        text: str | None = None,
        extra_attribs: ObjectDict | None = None,
        *,
        from_dict: bool = True,
    ) -> None:
        """Initialize abstraction metadata."""
        _specialobjs.create_abstraction(
            self,
            text=text,
            extra_attribs=extra_attribs,
            from_dict=from_dict,
        )

    def get_abstraction_io(self) -> tuple[int, int]:
        """Count inlet and outlet objects in the linked abstraction file."""
        return _specialobjs.get_abstraction_io(self)

    def update_abstraction_from_file(
        self,
        text: str,
        extra_attribs: ObjectDict | None,
        log_var: str | None = None,
    ) -> None:
        """Refresh abstraction metadata from the linked file."""
        _specialobjs.update_abstraction_from_file(
            self,
            text,
            extra_attribs,
            log_var=log_var,
        )

    def link_abstraction(self, link_file: str | None = None) -> None:
        """Link the object to an abstraction file."""
        _specialobjs.link_abstraction(self, link_file=link_file)

    def create_declared_abstraction(
        self,
        text: str,
        numinlets: int,
        numoutlets: int,
        extra_attribs: ObjectDict,
    ) -> None:
        """Create an abstraction with explicit inlet and outlet counts."""
        _specialobjs.create_declared_abstraction(
            self,
            text,
            numinlets,
            numoutlets,
            extra_attribs,
        )

    def get_trigger_out_types(self) -> list[str]:
        """Return trigger outlet types inferred from current args."""
        return _specialobjs.get_trigger_out_types(self)

    def get_unpack_out_types(self) -> list[str]:
        """Return unpack outlet types inferred from current args."""
        return _specialobjs.get_unpack_out_types(self)

    def update_vst(self) -> None:
        """Refresh the stored `vst~` save payload."""
        _specialobjs.update_vst(self)

    def notknown(self) -> bool:
        """Return whether the object is unresolved."""
        return _obj_misc.notknown(self)

    def __repr__(self) -> str:
        """Return a developer-facing object summary."""
        return _obj_misc.repr_object(self)

    def debug(self) -> None:
        """Write the internal object state to stdout."""
        _write_stdout("ref_file", self._ref_file)
        _write_stdout("dict", self._dict)
        _write_stdout("name", self._name)
        _write_stdout("args", self._args)
        _write_stdout("text_attribs", self._text_attribs)
        _write_stdout("ins", self._ins)
        _write_stdout("outs", self._outs)
        _write_stdout("ext_file", self._ext_file)
