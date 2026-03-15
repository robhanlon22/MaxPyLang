"""Miscellaneous helper functions."""

from __future__ import annotations

from pathlib import Path

from maxpylang.tools.constants import obj_info_folder


def get_objs() -> dict[str, list[str]]:
    """Return available templated objects grouped by package."""
    packages = sorted(Path(obj_info_folder).glob("*/"))

    objs = {}
    for package_path in packages:
        package_name = package_path.name
        package_objs = sorted(path.stem for path in package_path.glob("*.json"))
        objs[package_name] = package_objs

    return objs
