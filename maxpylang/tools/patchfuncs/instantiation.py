"""Helpers for constructing `MaxPatch` instances."""

from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import TYPE_CHECKING, Any, cast

from maxpylang.maxobject import MaxObject

if TYPE_CHECKING:
    from maxpylang.maxpatch import MaxPatch

JSONDict = dict[str, Any]


def _write_stdout(*parts: object) -> None:
    """Write a space-joined line to stdout."""
    sys.stdout.write(" ".join(str(part) for part in parts) + "\n")


def _read_json_dict(path: Path) -> JSONDict:
    """Read a JSON dictionary from disk."""
    return cast("JSONDict", json.loads(path.read_text(encoding="utf-8")))


def load_template(
    self: MaxPatch,
    template: str,
    *,
    verbose: bool = True,
) -> None:
    """Load a patch template into the patch instance."""
    template_path = Path(template)
    if not template_path.exists():
        template_path = Path(self.patch_templates_path) / template
        if not template_path.exists():
            message = "Error: template file not found"
            raise AssertionError(message)

    self._patcher_dict = _read_json_dict(template_path)
    if verbose:
        _write_stdout(
            "Patcher: new patch created from template file:",
            template_path.name,
        )


def load_file(
    self: MaxPatch,
    filename: str,
    *,
    reorder: bool = True,
    verbose: bool = True,
) -> None:
    """Load an existing `.maxpat` file into the patch instance."""
    input_path = Path(filename)
    if verbose:
        _write_stdout("Patcher: loading patch from existing file:", input_path.name)

    patch_dict = _read_json_dict(input_path)
    self.load_objs_from_dict(patch_dict, verbose=verbose)
    self.load_patchcords_from_dict(patch_dict, verbose=verbose)
    self._patcher_dict = self.clean_patcher_dict(patch_dict)

    if reorder:
        self.reorder()
    if verbose:
        _write_stdout("Patcher: patch loaded from existing file:", input_path.name)


def load_objs_from_dict(
    self: MaxPatch,
    patch_dict: JSONDict,
    *,
    verbose: bool = True,
) -> None:
    """Load box objects from a serialized patch dictionary."""
    self._num_objs = 0
    patcher = cast("dict[str, Any]", patch_dict["patcher"])
    for box in cast("list[Any]", patcher["boxes"]):
        obj = MaxObject(box, from_dict=True)
        self._num_objs += 1
        self._objs[obj.box_id] = obj
        if verbose:
            _write_stdout("Patcher:", obj.name, "added, total objects", self._num_objs)


def load_patchcords_from_dict(
    self: MaxPatch,
    patch_dict: JSONDict,
    *,
    verbose: bool = True,
) -> None:
    """Load patchcords from a serialized patch dictionary."""
    patcher = cast("dict[str, Any]", patch_dict["patcher"])
    for line in cast("list[Any]", patcher["lines"]):
        line_dict = cast("dict[str, Any]", line)
        patchline = cast("dict[str, Any]", line_dict["patchline"])
        source = cast("list[Any]", patchline["source"])
        destination = cast("list[Any]", patchline["destination"])
        source_obj = self._objs[cast("str", source[0])]
        destination_obj = self._objs[cast("str", destination[0])]
        connection = [
            source_obj.outs[cast("int", source[1])],
            destination_obj.ins[cast("int", destination[1])],
        ]
        connection.append(
            cast("list[float | None]", patchline.get("midpoints", [None])),
        )
        self.connect(connection, verbose=verbose)


def clean_patcher_dict(self: MaxPatch, patch_dict: JSONDict) -> JSONDict:
    """Strip box and patchcord data from a patch dictionary."""
    del self
    patcher = cast("dict[str, Any]", patch_dict["patcher"])
    patcher["boxes"] = []
    patcher["lines"] = []
    return patch_dict
