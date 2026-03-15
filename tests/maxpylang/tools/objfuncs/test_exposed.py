"""Tests for objfuncs.exposed helpers."""

from pathlib import Path

import pytest
from _pytest.capture import CaptureFixture
from _pytest.monkeypatch import MonkeyPatch

from maxpylang import MaxObject
from maxpylang.exceptions import UnknownObjectWarning
from maxpylang.tools.objfuncs import exposed as obj_exposed


def test_move_updates_patch_position() -> None:
    """Verify move updates box coordinates."""
    obj = MaxObject("button")
    obj.move(10, 20)
    assert obj.__dict__["_dict"]["box"]["patching_rect"][:2] == [10, 20]


def test_link_restricts_to_js_and_abstractions(
    capsys: CaptureFixture[str],
) -> None:
    """Verify standard UI objects cannot be linked."""
    obj = MaxObject("toggle")
    obj.link()
    assert "cannot be linked to a file" in capsys.readouterr().out


def test_edit_noop_for_unknown_objects(capsys: CaptureFixture[str]) -> None:
    """Verify unknown objects still collect a no-op warning path."""
    with pytest.warns(UnknownObjectWarning, match="does_not_exist"):
        unknown = MaxObject("does_not_exist")
    unknown.edit(text="42")
    assert "attempting edit on empty object" in capsys.readouterr().out


def test_edit_obeys_args_validation_and_returns_for_invalid_input(
    capsys: CaptureFixture[str],
) -> None:
    """Verify invalid args abort edit with warning and no mutation."""

    class DummyEditObject:
        def __init__(self) -> None:
            self.name = "demo"
            self.__dict__["_dict"] = {"box": {"text": "demo"}}
            self.__dict__["_args"] = []
            self.__dict__["_text_attribs"] = {}
            self.__dict__["_ref_file"] = "ref.json"

        def notknown(self) -> bool:
            return False

        def parse_text(
            self, _text: str
        ) -> tuple[str, list[int], dict[str, list[str]]]:
            return "demo", [1], {}

        def get_info(self, _text: str = "") -> dict:
            return {"args": {}, "attribs": [], "in/out": {}, "default": {}}

        def args_valid(
            self, _name: str, _args: list[int], _arg_info: dict
        ) -> bool:
            return False

    obj_exposed.edit(DummyEditObject(), text="1", text_add="replace")
    # In this path args are invalid, so object remains unchanged.
    assert "demo not edited" in capsys.readouterr().out


def test_link_handles_js_and_abstraction_paths_and_rejects_non_linkable(
    capsys: CaptureFixture[str], tmp_path: Path, monkeypatch: MonkeyPatch
) -> None:
    """Verify js and abstraction paths can link while non-linkables fail."""
    monkeypatch.chdir(tmp_path)

    js_file = tmp_path / "demo.js"
    js_file.write_text("inlets = 1;\noutlets = 2;\n", encoding="utf-8")
    abstraction_file = tmp_path / "demo.maxpat"
    abstraction_file.write_text(
        '{"patcher": {"boxes": [{"box": {"maxclass": "inlet"}}]}}',
        encoding="utf-8",
    )

    js_obj = MaxObject("js demo")
    assert js_obj.__dict__["_ext_file"] == str(js_file)
    js_obj.link(js_file.name)
    assert js_obj.__dict__["_ext_file"] == str(js_file)
    assert js_obj.__dict__["_args"] == [2, 1, "demo.js"]

    with pytest.warns(UnknownObjectWarning, match="mystery"):
        unknown = MaxObject("mystery")
    unknown.link("demo.maxpat")
    assert unknown.__dict__["_ref_file"] == "abstraction"
    assert unknown.__dict__["_ext_file"] == "demo.maxpat"
    assert unknown.__dict__["_name"] == "demo"

    with pytest.warns(UnknownObjectWarning, match="still_missing"):
        missing = MaxObject("still_missing")
    missing.link("missing.maxpat")
    assert missing.__dict__["_ext_file"] is None

    non_linkable = MaxObject("toggle")
    non_linkable.link("demo.maxpat")
    assert "cannot be linked to a file" in capsys.readouterr().out
