"""Tests for import and object metadata generation helpers."""

from __future__ import annotations

import json
from pathlib import Path
from types import SimpleNamespace
from typing import TYPE_CHECKING

from defusedxml.ElementTree import parse as parse_xml

from maxpylang import importobjs

if TYPE_CHECKING:
    from _pytest.capture import CaptureFixture
    from _pytest.monkeypatch import MonkeyPatch


def write_maxref(
    path: Path, name: str, category: str | None = None, body: str = ""
) -> None:
    """Write a temporary maxref XML file for import tests."""
    category_attr = f' category="{category}"' if category is not None else ""
    path.write_text(
        f'<c74object name="{name}"{category_attr}>{body}</c74object>',
        encoding="utf-8",
    )


def _read_xml_root(path: Path) -> object:
    return parse_xml(str(path)).getroot()

def test_import_objs_creates_info_root_and_delegates(
    monkeypatch: MonkeyPatch, tmp_path: Path
) -> None:
    """Verify import entrypoint creates metadata folders and delegates work."""
    calls = []
    obj_info_root = tmp_path / "OBJ_INFO"
    monkeypatch.setattr(importobjs, "obj_info_folder", str(obj_info_root))
    monkeypatch.setattr(
        importobjs,
        "get_package_paths",
        lambda packages: calls.append(("paths", packages)) or {"max": "/refs/max"},
    )
    monkeypatch.setattr(
        importobjs,
        "prep_make_info_folders",
        lambda package_paths, overwrite=False: (
            calls.append(("prep", package_paths, overwrite))
            or {"max": str(obj_info_root / "max")}
        ),
    )
    monkeypatch.setattr(
        importobjs,
        "save_obj_info",
        lambda package_paths, info_folders: calls.append(
            ("save", package_paths, info_folders)
        ),
    )
    monkeypatch.setattr(
        importobjs,
        "generate_stubs",
        lambda package_paths, info_folders: calls.append(
            ("stubs", package_paths, info_folders)
        ),
    )

    importobjs.import_objs("max", overwrite=True)

    assert obj_info_root.exists()
    assert calls == [
        ("paths", ["max"]),
        ("prep", {"max": "/refs/max"}, True),
        ("save", {"max": "/refs/max"}, {"max": str(obj_info_root / "max")}),
        ("stubs", {"max": "/refs/max"}, {"max": str(obj_info_root / "max")}),
    ]


def test_get_package_paths_expands_vanilla_and_custom_packages(
    monkeypatch: MonkeyPatch,
) -> None:
    """Verify package names are resolved to default and docs paths."""
    constants = {
        "max_refpath": "/Applications/Max/refs",
        "packages_path": "/Users/rob/Documents/Max Packages",
    }
    monkeypatch.setattr(importobjs, "get_constant", lambda name: constants[name])

    result = importobjs.get_package_paths(["vanilla", "custom"])

    assert result == {
        "max": "/Applications/Max/refs/max-ref",
        "msp": "/Applications/Max/refs/msp-ref",
        "jit": "/Applications/Max/refs/jit-ref",
        "custom": "/Users/rob/Documents/Max Packages/custom/docs",
    }


def test_prep_make_info_folders_handles_missing_skip_new_and_overwrite(
    monkeypatch: MonkeyPatch, tmp_path: Path, capsys: CaptureFixture[str]
) -> None:
    """Verify folder creation handles missing, skipped, and overwritten cases."""
    obj_info_root = tmp_path / "OBJ_INFO"
    obj_info_root.mkdir()
    monkeypatch.setattr(importobjs, "obj_info_folder", str(obj_info_root))

    existing_package_path = tmp_path / "existing-ref"
    existing_package_path.mkdir()
    skipped_info = obj_info_root / "skipme"
    skipped_info.mkdir()
    overwritten_info = obj_info_root / "replace-me"
    overwritten_info.mkdir()
    (overwritten_info / "old.json").write_text("stale", encoding="utf-8")

    result = importobjs.prep_make_info_folders(
        {
            "missing": str(tmp_path / "missing-ref"),
            "skipme": str(existing_package_path),
            "replace-me": str(existing_package_path),
            "brand-new": str(existing_package_path),
        },
        overwrite=True,
    )

    assert result == {
        "skipme": str(skipped_info),
        "replace-me": str(overwritten_info),
        "brand-new": str(obj_info_root / "brand-new"),
    }
    assert not (overwritten_info / "old.json").exists()
    assert (obj_info_root / "brand-new").exists()
    output = capsys.readouterr().out
    assert "package missing not found" in output
    assert "prepping to re-import skipme" in output
    assert "prepping to re-import replace-me" in output
    assert "prepping to import brand-new" in output


