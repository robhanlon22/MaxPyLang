"""Helpers for serializing `MaxPatch` instances."""

from __future__ import annotations

import copy
import json
import sys
from pathlib import Path
from typing import TYPE_CHECKING, cast

if TYPE_CHECKING:
    from maxpylang.maxpatch import MaxPatch

JSONDict = dict[str, object]


def _write_stdout(*parts: object) -> None:
    """Write a space-joined line to stdout."""
    sys.stdout.write(" ".join(str(part) for part in parts) + "\n")


def save(
    self: MaxPatch,
    filename: str = "default.maxpat",
    *,
    verbose: bool = True,
    check: bool = True,
) -> None:
    """Save the patch to a `.maxpat` file."""
    output_path = Path(filename)
    if ".maxpat" not in output_path.suffixes:
        output_path = output_path.with_suffix(".maxpat")

    json_dict = self.get_json()
    with output_path.open("w", encoding="utf-8") as handle:
        json.dump(json_dict, handle, indent=2)

    self._filename = str(output_path)
    if check:
        self.check("unknown", "js", "abstractions")
    if verbose:
        _write_stdout("maxpatch saved to", output_path)


def get_json(self: MaxPatch) -> JSONDict:
    """Return the patch dictionary with boxes and lines populated."""
    json_dict = cast("JSONDict", copy.deepcopy(self._patcher_dict))
    patcher = cast("dict[str, object]", json_dict["patcher"])
    boxes = cast("list[object]", patcher["boxes"])
    lines = cast("list[object]", patcher["lines"])

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
