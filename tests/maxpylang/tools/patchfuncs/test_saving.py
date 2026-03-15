"""Tests for save and serialization helpers."""

from pathlib import Path

from _pytest.capture import CaptureFixture

from maxpylang import MaxPatch


def test_get_json_captures_boxes_and_patchcords() -> None:
    """Verify get_json includes all boxes and lines."""
    patch = MaxPatch(verbose=False)
    source = patch.place("toggle", verbose=False)[0]
    destination = patch.place("number", verbose=False)[0]
    patch.connect([source.outs[0], destination.ins[0]], verbose=False)

    patch_json = patch.get_json()

    assert {box["box"]["id"] for box in patch_json["patcher"]["boxes"]} == {
        "obj-1",
        "obj-2",
    }
    assert len(patch_json["patcher"]["lines"]) == 1
    assert patch_json["patcher"]["lines"][0]["patchline"] == {
        "destination": ["obj-2", 0],
        "source": ["obj-1", 0],
        "midpoints": [None],
    }


def test_save_writes_file_and_runs_check_when_verbose(
    tmp_path: Path, capsys: CaptureFixture[str]
) -> None:
    """Verify save writes file and runs patch check when verbose."""
    patch = MaxPatch(verbose=False)
    patch.place("definitely_unknown", verbose=False)
    save_path = tmp_path / "generated"

    patch.save(str(save_path), verbose=True, check=True)
    assert (tmp_path / "generated.maxpat").exists()

    output = capsys.readouterr().out
    assert "PatchCheck: unknown objects :" in output
    assert "maxpatch saved to" in output


def test_save_skips_patch_check_when_disabled(tmp_path: Path) -> None:
    """Verify save can skip patch checking."""
    patch = MaxPatch(verbose=False)
    output_file = tmp_path / "noself.maxpat"
    patch.save(str(output_file), verbose=False, check=False)
    assert output_file.exists()
