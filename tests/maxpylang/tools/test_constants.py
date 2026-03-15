"""Tests for constant helpers."""

import json

from maxpylang.tools import constants


def test_constants_helpers_update_backing_json_file(tmp_path, monkeypatch):
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

    constants.set_packages_path("/tmp/packages")
    constants.set_max_path("/Applications/Max.app")
    constants.set_wait_time(9)
    constants.set_constant("custom", "value")

    assert constants.get_constant("packages_path") == "/tmp/packages"
    assert (
        constants.get_constant("max_refpath")
        == "/Applications/Max.app/Contents/Resources/C74/docs/refpages/"
    )
    assert constants.get_constant("wait_time") == 9
    assert constants.get_constant("custom") == "value"

    persisted = json.loads(constants_file.read_text(encoding="utf-8"))
    assert persisted["packages_path"] == "/tmp/packages"
    assert persisted["custom"] == "value"
