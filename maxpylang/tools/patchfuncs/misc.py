"""
tools.patchfuncs.misc

Miscellaneous MaxPatch functions.
"""

from typing import Any


def add_barebones_obj(self: Any, obj_text: str) -> None:
    """
    For importing objs.
    Place a barebones obj in the patch.
    """
    barebones_obj = {
        "box": {"maxclass": "newobj", "text": obj_text, "patching_rect": [100.0, 100.0]}
    }

    self._patcher_dict["patcher"]["boxes"].append(barebones_obj)
