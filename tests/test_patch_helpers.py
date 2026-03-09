import json
from types import SimpleNamespace

import pytest

from maxpylang.tools.objfuncs import specialobjs
from maxpylang.tools.patchfuncs import checking, misc, saving
from maxpylang.xlet import Inlet, Outlet


class DummyObj:
    def __init__(self, name, ref_file=None, ext_file=None):
        self.name = name
        self._name = name
        self._ref_file = ref_file
        self._ext_file = ext_file

    def __repr__(self):
        return f"<{self.name}>"


class DummyPatch:
    def __init__(self, objs):
        self._objs = objs

    def get_unknowns(self):
        return checking.get_unknowns(self)

    def get_abstractions(self):
        return checking.get_abstractions(self)

    def get_js_objs(self):
        return checking.get_js_objs(self)


class DummySpecialObject:
    unknown_obj_dict = {
        "box": {
            "id": "obj-1",
            "maxclass": "newobj",
            "patching_rect": [1.0, 2.0, 3.0, 4.0],
            "text": "UNK",
        }
    }

    def __init__(self, name="js", args=None, filename="", text="dummy"):
        self.name = name
        self._name = name
        self._args = list(args or [])
        self._ext_file = None
        self._dict = {
            "box": {
                "saved_object_attributes": {"filename": filename},
                "numinlets": 2,
                "numoutlets": 3,
                "save": ["prefix", ";"],
                "text": text,
            }
        }
        self.edit_calls = []
        self.update_abstraction_calls = []
        self.added_attribs = None
        self.made_xlets = False
        self.updated_text = False
        self._ref_file = None

    def edit(self, **kwargs):
        self.edit_calls.append(kwargs)

    def update_text(self):
        self.updated_text = True

    def get_js_io(self, filename, log_var=None):
        return specialobjs.get_js_io(self, filename, log_var=log_var)

    def get_js_filename(self):
        return specialobjs.get_js_filename(self)

    def update_js_from_file(self, filename, log_var=None):
        return specialobjs.update_js_from_file(self, filename, log_var=log_var)

    def update_abstraction_from_file(self, text, extra_attribs, log_var=None):
        self.update_abstraction_calls.append((text, extra_attribs, log_var))

    def make_xlets_from_self_dict(self):
        self.made_xlets = True

    def get_all_valid_attribs(self, text_attribs, extra_attribs, attrib_info):
        return text_attribs, {"sanitized": extra_attribs, "attrib_info": attrib_info}

    def add_extra_attribs(self, extra_attribs):
        self.added_attribs = extra_attribs

    def get_abstraction_io(self):
        return specialobjs.get_abstraction_io(self)

    def get_text(self):
        return self._dict["box"]["text"]

    def get_extra_attribs(self):
        return {"volume": 11}


def test_get_unknowns_get_abstractions_and_get_js_objs_partition_objects():
    objs = {
        "obj-1": DummyObj("mystery", ref_file=None),
        "obj-2": DummyObj("linked-js", ref_file="js", ext_file="/tmp/file.js"),
        "obj-3": DummyObj("js", ref_file="js", ext_file=None),
        "obj-4": DummyObj(
            "subpatch", ref_file="abstraction", ext_file="/tmp/thing.maxpat"
        ),
    }
    patch = DummyPatch(objs)

    assert checking.get_unknowns(patch) == {"obj-1": objs["obj-1"]}
    assert checking.get_abstractions(patch) == {"obj-4": objs["obj-4"]}
    assert checking.get_js_objs(patch) == (
        {},
        {"obj-3": objs["obj-3"]},
    )


