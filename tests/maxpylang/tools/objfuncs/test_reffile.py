"""Tests for objfuncs.reffile helpers."""

import json
from pathlib import Path

import pytest
from _pytest.monkeypatch import MonkeyPatch

from maxpylang import MaxObject
from maxpylang.exceptions import UnknownObjectWarning


def test_get_ref_checks_aliases_abstractions_and_missing_lookup(
    tmp_path: Path, monkeypatch: MonkeyPatch
) -> None:
    """Verify alias, abstraction, and missing path behavior."""
    ref_root = tmp_path / "OBJ_INFO"
    package_dir = ref_root / "pkg"
    package_dir.mkdir(parents=True)
    ref_file = package_dir / "foo.json"
    ref_file.write_text("{}", encoding="utf-8")
    (ref_root / "obj_aliases.json").write_text(
        json.dumps({"bar": "foo"}), encoding="utf-8"
    )

    (tmp_path / "demo.maxpat").write_text("{}", encoding="utf-8")
    monkeypatch.chdir(tmp_path)

    obj = MaxObject("toggle")
    obj.obj_info_folder = str(ref_root)
    obj.known_objs = {"pkg": ["foo"]}

    assert obj.check_aliases("bar") == "foo"
    assert obj.get_ref("bar") == str(ref_file)
    assert obj.get_ref("demo") == "abstraction"

    with pytest.warns(UnknownObjectWarning, match="still_missing"):
        assert obj.get_ref("still_missing") == "not_found"


def test_get_info_reads_ref_file(tmp_path: Path) -> None:
    """Verify get_info reads and returns json contents."""
    obj = MaxObject("toggle")
    info = {"args": {}, "attribs": [], "in/out": {}, "default": {}}
    ref_file = tmp_path / "widget.json"
    ref_file.write_text(json.dumps(info), encoding="utf-8")
    assert obj.get_info(ref_file=str(ref_file)) == info
