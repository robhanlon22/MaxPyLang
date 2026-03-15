"""Helpers for serializing `MaxPatch` instances."""

from __future__ import annotations

import copy
import json
import logging
from pathlib import Path
from typing import TYPE_CHECKING, Any, cast

if TYPE_CHECKING:
    from maxpylang.maxpatch import MaxPatch

JSONDict = dict[str, Any]
_LOGGER = logging.getLogger(__name__)


def save(
    self: MaxPatch,
    filename: str = "default.maxpat",
    *,
    verbose: bool = True,
    check: bool = True,
) -> None:
    """Save the patch to a `.maxpat` file."""
    del verbose
    output_path = Path(filename)
    if ".maxpat" not in output_path.suffixes:
        output_path = output_path.with_suffix(".maxpat")

    json_dict = self.get_json()
    with output_path.open("w", encoding="utf-8") as handle:
        json.dump(json_dict, handle, indent=2)

    self._filename = str(output_path)
    if check:
        self.check("unknown", "js", "abstractions")
    _LOGGER.debug("maxpatch saved to %s", output_path)


def get_json(self: MaxPatch) -> JSONDict:
    """Return the patch dictionary with boxes and lines populated."""
    json_dict = copy.deepcopy(self._patcher_dict)
    patcher = cast("dict[str, Any]", json_dict["patcher"])
    boxes = cast("list[Any]", patcher["boxes"])
    lines = cast("list[Any]", patcher["lines"])

    for source_id, obj in self._objs.items():
        boxes.append(obj.raw_dict)
        for outlet in obj.outs:
            for destination in outlet.destinations:
                patchcord_dict: JSONDict = {
                    "patchline": {
                        "destination": [destination.parent.box_id, destination.index],
                        "source": [source_id, outlet.index],
                        "midpoints": destination.midpoints[
                            destination.sources.index(outlet)
                        ],
                    }
                }
                lines.append(patchcord_dict)

    return json_dict