def test_prep_make_info_folders_skips_existing_when_not_overwriting(
    monkeypatch: MonkeyPatch, tmp_path: Path, capsys: CaptureFixture[str]
) -> None:
    """Verify existing folders are skipped when overwrite is disabled."""
    obj_info_root = tmp_path / "OBJ_INFO"
    obj_info_root.mkdir()
    monkeypatch.setattr(importobjs, "obj_info_folder", str(obj_info_root))
    package_path = tmp_path / "pkg-ref"
    package_path.mkdir()
    existing_info = obj_info_root / "pkg"
    existing_info.mkdir()

    result = importobjs.prep_make_info_folders(
        {"pkg": str(package_path)}, overwrite=False
    )

    assert result == {}
    assert "pkg previously imported, skipping..." in capsys.readouterr().out


def test_is_unlisted_and_get_obj_aliases_handle_category_and_missing_text(
    tmp_path: Path,
) -> None:
    """Verify unlisted and alias extraction behavior."""
    listed = tmp_path / "listed.maxref.xml"
    write_maxref(listed, "button")
    unlisted = tmp_path / "unlisted.maxref.xml"
    write_maxref(unlisted, "button", category="Unlisted")

    assert importobjs.is_unlisted(str(listed)) is False
    assert importobjs.is_unlisted(str(unlisted)) is True
    assert importobjs.get_obj_aliases(
        {
            "button": {"box": {"text": "button"}},
            "select": {"box": {"text": "sel"}},
            "missing": {"box": {}},
        },
        ["button", "select", "missing"],
    ) == {"sel": "select"}


def test_get_default_obj_info_uses_patch_save_open_sleep_and_cleans_file(
    monkeypatch: MonkeyPatch, tmp_path: Path
) -> None:
    """Verify defaults import writes temporary patch and cleans temporary files."""
    calls = []

    class DummyPatch:
        def __init__(self, *, verbose: bool = False) -> None:
            assert verbose is False
            self.__dict__["_patcher_dict"] = {"patcher": {"boxes": [], "lines": []}}

        def save(self, filename: str, *, verbose: bool = False) -> None:
            calls.append(("save", filename, verbose))
            Path(filename).write_text(
                json.dumps(
                    {
                        "patcher": {
                            "boxes": [{"box": {"text": f"tool-{i}"}} for i in range(6)]
                            + [
                                {"box": {"text": "alpha-default"}},
                                {"box": {"text": "beta-default"}},
                            ]
                        }
                    }
                ),
                encoding="utf-8",
            )

    monkeypatch.chdir(tmp_path)
    monkeypatch.setattr(importobjs, "MaxPatch", DummyPatch)
    monkeypatch.setattr(
        importobjs,
        "get_constant",
        lambda name: 2 if name == "wait_time" else None,
    )
    monkeypatch.setattr(
        importobjs,
        "add_save_close",
        lambda patch: calls.append(
            ("add_save_close", patch.__dict__["_patcher_dict"].copy())
        ),
    )
    monkeypatch.setattr(
        importobjs,
        "add_barebones_objs",
        lambda refs, _patch: calls.append(("add_barebones_objs", tuple(refs))),
    )
    monkeypatch.setattr(
        importobjs.subprocess,
        "call",
        lambda cmd: calls.append(("open", cmd)) or 0,
    )
    monkeypatch.setattr(
        importobjs.time,
        "sleep",
        lambda seconds: calls.append(("sleep", seconds)),
    )

    result = importobjs.get_default_obj_info(
        "demo", ["alpha.maxref.xml", "beta.maxref.xml"], ["alpha", "beta"]
    )

    assert result == {
        "alpha": {"box": {"text": "alpha-default"}},
        "beta": {"box": {"text": "beta-default"}},
    }
    assert ("save", "defaults_demo.maxpat", False) in calls
    assert ("open", ["open", "defaults_demo.maxpat"]) in calls
    assert ("sleep", 2) in calls
    assert not (tmp_path / "defaults_demo.maxpat").exists()


