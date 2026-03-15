"""Miscellaneous helper functions."""

import sys
from pathlib import Path

from maxpylang.tools.constants import obj_info_folder


def write_stdout(*parts: object) -> None:
    """Write a single line to stdout."""
    sys.stdout.write(" ".join(str(part) for part in parts) + "\n")


def get_objs() -> dict[str, list[str]]:
    """Return available templated objects grouped by package."""
    packages = sorted(Path(obj_info_folder).glob("*/"))

    objs = {}
    for package_path in packages:
        package_name = package_path.name
        package_objs = sorted(path.stem for path in package_path.glob("*.json"))
        objs[package_name] = package_objs

    return objs
