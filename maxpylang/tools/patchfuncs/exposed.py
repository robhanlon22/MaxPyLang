"""User-facing helpers exposed through `MaxPatch`."""

from __future__ import annotations

import sys
from typing import TYPE_CHECKING, Any, cast

if TYPE_CHECKING:
    from maxpylang.maxobject import MaxObject
    from maxpylang.maxpatch import MaxPatch


def _write_stdout(*parts: object) -> None:
    """Write a space-joined line to stdout."""
    sys.stdout.write(" ".join(str(part) for part in parts) + "\n")


def reorder(self: MaxPatch, *, verbose: bool = False) -> None:
    """Renumber patch objects sequentially."""
    if verbose:
        _write_stdout("reordering", self.num_objs, "objects...")

    self._num_objs = 0
    new_objs_dict: dict[str, MaxObject] = {}
    for obj in self._objs.values():
        self._num_objs += 1
        obj.set_box_id(f"obj-{self._num_objs}")
        new_objs_dict[obj.box_id] = obj
    self._objs = new_objs_dict

    if verbose:
        _write_stdout(self.num_objs, "objects reordered")


def set_position(
    self: MaxPatch,
    new_x: float,
    new_y: float,
    *,
    from_place: bool = False,
    verbose: bool = False,
) -> None:
    """Set the patch placement cursor."""
    if isinstance(new_x, (float, int)) and isinstance(new_y, (float, int)):
        self._curr_position = [new_x, new_y]
        if verbose:
            if from_place:
                _write_stdout("starting position set to", self._curr_position)
            else:
                _write_stdout("position set to", self._curr_position)
        return

    if from_place:
        _write_stdout(
            "Error: starting position must be specified as int or float, "
            "starting position not set"
        )
        return

    _write_stdout("Error: position must be specified as int or float, position not set")


def replace(
    self: MaxPatch,
    curr_obj_num: str,
    new_obj: object,
    *,
    retain: bool = True,
    verbose: bool = False,
    **new_attribs: object,
) -> None:
    """Replace one object with another and preserve compatible state."""
    if curr_obj_num not in self._objs:
        _write_stdout(curr_obj_num, "does not exist, nothing changed")
        return

    old_obj = self._objs[curr_obj_num]
    old_box = cast("dict[str, Any]", old_obj.raw_dict["box"])
    position = cast("list[float]", old_box["patching_rect"][:2])
    old_name = old_obj.name

    replacement = self.get_obj_from_spec(
        cast("str | MaxObject | list[Any]", new_obj),
    )
    if retain:
        replacement.retain_attribs(old_obj)

    replacement.edit(**cast("dict[str, Any]", new_attribs))
    self.swap_patchcords(replacement, old_obj)
    self.delete_objs(curr_obj_num, verbose=verbose)
    self.place_obj(
        replacement,
        position=position,
        verbose=verbose,
        replace_id=curr_obj_num,
    )

    if verbose:
        _write_stdout(old_name, "replaced, new", curr_obj_num, ":", replacement.name)


def inspect(self: MaxPatch, *objs: str, info: str = "all") -> None:
    """Inspect the patch or selected objects."""
    del self, objs, info