def test_add_barebones_objs_reads_xml_names_into_patch(tmp_path: Path) -> None:
    """Verify barebone object creation from ref paths collects names."""
    alpha = tmp_path / "alpha.maxref.xml"
    beta = tmp_path / "beta.maxref.xml"
    write_maxref(alpha, "alpha")
    write_maxref(beta, "beta")
    added = []
    patch = SimpleNamespace(add_barebones_obj=added.append)

    importobjs.add_barebones_objs([str(alpha), str(beta)], patch)

    assert added == ["alpha", "beta"]


def test_add_save_close_copies_boxes_and_lines_from_import_tools(
    tmp_path: Path, monkeypatch: MonkeyPatch
) -> None:
    """Verify `add_save_close` reads `import_tools` and appends metadata."""
    import_tools = tmp_path / "import_tools.json"
    import_tools.write_text(
        json.dumps({"boxes": [{"box": {"text": "save"}}], "lines": [{"line": 1}]}),
        encoding="utf-8",
    )
    monkeypatch.setattr(importobjs, "import_tools", str(import_tools))
    patch = SimpleNamespace()
    patch.__dict__["_patcher_dict"] = {"patcher": {"boxes": [], "lines": []}}

    importobjs.add_save_close(patch)

    assert patch.__dict__["_patcher_dict"]["patcher"] == {
        "boxes": [{"box": {"text": "save"}}],
        "lines": [{"line": 1}],
    }


def test_get_objargs_by_flag_and_get_objarg_info_parse_required_optional_and_types(
    tmp_path: Path,
) -> None:
    """Verify required and optional argument parsing handles mixed type tokens."""
    ref = tmp_path / "demo.maxref.xml"
    write_maxref(
        ref,
        "demo",
        body="""
<objarglist>
  <objarg name="count" optional="0" type="int, float, or string" />
  <objarg name="OBJARG_NAME" optional="0" type="OBJARG_TYPE" />
  <objarg name="mode" optional="1" />
</objarglist>
""",
    )
    root = _read_xml_root(ref)

    assert importobjs.get_objargs_by_flag(root, "[@optional='0']") == [
        {"name": "count", "type": ["int", "float"]}
    ]
    assert importobjs.get_objargs_by_flag(root, "[@optional='1']") == [
        {"name": "mode", "type": []}
    ]
    assert importobjs.get_objarg_info([str(ref)], ["demo"]) == {
        "demo": {
            "required": [{"name": "count", "type": ["int", "float"]}],
            "optional": [{"name": "mode", "type": []}],
        }
    }


