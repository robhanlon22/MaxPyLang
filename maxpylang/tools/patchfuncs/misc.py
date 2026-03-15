"""Miscellaneous MaxPatch helper functions."""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from maxpylang.maxpatch import MaxPatch


def add_barebones_obj(self: MaxPatch, obj_text: str) -> None:
    """Place a barebones object entry into the patcher dictionary."""
    barebones_obj = {
        "box": {"maxclass": "newobj", "text": obj_text, "patching_rect": [100.0, 100.0]}
    }

    self._patcher_dict["patcher"]["boxes"].append(barebones_obj)
