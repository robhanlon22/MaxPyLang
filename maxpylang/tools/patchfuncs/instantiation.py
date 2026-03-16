"""Helpers for constructing and loading ``MaxPatch`` instances."""

from __future__ import annotations

import json
import logging
from pathlib import Path
from typing import TYPE_CHECKING, Any, cast

from maxpylang.maxobject import MaxObject

if TYPE_CHECKING:
    from maxpylang.maxpatch import MaxPatch

JSONDict = dict[str, Any]
_LOGGER = logging.getLogger(__name__)


def _read_json_dict(path: Path) -> JSONDict:
    """Read a JSON dictionary from disk."""
    return cast("JSONDict", json.loads(path.read_text(encoding="utf-8")))


def load_template(
    self: MaxPatch,
    template: str,
    *,
    verbose: bool = True,
) -> None:
    """Load a patch template into the patch instance.

    Args:
        self: Patch being initialized.
        template: Template filename or path.
        verbose: Legacy compatibility flag retained for the public API.

    Raises:
        AssertionError: If the requested template does not exist.
    """
    del verbose
    template_path = Path(template)
    if not template_path.exists():
        template_path = Path(self.patch_templates_path) / template
        if not template_path.exists():
            message = "Error: template file not found"
            raise AssertionError(message)

    self._patcher_dict = _read_json_dict(template_path)
    _LOGGER.debug(
        "Patcher: new patch created from template file: %s",
        template_path.name,
    )


def load_file(
    self: MaxPatch,
    filename: str,
    *,
    reorder: bool = True,
    verbose: bool = True,
) -> None:
    """Load an existing ``.maxpat`` file into the patch instance.

    Args:
        self: Patch being initialized.
        filename: Existing patch path.
        reorder: Whether to renumber loaded objects after reading them.
        verbose: Legacy compatibility flag retained for the public API.
    """
    input_path = Path(filename)
    _LOGGER.debug("Patcher: loading patch from existing file: %s", input_path.name)

    patch_dict = _read_json_dict(input_path)
    self.load_objs_from_dict(patch_dict, verbose=verbose)
    self.load_patchcords_from_dict(patch_dict, verbose=verbose)
    self._patcher_dict = self.clean_patcher_dict(patch_dict)

    if reorder:
        self.reorder()
    _LOGGER.debug("Patcher: patch loaded from existing file: %s", input_path.name)


def load_objs_from_dict(
    self: MaxPatch,
    patch_dict: JSONDict,
    *,
    verbose: bool = True,
) -> None:
    """Load box objects from a serialized patch dictionary.

    Args:
        self: Patch being populated.
        patch_dict: Serialized patcher dictionary.
        verbose: Legacy compatibility flag retained for the public API.
    """
    del verbose
    self._num_objs = 0
    patcher = cast("dict[str, Any]", patch_dict["patcher"])
    for box in cast("list[Any]", patcher["boxes"]):
        obj = MaxObject(box, from_dict=True)
        self._num_objs += 1
        self._objs[obj.box_id] = obj
        _LOGGER.debug("Patcher: %s added, total objects %s", obj.name, self._num_objs)


def load_patchcords_from_dict(
    self: MaxPatch,
    patch_dict: JSONDict,
    *,
    verbose: bool = True,
) -> None:
    """Load patchcords from a serialized patch dictionary.

    Args:
        self: Patch being populated.
        patch_dict: Serialized patcher dictionary.
        verbose: Legacy compatibility flag retained for the public API.
    """
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
    """Strip box and patchcord data from a patch dictionary.

    Args:
        self: Unused patch reference kept for API symmetry.
        patch_dict: Serialized patcher dictionary.

    Returns:
        A copy-ready patch dictionary with ``boxes`` and ``lines`` cleared.
    """
    del self
    patcher = cast("dict[str, Any]", patch_dict["patcher"])
    patcher["boxes"] = []
    patcher["lines"] = []
    return patch_dict
