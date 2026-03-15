from types import SimpleNamespace

from maxpylang import MaxPatch
from maxpylang.tools.patchfuncs import checking


def test_check_reports_sections_for_unknown_js_and_abstraction_flags(tmp_path, capsys):
    patch = MaxPatch(verbose=False)

    patch._objs = {
        "obj-1": SimpleNamespace(name="bad", _ref_file=None, _ext_file=None),
        "obj-2": SimpleNamespace(name="js", _ext_file="missing.js", _ref_file="js"),
        "obj-3": SimpleNamespace(
            name="js", _ext_file=str(tmp_path / "present.js"), _ref_file="js"
        ),
        "obj-4": SimpleNamespace(
            name="cycle~", _ref_file="abstraction", _ext_file="cycle.maxpat"
        ),
    }

    patch.check()
    output = capsys.readouterr().out
    assert "PatchCheck: unknown objects :" in output
    assert "PatchCheck: unlinked js objects :" in output
    assert (
        "PatchCheck: linked js objects (files must be in same folder as patch file):"
        in output
    )
    assert (
        "PatchCheck: linked abstractions (files must be in same folder as patch file):"
        in output
    )


def test_check_empty_sections_and_getters():
    patch = MaxPatch(verbose=False)
    patch._objs = {
        "obj-1": SimpleNamespace(
            name="toggle", _ref_file="abstraction", _ext_file="toggle.maxpat"
        ),
    }

    assert patch.check("unknowns", "js", "abstractions") is None
    assert checking.get_unknowns(patch) == {}
    assert checking.get_abstractions(patch) == {"obj-1": patch._objs["obj-1"]}
    assert checking.get_js_objs(patch) == ({}, {})


def test_check_all_includes_all_categories_and_handles_all_alias(tmp_path, capsys):
    patch = MaxPatch(verbose=False)
    patch._objs = {
        "obj-1": SimpleNamespace(name="bad", _ref_file=None, _ext_file=None),
        "obj-2": SimpleNamespace(name="js", _ref_file="js", _ext_file=None),
        "obj-3": SimpleNamespace(
            name="js", _ref_file="js", _ext_file=str(tmp_path / "linked.js")
        ),
        "obj-4": SimpleNamespace(
            name="cycle~", _ref_file="abstraction", _ext_file="cycle.maxpat"
        ),
    }

    assert patch.check("all") is None
    output = capsys.readouterr().out
    assert "PatchCheck: unknown objects :" in output
    assert "PatchCheck: unlinked js objects :" in output
    assert (
        "PatchCheck: linked js objects (files must be in same folder as patch file):"
        in output
    )
    assert (
        "PatchCheck: linked abstractions (files must be in same folder as patch file):"
        in output
    )
