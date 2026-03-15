"""Tests for constant helper persistence."""

import json
from pathlib import Path

from _pytest.monkeypatch import MonkeyPatch

from maxpylang.tools import constants

_DEFAULT_WAIT_TIME = 9


def test_constants_helpers_update_backing_json_file(
    tmp_path: Path,
    monkeypatch: MonkeyPatch,
) -> None:
    """Verify set/get helpers update live constants and persist to file."""
    constants_file = tmp_path / "constants.json"
    constants_file.write_text(
        json.dumps(
            {
                "packages_path": "/existing/packages",
                "max_refpath": "/existing/refpages",
                "wait_time": 1,
            }
        ),
        encoding="utf-8",
    )
    monkeypatch.setattr(constants, "constants_file", str(constants_file))

    packages_path = str(tmp_path / "packages")
    constants.set_packages_path(packages_path)
    constants.set_max_path("/Applications/Max.app")
    constants.set_wait_time(_DEFAULT_WAIT_TIME)
    constants.set_constant("custom", "value")

    assert constants.get_constant("packages_path") == packages_path
    assert (
        constants.get_constant("max_refpath")
        == "/Applications/Max.app/Contents/Resources/C74/docs/refpages/"
    )
    assert constants.get_constant("wait_time") == _DEFAULT_WAIT_TIME
    assert constants.get_constant("custom") == "value"

    persisted = json.loads(constants_file.read_text(encoding="utf-8"))
    assert persisted["packages_path"] == packages_path
    assert persisted["custom"] == "value"
