"""Tests for misc utilities."""

from maxpylang.tools import misc as tools_misc


def test_get_objs_collects_sorted_json_stems_by_package(tmp_path, monkeypatch):
    package_root = tmp_path / "OBJ_INFO"
    for package, names in {"jit": ["b", "a"], "max": ["solo"]}.items():
        package_dir = package_root / package
        package_dir.mkdir(parents=True)
        for name in names:
            (package_dir / f"{name}.json").write_text("{}", encoding="utf-8")
        (package_dir / "ignore.txt").write_text("skip", encoding="utf-8")

    monkeypatch.setattr(tools_misc, "obj_info_folder", str(package_root))

    assert tools_misc.get_objs() == {"jit": ["a", "b"], "max": ["solo"]}
