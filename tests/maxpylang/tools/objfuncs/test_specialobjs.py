"""Tests for objfuncs.specialobjs helpers."""

from __future__ import annotations

import json
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from pathlib import Path

    from _pytest.capture import CaptureFixture
    from _pytest.monkeypatch import MonkeyPatch

import pytest

from maxpylang import MaxObject
from maxpylang.tools.objfuncs import specialobjs

_NUM_INLET_DEFAULT = 2
_NUM_OUTLET_DEFAULT = 3
_EXPECTED_NUMINLETS = 2
_EXPECTED_NUMOUTLETS = 1
_VST_OUTLETS = 10
_ABSTRACTION_NOIN = 2
_ABSTRACTION_NOOUT = 1

class DummySpecialObject:
    """Fixture object for special-object tests."""

    _DEFAULT_NUMINLETS = _NUM_INLET_DEFAULT
    _DEFAULT_NUMOUTLETS = _NUM_OUTLET_DEFAULT

    def __init__(
        self,
        name: str = "js",
        args: list[str] | None = None,
        filename: str = "",
        text: str = "dummy",
    ) -> None:
        """Initialize a bare object-like object with shared test defaults."""
        self.name = name
        self.__dict__["_name"] = name
        self.__dict__["_args"] = list(args or [])
        self.__dict__["_ext_file"] = None
        self.__dict__["_dict"] = {
            "box": {
                "saved_object_attributes": {"filename": filename},
                "numinlets": self._DEFAULT_NUMINLETS,
                "numoutlets": self._DEFAULT_NUMOUTLETS,
                "save": ["prefix", ";"],
                "text": text,
            }
        }
        self.__dict__["edit_calls"] = []
        self.__dict__["update_abstraction_calls"] = []
        self.__dict__["added_attribs"] = None
        self.__dict__["made_xlets"] = False
        self.__dict__["updated_text"] = False
        self.__dict__["_ref_file"] = None

    def edit(self, **kwargs: object) -> None:
        """Capture edit calls for inspection."""
        self.__dict__["edit_calls"].append(kwargs)

    def update_text(self) -> None:
        """Track that update_text was called."""
        self.__dict__["updated_text"] = True

    def get_js_io(
        self, filename: str, log_var: str | None = None
    ) -> tuple[int | str, int | str]:
        """Proxy through to the real JS io parser."""
        return specialobjs.get_js_io(self, filename, log_var=log_var)

    def get_js_filename(self) -> str | None:
        """Return the resolved js filename."""
        return specialobjs.get_js_filename(self)

    def update_js_from_file(
        self, filename: str, log_var: str | None = None
    ) -> None:
        """Proxy through to the real js-file updater."""
        return specialobjs.update_js_from_file(self, filename, log_var=log_var)

    def update_abstraction_from_file(
        self, text: str, extra_attribs: dict, log_var: str | None = None
    ) -> None:
        """Capture abstraction update calls."""
        self.__dict__["update_abstraction_calls"].append((text, extra_attribs, log_var))

    def make_xlets_from_self_dict(self) -> None:
        """Track when xlet creation is requested."""
        self.__dict__["made_xlets"] = True

    def get_all_valid_attribs(
        self, text_attribs: dict, extra_attribs: dict, attrib_info: list
    ) -> tuple[dict, dict]:
        """Return text attribs while passing through extra attrib payload."""
        return text_attribs, {"sanitized": extra_attribs, "attrib_info": attrib_info}

    def add_extra_attribs(self, extra_attribs: dict) -> None:
        """Capture calls made to add extra attributes."""
        self.__dict__["added_attribs"] = extra_attribs

    def get_abstraction_io(self) -> tuple[int, int]:
        """Proxy to abstraction in/out helper."""
        return specialobjs.get_abstraction_io(self)

    def get_text(self) -> str:
        """Return the backing text field."""
        return self.__dict__["_dict"]["box"]["text"]

    def get_extra_attribs(self) -> dict:
        """Return mocked common attributes."""
        return {"volume": 11}


def test_get_js_filename_uses_first_non_numeric_arg_and_appends_js() -> None:
    """Verify parse chooses first non-numeric arg as js name."""
    obj = DummySpecialObject(args=["2", "3", "script"])
    assert specialobjs.get_js_filename(obj) == "script.js"


def test_get_js_filename_returns_none_when_no_filename_arg() -> None:
    """Verify missing filename arg returns None."""
    obj = DummySpecialObject(args=["2", "3"])
    assert specialobjs.get_js_filename(obj) is None