def test_get_objattrib_info_and_get_objinout_info_cover_ui_non_ui_and_missing_io(
    tmp_path: Path, monkeypatch: MonkeyPatch
) -> None:
    """Verify attrib and i/o info combines UI and non-UI object paths."""
    non_ui = tmp_path / "signal.maxref.xml"
    write_maxref(
        non_ui,
        "signal",
        category="MSP",
        body="""
<attributelist>
  <attribute name="gain" type="float" size="1" get="1" set="1" />
</attributelist>
""",
    )
    ui = tmp_path / "dial.maxref.xml"
    write_maxref(
        ui,
        "dial",
        category="U/I",
        body="""
<attributelist>
  <attribute name="presentation" type="int" size="1" />
</attributelist>
""",
    )

    attribs = importobjs.get_objattrib_info([str(non_ui), str(ui)], ["signal", "dial"])
    assert attribs["signal"][0] == {"name": "COMMON"}
    assert attribs["signal"][1] == {"name": "gain", "type": "float", "size": "1"}
    assert attribs["dial"] == [{"name": "presentation", "type": "int", "size": "1"}]

    io_root = tmp_path / "io"
    io_root.mkdir()
    (io_root / "demo_io.json").write_text(
        json.dumps({"signal": {"numoutlets": [{"type": "signal"}]}}),
        encoding="utf-8",
    )
    monkeypatch.setattr(importobjs, "obj_io_folder", str(io_root))

    assert importobjs.get_objinout_info("demo", ["signal", "dial"]) == {
        "signal": {"numoutlets": [{"type": "signal"}]},
        "dial": {},
    }
    assert importobjs.get_objinout_info("missing", ["signal"]) == {"signal": {}}


def test_save_obj_info_filters_unlisted_writes_json_and_alias_file(
    tmp_path: Path, monkeypatch: MonkeyPatch, capsys: CaptureFixture[str]
) -> None:
    """Verify unlisted objects are skipped and aliases are persisted."""
    obj_info_root = tmp_path / "OBJ_INFO"
    obj_info_root.mkdir()
    monkeypatch.setattr(importobjs, "obj_info_folder", str(obj_info_root))
    monkeypatch.setattr(importobjs, "known_aliases", {"t": "trigger"})

    ref_root = tmp_path / "refs"
    ref_root.mkdir()
    listed_ref = ref_root / "alpha.maxref.xml"
    write_maxref(listed_ref, "alpha")
    unlisted_ref = ref_root / "beta.maxref.xml"
    write_maxref(unlisted_ref, "beta", category="Unlisted")

    package_folder = obj_info_root / "demo"
    package_folder.mkdir()

    monkeypatch.setattr(
        importobjs,
        "get_default_obj_info",
        lambda _package, _refs, _names: {
            "alpha": {"box": {"text": "alias-alpha"}}
        },
    )
    monkeypatch.setattr(
        importobjs,
        "get_obj_aliases",
        lambda _default_info, _names: {"alias-alpha": "alpha"},
    )
    monkeypatch.setattr(
        importobjs,
        "get_objarg_info",
        lambda _refs, _names: {
            "alpha": {"required": [{"name": "count"}], "optional": []}
        },
    )
    monkeypatch.setattr(
        importobjs,
        "get_objattrib_info",
        lambda _refs, _names: {"alpha": [{"name": "COMMON"}]},
    )
    monkeypatch.setattr(
        importobjs,
        "get_objinout_info",
        lambda _package, _names: {"alpha": {"numoutlets": [{"type": "signal"}]}},
    )

    importobjs.save_obj_info({"demo": str(ref_root)}, {"demo": str(package_folder)})

    saved_obj = json.loads((package_folder / "alpha.json").read_text(encoding="utf-8"))
    assert saved_obj == {
        "default": {"box": {"text": "alias-alpha"}},
        "args": {"required": [{"name": "count"}], "optional": []},
        "attribs": [{"name": "COMMON"}],
        "in/out": {"numoutlets": [{"type": "signal"}]},
        "doc": {},
    }
    aliases = json.loads(
        (obj_info_root / "obj_aliases.json").read_text(encoding="utf-8")
    )
    assert aliases == {"t": "trigger", "alias-alpha": "alpha"}
    output = capsys.readouterr().out
    assert "importing demo objects..." in output
    assert "1 object info files saved" in output
    assert "object aliases saved successfully" in output