def test_check_reports_all_sections_and_empty_sections(capsys):
    linked_js = DummyObj("js", ref_file="js", ext_file="/tmp/linked.js")
    unlinked_js = DummyObj("js", ref_file="js", ext_file=None)
    abstraction = DummyObj("abs", ref_file="abstraction", ext_file="/tmp/demo.maxpat")
    unknown = DummyObj("mystery", ref_file=None)
    patch = DummyPatch(
        {
            "obj-1": unknown,
            "obj-2": linked_js,
            "obj-3": unlinked_js,
            "obj-4": abstraction,
        }
    )

    checking.check(patch)
    output = capsys.readouterr().out
    assert "PatchCheck: unknown objects :" in output
    assert "PatchCheck: unlinked js objects :" in output
    assert "PatchCheck: linked js objects" in output
    assert "PatchCheck: linked abstractions" in output
    assert "linked.js" in output
    assert "demo.maxpat" in output

    empty_patch = DummyPatch({})
    checking.check(empty_patch, "unknowns", "js", "abstraction")
    empty_output = capsys.readouterr().out
    assert "no unknown objects" in empty_output
    assert "no unlinked js objects" in empty_output
    assert "no linked js objects" in empty_output
    assert "no linked abstractions" in empty_output


def test_add_barebones_obj_appends_box():
    patch = SimpleNamespace(_patcher_dict={"patcher": {"boxes": []}})

    misc.add_barebones_obj(patch, "cycle~ 440")

    assert patch._patcher_dict["patcher"]["boxes"] == [
        {
            "box": {
                "maxclass": "newobj",
                "text": "cycle~ 440",
                "patching_rect": [100.0, 100.0],
            }
        }
    ]


def test_get_json_includes_objects_and_patchcord_midpoints():
    source_parent = SimpleNamespace(_name="source")
    dest_parent = SimpleNamespace(_name="dest")
    outlet = Outlet(source_parent, 0, types=["signal"])
    inlet = Inlet(
        dest_parent, 1, sources=[outlet], midpoints=[[10.0, 20.0]], types=["signal"]
    )
    outlet._destinations.append(inlet)

    source_parent._dict = {"box": {"id": "obj-1", "text": "source"}}
    source_parent.outs = [outlet]
    dest_parent._dict = {"box": {"id": "obj-2", "text": "dest"}}
    dest_parent.outs = []

    patch = SimpleNamespace(
        _patcher_dict={"patcher": {"boxes": [], "lines": [], "metadata": "kept"}},
        _objs={"obj-1": source_parent, "obj-2": dest_parent},
    )

    result = saving.get_json(patch)

    assert result["patcher"]["metadata"] == "kept"
    assert result["patcher"]["boxes"] == [source_parent._dict, dest_parent._dict]
    assert result["patcher"]["lines"] == [
        {
            "patchline": {
                "destination": ["obj-2", 1],
                "source": ["obj-1", 0],
                "midpoints": [10.0, 20.0],
            }
        }
    ]
    assert patch._patcher_dict["patcher"]["boxes"] == []
    assert patch._patcher_dict["patcher"]["lines"] == []


def test_save_writes_maxpat_runs_check_and_prints(tmp_path, capsys):
    calls = []
    patch = SimpleNamespace(
        _filename="old.maxpat",
        get_json=lambda: {"patcher": {"boxes": [], "lines": []}},
        check=lambda *flags: calls.append(flags),
    )

    saving.save(patch, filename=str(tmp_path / "demo"), verbose=True, check=True)

    saved_path = tmp_path / "demo.maxpat"
    assert saved_path.exists()
    assert json.loads(saved_path.read_text()) == {"patcher": {"boxes": [], "lines": []}}
    assert patch._filename == str(saved_path)
    assert calls == [("unknown", "js", "abstractions")]
    assert "maxpatch saved to" in capsys.readouterr().out


def test_save_can_skip_check_and_keep_existing_suffix(tmp_path, capsys):
    patch = SimpleNamespace(
        _filename="before.maxpat",
        get_json=lambda: {"ok": True},
        check=lambda *flags: pytest.fail("check should not run"),
    )

    saving.save(
        patch, filename=str(tmp_path / "named.maxpat"), verbose=False, check=False
    )

    saved_path = tmp_path / "named.maxpat"
    assert saved_path.exists()
    assert patch._filename == str(saved_path)
    assert capsys.readouterr().out == ""


