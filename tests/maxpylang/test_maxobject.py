"""Tests for MaxObject-level construction and behavior."""

import copy
import json
import logging
from pathlib import Path

import pytest
from _pytest.monkeypatch import MonkeyPatch

from maxpylang import MaxObject
from maxpylang.exceptions import UnknownObjectWarning

_CYCLE_INLETS = 2
_MESSAGE_OUTLETS = 1
_JS_FILE_INLETS = 2
_JS_FILE_OUTLETS = 3


def _write_js_file(tmp_path: Path, name: str = "demo.js") -> Path:
    """Write a js reference file with two inlets and three outlets."""
    path = tmp_path / name
    path.write_text("inlets = 2;\noutlets = 3;\n", encoding="utf-8")
    return path


def _write_abstraction_file(
    tmp_path: Path, name: str = "demo.maxpat", num_inlets: int = 1, num_outlets: int = 1
) -> Path:
    """Write a mock abstraction with controlled inlets/outlets."""
    boxes = [{"box": {"maxclass": "inlet"}} for _ in range(num_inlets)] + [
        {"box": {"maxclass": "outlet"}} for _ in range(num_outlets)
    ]
    path = tmp_path / name
    path.write_text(json.dumps({"patcher": {"boxes": boxes}}), encoding="utf-8")
    return path


def test_maxobject_user_methods_cover_known_and_unknown_paths(
    caplog: object,
) -> None:
    """Exercise known/unknown object paths and ensure expected user-facing output."""
    obj = MaxObject("cycle~ 440", color=[0.1, 0.2, 0.3, 0.4])

    assert obj.name == "cycle~"
    assert len(obj.ins) == _CYCLE_INLETS
    assert len(obj.outs) == _MESSAGE_OUTLETS
    assert obj.get_text() == "cycle~ 440"
    assert obj.get_extra_attribs()["color"] == [0.1, 0.2, 0.3, 0.4]

    obj.move(12, 34)
    assert obj.__dict__["_dict"]["box"]["patching_rect"][:2] == [12, 34]

    obj.edit(text="880 @fontsize 18", text_add="replace")
    caplog.clear()
    assert obj.get_text() == "cycle~ 880 @fontsize 18"
    assert obj.inspect() is None

    with caplog.at_level(logging.DEBUG, logger="maxpylang"):
        obj.debug()
    debug_output = caplog.text
    assert "name cycle~" in debug_output

    with pytest.warns(UnknownObjectWarning, match="this_object_is_missing"):
        unknown = MaxObject("this_object_is_missing")
    assert unknown.notknown() is True
    assert "this_object_is_missing" in repr(unknown)

    caplog.clear()
    unknown.edit(text="1")
    output = caplog.text
    assert "attempting edit on empty object" in output

    caplog.clear()
    obj.link()
    assert "cannot be linked to a file" in caplog.text


def test_maxobject_js_and_abstraction_paths(
    tmp_path: Path, monkeypatch: MonkeyPatch
) -> None:
    """Validate js and abstraction references created from files."""
    monkeypatch.chdir(tmp_path)
    _write_js_file(tmp_path)
    _write_abstraction_file(tmp_path)

    js_obj = MaxObject("js demo")
    assert js_obj.__dict__["_ext_file"] == str(tmp_path / "demo.js")
    assert js_obj.__dict__["_args"] == [3, 2, "demo.js"]
    assert len(js_obj.ins) == _JS_FILE_INLETS
    assert len(js_obj.outs) == _JS_FILE_OUTLETS

    js_obj.__dict__["_ext_file"] = None
    js_obj.link()
    assert js_obj.__dict__["_ext_file"] == str(tmp_path / "demo.js")

    abstraction = MaxObject("demo")
    assert abstraction.__dict__["_ref_file"] == "abstraction"
    assert abstraction.__dict__["_ext_file"] == "demo.maxpat"
    assert len(abstraction.ins) == 1
    assert len(abstraction.outs) == 1

    abstraction.edit(text="demo @fontsize 20", text_add="replace", bgcolor=[1, 2, 3, 4])
    assert abstraction.__dict__["_dict"]["box"]["text"] == "demo @fontsize 20"
    assert abstraction.__dict__["_dict"]["box"]["bgcolor"] == [1, 2, 3, 4]

    abstraction.link()
    assert abstraction.__dict__["_ext_file"] == "demo.maxpat"

    from_dict_obj = MaxObject(
        copy.deepcopy(js_obj.__dict__["_dict"]),
        from_dict=True,
    )
    assert from_dict_obj.__dict__["_args"] == [2, 3, "demo.js"]

    missing_js_dict = copy.deepcopy(js_obj.__dict__["_dict"])
    missing_js_dict["box"]["saved_object_attributes"]["filename"] = "missing.js"
    missing_js = MaxObject(missing_js_dict, from_dict=True)
    assert missing_js.__dict__["_args"] == [2, 3, "missing.js"]


def test_maxobject_explicit_js_link_updates_reference_paths(
    tmp_path: Path, monkeypatch: MonkeyPatch
) -> None:
    """Verify explicit link resolution updates paths from dict."""
    monkeypatch.chdir(tmp_path)

    (tmp_path / "demo.js").write_text("inlets = 2;\noutlets = 3;\n", encoding="utf-8")

    js_obj = MaxObject("js demo")
    assert js_obj.__dict__["_ext_file"] == str(tmp_path / "demo.js")
    assert js_obj.__dict__["_args"] == [3, 2, "demo.js"]

    js_obj.link("demo.js")
    assert js_obj.__dict__["_ext_file"] == str(tmp_path / "demo.js")

    js_from_dict = MaxObject(
        {
            "box": {
                "id": "obj-1",
                "maxclass": "newobj",
                "numinlets": 4,
                "numoutlets": 5,
                "patching_rect": [0, 0, 10, 10],
                "text": "js demo.js",
                "saved_object_attributes": {"filename": "demo.js"},
                "outlettype": ["", "", "", "", ""],
            }
        },
        from_dict=True,
    )
    assert js_from_dict.__dict__["_args"] == [4, 5, "demo.js"]


def test_maxobject_known_object_reference_lookup_and_ui_from_dict() -> None:
    """Resolve object metadata from refs and direct dict loading."""
    obj = MaxObject("toggle")
    assert obj.get_ref("sel").endswith("select.json")
    assert obj.get_ref("toggle").endswith("toggle.json")
    assert obj.get_info()["default"]["box"]["maxclass"] == "toggle"
    assert obj.notknown() is False
    assert repr(obj) == "toggle [toggle]"

    ui_dict = {
        "box": {
            "id": "obj-1",
            "maxclass": "toggle",
            "numinlets": 1,
            "numoutlets": 1,
            "outlettype": [""],
            "patching_rect": [0, 0, 20, 20],
            "text": "toggle",
        }
    }
    ui_obj = MaxObject(ui_dict, from_dict=True)
    assert ui_obj.name == "toggle"
    assert repr(ui_obj) == "toggle [toggle]"