def test_get_obj_doc_info_and_strip_xml_text_extracts_semantic_sections(
    tmp_path: Path,
) -> None:
    """Verify XML metadata parsing removes formatting tags and preserves details."""
    ref_file = tmp_path / "demo.maxref.xml"
    write_maxref(
        ref_file,
        "demo",
        body="""
        <digest>Hello <o>world</o></digest>
        <description>Main <m>description</m></description>
        <inletlist>
          <inlet id="0" type="signal">
            <digest>Signal in</digest>
            <description>Input <br /> path</description>
          </inlet>
          <inlet id="1" type="float">
            <digest>Aux in</digest>
            <description>Input</description>
          </inlet>
        </inletlist>
        <outletlist>
          <outlet id="1" type="int">
            <digest>Count out</digest>
            <description>Output path</description>
          </outlet>
        </outletlist>
        <methodlist>
          <method name="bang">
            <digest>Fire</digest>
            <description>Trigger action</description>
            <arglist>
              <arg name="value" type="int" />
            </arglist>
          </method>
        </methodlist>
""",
    )

    xml_snippet = tmp_path / "snippet.maxref.xml"
    xml_snippet.write_text("<x>Hello <o>there</o><br/>!</x>", encoding="utf-8")
    stripped = importobjs.strip_xml_text(_read_xml_root(xml_snippet))
    assert stripped == "Hello there!"

    result = importobjs.get_obj_doc_info([str(ref_file)], ["demo"])
    assert result == {
        "demo": {
            "digest": "Hello world",
            "description": "Main description",
            "inlets": [
                {
                    "id": "0",
                    "type": "signal",
                    "digest": "Signal in",
                    "description": "Input  path",
                },
                {
                    "id": "1",
                    "type": "float",
                    "digest": "Aux in",
                    "description": "Input",
                },
            ],
            "outlets": [
                {
                    "id": "1",
                    "type": "int",
                    "digest": "Count out",
                    "description": "Output path",
                }
            ],
            "methods": [
                {
                    "name": "bang",
                    "digest": "Fire",
                    "description": "Trigger action",
                    "args": [{"name": "value", "type": "int"}],
                }
            ],
        }
    }


def test_generate_stubs_writes_modules_and_warning_suppressing_init(
    tmp_path: Path,
    monkeypatch: MonkeyPatch,
 ) -> None:
    """Verify generated stubs include object exports and init warning suppression."""
    fake_importobjs = tmp_path / "fake_importobjs.py"
    fake_importobjs.write_text("# stub", encoding="utf-8")
    monkeypatch.setattr(importobjs, "__file__", str(fake_importobjs))

    empty_folder = tmp_path / "OBJ_INFO" / "empty"
    empty_folder.mkdir(parents=True)
    info_folder = tmp_path / "OBJ_INFO" / "demo"
    info_folder.mkdir(parents=True)
    (info_folder / "in.json").write_text(
        json.dumps(
            {
                "doc": {"digest": "Keyword object", "methods": [{"name": "bang"}]},
                "args": {"required": [], "optional": []},
                "attribs": [{"name": "COMMON"}, {"name": "style"}],
            },
            indent=2,
        ),
        encoding="utf-8",
    )
    (info_folder / "2d.wave~.json").write_text(
        json.dumps(
            {
                "doc": {
                    "description": "Generated object",
                    "inlets": [
                        {"id": "0", "type": "signal", "digest": "input"},
                        {"id": "1", "digest": "sidechain"},
                        {"id": "2", "type": "float"},
                    ],
                    "outlets": [
                        {"id": "0", "type": "signal", "digest": "output"},
                        {"id": "1", "digest": "status"},
                        {"id": "2", "type": "int"},
                    ],
                },
                "args": {
                    "required": [{"name": "freq", "type": ["number"]}],
                    "optional": [{"name": "mode", "type": ["symbol"]}],
                },
                "attribs": [{"name": "COMMON"}, {"name": "hidden"}],
            },
            indent=2,
        ),
        encoding="utf-8",
    )

    importobjs.generate_stubs(
        {}, {"empty": str(empty_folder), "demo": str(info_folder)}
    )

    objects_dir = tmp_path / "objects"
    stub_text = (objects_dir / "demo.py").read_text(encoding="utf-8")

    assert "_2d_wave_tilde" in stub_text
    assert "in_ = MaxObject('in')" in stub_text
    assert "Args:" in stub_text
    assert "Messages: bang" in stub_text
    assert "1: sidechain" in stub_text