def test_get_js_filename_uses_first_non_numeric_arg_and_appends_js():
    obj = DummySpecialObject(args=["2", "3", "script"])
    assert specialobjs.get_js_filename(obj) == "script.js"


def test_get_js_filename_returns_none_when_no_filename_arg():
    obj = DummySpecialObject(args=["2", "3"])
    assert specialobjs.get_js_filename(obj) is None


def test_get_js_io_parses_counts_and_falls_back_to_defaults(tmp_path, capsys):
    js_file = tmp_path / "counts.js"
    js_file.write_text("inlets = 4; // comment\noutlets = 2;\n")
    fallback_file = tmp_path / "fallback.js"
    fallback_file.write_text("console.log('no io markers');\n")
    obj = DummySpecialObject()

    assert specialobjs.get_js_io(obj, str(js_file), log_var="scan") == ("4", "2")
    assert specialobjs.get_js_io(obj, str(fallback_file), log_var="scan") == (1, 1)
    output = capsys.readouterr().out
    assert "defaults assumed (1 inlet, 1 outlet)" in output


def test_update_js_from_file_updates_args_calls_edit_and_logs(tmp_path, capsys):
    js_file = tmp_path / "counts.js"
    js_file.write_text("inlets = 5;\noutlets = 7;\n")
    obj = DummySpecialObject()

    specialobjs.update_js_from_file(obj, str(js_file), log_var="creation")

    assert obj._args == ["7", "5", str(js_file)]
    assert obj.edit_calls == [{"text": f"7 5 {js_file}", "text_add": "replace"}]
    assert "7 outlets" in capsys.readouterr().out


def test_create_js_handles_missing_filename_and_missing_file(capsys):
    no_name = DummySpecialObject(args=["1", "2"])
    specialobjs.create_js(no_name, from_dict=False)
    missing = DummySpecialObject(args=["1", "2", "missing"])
    specialobjs.create_js(missing, from_dict=False)

    output = capsys.readouterr().out
    assert "no filename specified" in output
    assert "missing.js not found" in output
    assert missing._ext_file is None


def test_create_js_from_file_and_from_dict_updates_state(tmp_path, monkeypatch, capsys):
    js_file = tmp_path / "script.js"
    js_file.write_text("inlets = 1;\noutlets = 2;\n")
    monkeypatch.chdir(tmp_path)

    created = DummySpecialObject(args=["1", "2", "script"])
    specialobjs.create_js(created, from_dict=False)
    assert created._dict["box"]["saved_object_attributes"]["filename"] == "script.js"
    assert created._ext_file == str(js_file.resolve())
    assert created._args == ["2", "1", "script.js"]

    from_dict_obj = DummySpecialObject(filename="script.js")
    specialobjs.create_js(from_dict_obj, from_dict=True)
    assert from_dict_obj._args == [2, 3, "script.js"]
    assert from_dict_obj.updated_text is True
    assert "found, parsing for inlet/outlet numbers" in capsys.readouterr().out


def test_link_js_covers_empty_filename_existing_file_and_missing_file(
    tmp_path, monkeypatch, capsys
):
    js_file = tmp_path / "linked.js"
    js_file.write_text("inlets = 8;\noutlets = 9;\n")
    monkeypatch.chdir(tmp_path)

    no_filename = DummySpecialObject(filename="")
    specialobjs.link_js(no_filename)
    assert "no filename specified" in capsys.readouterr().out

    linked = DummySpecialObject()
    specialobjs.link_js(linked, "linked.js")
    assert linked._ext_file == str(js_file.resolve())
    assert linked._args == ["9", "8", "linked.js"]

    missing = DummySpecialObject()
    specialobjs.link_js(missing, "absent.js")
    assert "absent.js not found" in capsys.readouterr().out


