"""Tests for objfuncs.reffile helpers."""

from pathlib import Path
from types import SimpleNamespace

import pytest

from maxpylang.tools.objfuncs import reffile


def test_get_ref_returns_existing_json(tmp_path: Path) -> None:
    """Resolve known objects from a mock obj-info folder."""
    dummy = SimpleNamespace(
        known_objs={"pkg": ["foo"]},
        obj_info_folder=str(tmp_path),
        check_aliases=lambda name: name,
    )
    package_folder = tmp_path / "pkg"
    package_folder.mkdir()
    json_file = package_folder / "foo.json"
    json_file.write_text("{}", encoding="utf-8")

    result = reffile.get_ref(dummy, "foo")

    assert Path(result) == json_file


def test_get_info_requires_ref_file() -> None:
    """Raise when the object has not been linked to a reference file."""
    dummy = SimpleNamespace(_ref_file=None)

    with pytest.raises(AssertionError, match="reference file is not set"):
        reffile.get_info(dummy)


def test_get_ref_returns_missing_known_path_when_json_file_is_absent(
    tmp_path: Path,
) -> None:
    """Known objects without a materialized json file return the computed path."""
    dummy = SimpleNamespace(
        known_objs={"pkg": ["ghost"]},
        obj_info_folder=str(tmp_path),
        check_aliases=lambda name: name,
    )
    package_folder = tmp_path / "pkg"
    package_folder.mkdir()

    result = reffile.get_ref(dummy, "ghost")

    assert Path(result) == package_folder / "ghost.json"