def test_get_js_io_reads_file_or_defaults(
    tmp_path: Path, capsys: CaptureFixture[str]
) -> None:
    """Verify io markers fall back to defaults when missing."""
    js_file = tmp_path / "counts.js"
    js_file.write_text("inlets = 4; // comment\noutlets = 2;\n", encoding="utf-8")
    fallback_file = tmp_path / "fallback.js"
    fallback_file.write_text("console.log('no io markers');\n", encoding="utf-8")
    obj = DummySpecialObject()

    assert specialobjs.get_js_io(obj, str(js_file), log_var="scan") == (
        "4",
        "2",
    )
    assert specialobjs.get_js_io(obj, str(fallback_file), log_var="scan") == (1, 1)
    output = capsys.readouterr().out
    assert "defaults assumed (1 inlet, 1 outlet)" in output


def test_update_js_from_file_updates_args_and_logs(
    tmp_path: Path, capsys: CaptureFixture[str]
) -> None:
    """Verify js inlet/outlet update mutates args and logs."""
    js_file = tmp_path / "counts.js"
    js_file.write_text("inlets = 5;\noutlets = 7;\n", encoding="utf-8")
    obj = DummySpecialObject()

    specialobjs.update_js_from_file(obj, str(js_file), log_var="creation")

    assert obj.__dict__["_args"] == ["7", "5", str(js_file)]
    assert obj.__dict__["edit_calls"] == [
        {"text": f"7 5 {js_file}", "text_add": "replace"}
    ]
    assert "7 outlets" in capsys.readouterr().out


def test_create_js_reports_missing_filename_and_file(
    capsys: CaptureFixture[str],
) -> None:
    """Verify create_js handles missing filename and missing file cases."""
    no_name = DummySpecialObject(args=["1", "2"])
    specialobjs.create_js(no_name, from_dict=False)
    missing = DummySpecialObject(args=["1", "2", "missing"])
    specialobjs.create_js(missing, from_dict=False)

    output = capsys.readouterr().out
    assert "no filename specified" in output
    assert "missing.js not found" in output
    assert missing.__dict__["_ext_file"] is None


def test_create_js_and_abstraction_update_state(
    tmp_path: Path, monkeypatch: MonkeyPatch, capsys: CaptureFixture[str]
) -> None:
    """Verify create_js updates state for both raw and from-dict paths."""
    js_file = tmp_path / "script.js"
    js_file.write_text("inlets = 1;\noutlets = 2;\n", encoding="utf-8")
    monkeypatch.chdir(tmp_path)

    created = DummySpecialObject(args=["1", "2", "script"])
    specialobjs.create_js(created, from_dict=False)
    assert (
        created.__dict__["_dict"]["box"]["saved_object_attributes"]["filename"]
        == "script.js"
    )
    assert created.__dict__["_ext_file"] == str(js_file.resolve())
    assert created.__dict__["_args"] == ["2", "1", "script.js"]

    from_dict_obj = DummySpecialObject(filename="script.js")
    specialobjs.create_js(from_dict_obj, from_dict=True)
    assert from_dict_obj.__dict__["_args"] == [
        _ABSTRACTION_NOIN,
        _ABSTRACTION_NOOUT,
        "script.js",
    ]
    assert from_dict_obj.__dict__["updated_text"] is True
    assert "found, parsing for inlet/outlet numbers" in capsys.readouterr().out


def test_link_js_handles_no_filename_existing_and_missing_file(
    tmp_path: Path, monkeypatch: MonkeyPatch, capsys: CaptureFixture[str]
) -> None:
    """Verify link_js reports missing and resolves present files."""
    js_file = tmp_path / "linked.js"
    js_file.write_text("inlets = 8;\noutlets = 9;\n", encoding="utf-8")
    monkeypatch.chdir(tmp_path)

    no_filename = DummySpecialObject(filename="")
    specialobjs.link_js(no_filename)
    assert "no filename specified" in capsys.readouterr().out

    linked = DummySpecialObject()
    specialobjs.link_js(linked, "linked.js")
    assert linked.__dict__["_ext_file"] == str(js_file.resolve())
    assert linked.__dict__["_args"] == ["9", "8", "linked.js"]

    missing = DummySpecialObject()
    specialobjs.link_js(missing, "absent.js")
    assert "absent.js not found" in capsys.readouterr().out


def test_create_abstraction_and_update_from_file_paths(
    capsys: CaptureFixture[str],
) -> None:
    """Verify abstraction creation and update paths."""
    from_dict_obj = DummySpecialObject(name="subpatch")
    specialobjs.create_abstraction(from_dict_obj, from_dict=True)
    assert from_dict_obj.__dict__["_ext_file"] == "subpatch.maxpat"
    assert from_dict_obj.__dict__["made_xlets"] is True
    assert "abstraction created" in capsys.readouterr().out

    created = DummySpecialObject(name="explicit.maxpat")
    specialobjs.create_abstraction(
        created, text="explicit @gain 2", extra_attribs={"gain": 2}, from_dict=False
    )
    assert created.__dict__["_ext_file"] == "explicit.maxpat"
    assert created.__dict__["update_abstraction_calls"] == [
        ("explicit @gain 2", {"gain": 2}, "creation")
    ]