def test_create_abstraction_variants_update_expected_helpers(capsys):
    from_dict_obj = DummySpecialObject(name="subpatch")
    specialobjs.create_abstraction(from_dict_obj, from_dict=True)
    assert from_dict_obj._ext_file == "subpatch.maxpat"
    assert from_dict_obj.made_xlets is True
    assert "abstraction created" in capsys.readouterr().out

    created = DummySpecialObject(name="explicit.maxpat")
    specialobjs.create_abstraction(
        created, text="explicit @gain 2", extra_attribs={"gain": 2}, from_dict=False
    )
    assert created._ext_file == "explicit.maxpat"
    assert created.update_abstraction_calls == [
        ("explicit @gain 2", {"gain": 2}, "creation")
    ]


def test_update_abstraction_from_file_builds_dict_and_logs(capsys):
    obj = DummySpecialObject(name="subpatch")
    obj.get_abstraction_io = lambda: (2, 1)

    specialobjs.update_abstraction_from_file(
        obj, "subpatch @gain 2", {"gain": 2}, log_var="link"
    )

    assert obj._dict["box"]["numinlets"] == 2
    assert obj._dict["box"]["numoutlets"] == 1
    assert obj._dict["box"]["outlettype"] == [""]
    assert obj._dict["box"]["patching_rect"] == [0.0, 0.0]
    assert obj._dict["box"]["text"] == "subpatch @gain 2"
    assert obj.added_attribs == {
        "sanitized": {"gain": 2},
        "attrib_info": [{"name": "COMMON"}],
    }
    assert obj.made_xlets is True
    assert "file found, abstraction created" in capsys.readouterr().out


def test_get_abstraction_io_counts_inlets_and_outlets(tmp_path):
    abstraction_file = tmp_path / "demo.maxpat"
    abstraction_file.write_text(
        json.dumps(
            {
                "patcher": {
                    "boxes": [
                        {"box": {"maxclass": "inlet"}},
                        {"box": {"maxclass": "inlet"}},
                        {"box": {"maxclass": "comment"}},
                        {"box": {"maxclass": "outlet"}},
                    ]
                }
            }
        )
    )
    obj = DummySpecialObject(name="demo")
    obj._ext_file = str(abstraction_file)

    assert specialobjs.get_abstraction_io(obj) == (2, 1)


def test_link_abstraction_updates_state_or_reports_missing(
    tmp_path, monkeypatch, capsys
):
    abstraction_file = tmp_path / "linked.maxpat"
    abstraction_file.write_text(json.dumps({"patcher": {"boxes": []}}))
    monkeypatch.chdir(tmp_path)

    linked = DummySpecialObject(name="linked")
    specialobjs.link_abstraction(linked)
    assert linked._ref_file == "abstraction"
    assert linked._ext_file == "linked.maxpat"
    assert linked._name == "linked"
    assert linked.update_abstraction_calls == [("dummy", {"volume": 11}, "link")]

    missing = DummySpecialObject(name="missing")
    specialobjs.link_abstraction(missing, "missing")
    assert "missing.maxpat not found" in capsys.readouterr().out


@pytest.mark.parametrize(
    ("args", "expected"),
    [
        (["b", "i", "3.5", "s", "custom"], ["bang", "int", "float", "", "custom"]),
        (["7", "f", "x"], ["int", "float", ""]),
    ],
)
def test_trigger_and_unpack_type_helpers(args, expected):
    obj = DummySpecialObject(args=args)
    if args[0] == "b":
        assert specialobjs.get_trigger_out_types(obj) == expected
    else:
        assert specialobjs.get_unpack_out_types(obj) == expected


def test_update_vst_rewrites_save_list():
    obj = DummySpecialObject(args=["plug", "preset"])

    specialobjs.update_vst(obj)

    assert obj._dict["box"]["save"] == ["prefix", "plug", "preset", ";"]
