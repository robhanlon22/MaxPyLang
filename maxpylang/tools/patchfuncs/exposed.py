"""User-facing helpers exposed through `MaxPatch`."""

from __future__ import annotations

import logging
from typing import TYPE_CHECKING, Any, cast

if TYPE_CHECKING:
    from maxpylang.maxobject import MaxObject
    from maxpylang.maxpatch import MaxPatch

_LOGGER = logging.getLogger(__name__)


def reorder(self: MaxPatch, *, verbose: bool = False) -> None:
    """Renumber patch objects sequentially."""
    del verbose
    _LOGGER.debug("reordering %s objects...", self.num_objs)

    self._num_objs = 0
    new_objs_dict: dict[str, MaxObject] = {}
    for obj in self._objs.values():
        self._num_objs += 1
        obj.set_box_id(f"obj-{self._num_objs}")
        new_objs_dict[obj.box_id] = obj
    self._objs = new_objs_dict

    _LOGGER.debug("%s objects reordered", self.num_objs)


def set_position(
    self: MaxPatch,
    new_x: float,
    new_y: float,
    *,
    from_place: bool = False,
    verbose: bool = False,
) -> None:
    """Set the patch placement cursor."""
    del verbose
    if isinstance(new_x, (float, int)) and isinstance(new_y, (float, int)):
        self._curr_position = [new_x, new_y]
        if from_place:
            _LOGGER.debug("starting position set to %s", self._curr_position)
        else:
            _LOGGER.debug("position set to %s", self._curr_position)
        return

    if from_place:
        _LOGGER.error(
            "Error: starting position must be specified as int or float, "
            "starting position not set"
        )
        return

    _LOGGER.error("Error: position must be specified as int or float, position not set")


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
        _LOGGER.warning("%s does not exist, nothing changed", curr_obj_num)
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

    _LOGGER.debug("%s replaced, new %s : %s", old_name, curr_obj_num, replacement.name)


def inspect(self: MaxPatch, *objs: str, info: str = "all") -> None:
    """Inspect the patch or selected objects."""
    del self, objs, info
