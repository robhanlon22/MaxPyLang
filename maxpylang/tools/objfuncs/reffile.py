"""Helpers for resolving and reading Max object reference files."""

from __future__ import annotations

import json
import warnings
from pathlib import Path
from typing import TYPE_CHECKING, cast

from maxpylang.exceptions import UnknownObjectWarning

if TYPE_CHECKING:
    from maxpylang.maxobject import MaxObject

ObjectInfo = dict[str, object]


def get_ref(self: MaxObject, name: str) -> str:
    """Return the reference file path or an abstraction marker."""
    aliased_name = self.check_aliases(name)
    ref_path: Path | None = None

    for package, obj_list in self.known_objs.items():
        if aliased_name not in obj_list:
            continue
        package_folder = Path(self.obj_info_folder) / package
        ref_path = package_folder / f"{aliased_name}.json"
        if ref_path.exists():
            return str(ref_path)

    if ref_path is None:
        abstraction_path = Path(aliased_name)
        if abstraction_path.exists() or Path(f"{aliased_name}.maxpat").exists():
            return "abstraction"
        warnings.warn(
            f"Unknown Max object: '{aliased_name}'",
            UnknownObjectWarning,
            stacklevel=4,
        )
        return "not_found"

    return str(ref_path)


def check_aliases(self: MaxObject, name: str) -> str:
    """Resolve known aliases for an object name."""
    aliases_path = Path(self.obj_info_folder) / "obj_aliases.json"
    obj_aliases = cast(
        "dict[str, str]",
        json.loads(aliases_path.read_text(encoding="utf-8")),
    )
    return obj_aliases.get(name, name)


def get_info(self: MaxObject, ref_file: str | None = None) -> ObjectInfo:
    """Read and return a reference file payload."""
    resolved_ref = self._ref_file if ref_file is None else ref_file
    if resolved_ref is None:
        message = "reference file is not set"
        raise AssertionError(message)
    ref_path = Path(resolved_ref)
    return cast("ObjectInfo", json.loads(ref_path.read_text(encoding="utf-8")))