def test_update_abstraction_from_file_builds_dict_and_logs(
    capsys: CaptureFixture[str]
) -> None:
    """Verify explicit update updates abstraction dict and xlet metadata."""
    obj = DummySpecialObject(name="subpatch")
    obj.get_abstraction_io = lambda: (2, 1)

    specialobjs.update_abstraction_from_file(
        obj, "subpatch @gain 2", {"gain": 2}, log_var="link"
    )

    assert obj.__dict__["_dict"]["box"]["numinlets"] == _EXPECTED_NUMINLETS
    assert obj.__dict__["_dict"]["box"]["numoutlets"] == _EXPECTED_NUMOUTLETS
    assert obj.__dict__["_dict"]["box"]["outlettype"] == [""]
    assert obj.__dict__["_dict"]["box"]["patching_rect"] == [0.0, 0.0]
    assert obj.__dict__["_dict"]["box"]["text"] == "subpatch @gain 2"
    assert obj.__dict__["added_attribs"] == {
        "sanitized": {"gain": 2},
        "attrib_info": [{"name": "COMMON"}],
    }
    assert obj.__dict__["made_xlets"] is True
    assert "file found, abstraction created" in capsys.readouterr().out


def test_get_abstraction_io_counts_inlet_outlet_numbers(tmp_path: Path) -> None:
    """Verify abstraction io counter detects inlet/outlet object counts."""
    abstraction_file = tmp_path / "demo.maxpat"
    abstraction_file.write_text(
        json.dumps(
            {
                "patcher": {
                    "boxes": [
                        {"box": {"maxclass": "inlet"}},
                        {"box": {"maxclass": "outlet"}},
                        {"box": {"maxclass": "comment"}},
                    ]
                }
            }
        ),
        encoding="utf-8",
    )
    obj = DummySpecialObject(name="demo")
    obj.__dict__["_ext_file"] = str(abstraction_file)

    assert specialobjs.get_abstraction_io(obj) == (1, 1)


def test_link_abstraction_updates_obj_from_existing_or_reports_missing(
    tmp_path: Path, monkeypatch: MonkeyPatch, capsys: CaptureFixture[str]
) -> None:
    """Verify link_abstraction resolves existing file and handles missing paths."""
    abstraction_file = tmp_path / "linked.maxpat"
    abstraction_file.write_text(
        json.dumps({"patcher": {"boxes": []}}),
        encoding="utf-8",
    )
    monkeypatch.chdir(tmp_path)

    linked = DummySpecialObject(name="linked")
    specialobjs.link_abstraction(linked)
    assert linked.__dict__["_ref_file"] == "abstraction"
    assert linked.__dict__["_ext_file"] == "linked.maxpat"
    assert linked.__dict__["_name"] == "linked"
    assert linked.__dict__["update_abstraction_calls"] == [
        ("dummy", {"volume": 11}, "link")
    ]

    missing = DummySpecialObject(name="missing")
    specialobjs.link_abstraction(missing, "missing")
    assert "missing.maxpat not found" in capsys.readouterr().out


@pytest.mark.parametrize(
    ("args", "expected"),
    [
        (
            ["b", "i", "3.5", "s", "custom"],
            ["bang", "int", "float", "", "custom"],
        ),
        (["7", "f", "x"], ["int", "float", ""]),
        (["i", "3", "f"], ["int", "int", "float"]),
    ],
)
def test_trigger_and_unpack_out_type_helpers(
    args: list[str], expected: list[str]
) -> None:
    """Verify helper dispatches expected trigger/unpack output typing."""
    obj = DummySpecialObject(args=args)
    if args[0] == "b":
        assert specialobjs.get_trigger_out_types(obj) == expected
    else:
        assert specialobjs.get_unpack_out_types(obj) == expected


def test_vst_instantiation_updates_save_field_and_outlets() -> None:
    """Verify vst save field encodes plug name and outlet count."""
    obj = MaxObject("vst~ 4 plugin")
    assert len(obj.outs) == _VST_OUTLETS
    assert obj.__dict__["_dict"]["box"]["save"][-4:] == [0, 4, "plugin", ";"]


def test_update_vst_rewrites_save_field() -> None:
    """Verify vst update rewrites argument save signature."""
    obj = DummySpecialObject(args=["plug", "preset"])
    specialobjs.update_vst(obj)
    assert obj.__dict__["_dict"]["box"]["save"] == ["prefix", "plug", "preset", ";"]