def test_importobjs_doc_helpers_and_doc_info(
    tmp_path: Path,
    monkeypatch: MonkeyPatch,
    capsys: CaptureFixture[str],
) -> None:
    """Verify doc helpers produce expected metadata and public stub generation text."""
    rich_ref = tmp_path / "rich.maxref.xml"
    rich_ref.write_text(
        """
<c74object name="2d.wave~">
  <digest>Signal <b>digest</b></digest>
  <description>Main <i>description</i>.</description>
<inletlist>
    <inlet id="0" type="signal">
      <digest>Signal input</digest>
    </inlet>
    <inlet id="1">
      <digest>Bang input</digest>
    </inlet>
    <inlet id="2" type="int" />
  </inletlist>
  <outletlist>
    <outlet id="0" type="signal">
      <digest>Signal output</digest>
    </outlet>
    <outlet id="1">
      <digest>Status output</digest>
    </outlet>
    <outlet id="2" type="int" />
  </outletlist>
  <methodlist>
    <method name="bang">
      <digest>Trigger now</digest>
      <description>Force output.</description>
      <arglist>
        <arg name="force" type="int" />
      </arglist>
    </method>
  </methodlist>
</c74object>
""".strip(),
        encoding="utf-8",
    )
    placeholder_ref = tmp_path / "placeholder.maxref.xml"
    placeholder_ref.write_text(
        """
<c74object name="in">
  <digest>TEXT_HERE</digest>
  <description>TEXT_HERE</description>
  <methodlist>
    <method name="noop">
      <digest>TEXT_HERE</digest>
      <description>TEXT_HERE</description>
    </method>
  </methodlist>
</c74object>
""".strip(),
        encoding="utf-8",
    )

    assert importobjs.strip_xml_text(None) == ""
    snippet_file = tmp_path / "snippet_digest.maxref.xml"
    snippet_file.write_text("<digest>Hello <b>there</b></digest>", encoding="utf-8")
    assert (
        importobjs.strip_xml_text(_read_xml_root(snippet_file))
        == "Hello there"
    )

    doc_info = importobjs.get_obj_doc_info(
        [str(rich_ref), str(placeholder_ref)], ["2d.wave~", "in"]
    )
    assert doc_info["2d.wave~"] == {
        "digest": "Signal digest",
        "description": "Main description.",
        "inlets": [
            {"id": "0", "type": "signal", "digest": "Signal input"},
            {"id": "1", "digest": "Bang input"},
            {"id": "2", "type": "int"},
        ],
        "outlets": [
            {"id": "0", "type": "signal", "digest": "Signal output"},
            {"id": "1", "digest": "Status output"},
            {"id": "2", "type": "int"},
        ],
        "methods": [
            {
                "name": "bang",
                "digest": "Trigger now",
                "description": "Force output.",
                "args": [{"name": "force", "type": "int"}],
            }
        ],
    }
    assert doc_info["in"] == {"methods": [{"name": "noop"}]}

    assert importobjs.sanitize_py_name("2d.wave~") == "_2d_wave_tilde"
    assert importobjs.sanitize_py_name("in") == "in_"
    assert importobjs.sanitize_py_name("live.dial") == "live_dial"

    rich_obj_info = {
        "doc": doc_info["2d.wave~"],
        "args": {
            "required": [{"name": "freq", "type": ["number", "int"]}],
            "optional": [{"name": "label", "type": "symbol"}],
        },
        "attribs": [{"name": "COMMON"}, {"name": "gain"}],
    }
    fake_module = tmp_path / "generated_pkg" / "importobjs.py"
    fake_module.parent.mkdir(parents=True)
    fake_module.write_text("# stub target", encoding="utf-8")
    monkeypatch.setattr(importobjs, "__file__", str(fake_module))
    assert "2d.wave~ - Signal digest" in rich_obj_info["doc"]["digest"]

    info_root = tmp_path / "info"
    demo_info = info_root / "demo"
    empty_info = info_root / "empty"
    demo_info.mkdir(parents=True)
    empty_info.mkdir(parents=True)
    (demo_info / "2d.wave~.json").write_text(
        json.dumps(rich_obj_info, indent=2),
        encoding="utf-8",
    )
    (demo_info / "in.json").write_text(
        json.dumps({"doc": {"methods": [{"name": "noop"}]}, "args": {}, "attribs": []}),
        encoding="utf-8",
    )

    importobjs.generate_stubs({}, {"demo": str(demo_info), "empty": str(empty_info)})

    objects_dir = fake_module.parent / "objects"
    stub_text = (objects_dir / "demo.py").read_text(encoding="utf-8")
    init_text = (objects_dir / "__init__.py").read_text(encoding="utf-8")
    output = capsys.readouterr().out

    assert "stub module generated: objects/demo.py (2 objects)" in output
    assert "stub generation complete" in output
    assert "__all__ = [" in stub_text
    assert "'_2d_wave_tilde'" in stub_text
    assert "'in_'" in stub_text
    assert "2d.wave~ - Signal digest" in stub_text
    assert "MaxObject('2d.wave~')" in stub_text
    assert "MaxObject('in')" in stub_text
    assert "3.14" not in stub_text
    assert "# ruff: noqa: F403" in init_text
    assert 'warnings.simplefilter("ignore", UnknownObjectWarning)' in init_text
    assert "from .demo import *" in init_text


def test_importobjs_doc_and_stub_helpers(
    monkeypatch: MonkeyPatch, tmp_path: Path, capsys: CaptureFixture[str]
) -> None:
    """Verify generated module stubs and exports include object metadata."""
    info_root = tmp_path / "info"
    demo_info = info_root / "demo"
    empty_info = info_root / "empty"
    demo_info.mkdir(parents=True)
    empty_info.mkdir(parents=True)

    fake_module = tmp_path / "generated_pkg" / "importobjs.py"
    fake_module.parent.mkdir(parents=True)
    fake_module.write_text("# stub target", encoding="utf-8")
    monkeypatch.setattr(importobjs, "__file__", str(fake_module))

    plain_obj_info = {
        "doc": {},
        "args": {"required": [], "optional": []},
        "attribs": [],
    }
    (demo_info / "2d.wave~.json").write_text(
        json.dumps(
            {
                "doc": {
                    "digest": "Signal",
                    "description": "Generated object",
                    "methods": [{"name": "bang"}],
                    "inlets": [],
                    "outlets": [],
                },
                "args": {
                    "required": [{"name": "freq", "type": ["number"]}],
                    "optional": [],
                },
                "attribs": [{"name": "COMMON"}],
            },
            indent=2,
        ),
        encoding="utf-8",
    )
    (demo_info / "plain.json").write_text(
        json.dumps(plain_obj_info, indent=2),
        encoding="utf-8",
    )
    (demo_info / "in.json").write_text(
        json.dumps({"doc": {"methods": [{"name": "noop"}]}, "args": {}, "attribs": []}),
        encoding="utf-8",
    )

    importobjs.generate_stubs({}, {"demo": str(demo_info), "empty": str(empty_info)})

    objects_dir = fake_module.parent / "objects"
    stub_text = (objects_dir / "demo.py").read_text(encoding="utf-8")
    init_text = (objects_dir / "__init__.py").read_text(encoding="utf-8")
    output = capsys.readouterr().out

    assert "stub module generated: objects/demo.py (3 objects)" in output
    assert "stub generation complete" in output
    assert "'_2d_wave_tilde'" in stub_text
    assert "'in_'" in stub_text
    assert "'plain'" in stub_text
    assert "2d.wave~ - Signal" in stub_text
    assert "MaxObject('2d.wave~')" in stub_text
    assert "MaxObject('in')" in stub_text
    assert "MaxObject('plain')" in stub_text
    assert "# ruff: noqa: F403" in init_text
    assert 'warnings.simplefilter("ignore", UnknownObjectWarning)' in init_text
    assert "from .demo import *" in init_text
