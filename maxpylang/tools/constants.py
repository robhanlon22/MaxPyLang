"""Constant paths and metadata used across MaxPyLang."""

import json
from pathlib import Path
from typing import Any

_MAXPY_PATH = Path(__file__).resolve().parent.parent
_DATA_PATH = _MAXPY_PATH / "data"
_CONSTANTS_PATH = _DATA_PATH / "constants.json"


maxpy_path = str(_MAXPY_PATH)
data_folder = str(_DATA_PATH)
import_tools = str(_DATA_PATH / "import_tools.json")
obj_info_folder = str(_DATA_PATH / "OBJ_INFO")
obj_io_folder = str(_DATA_PATH / "OBJ_IO")
patch_templates_path = str(_DATA_PATH / "PATCH_TEMPLATES")
constants_file = str(_CONSTANTS_PATH)


def _constants_path() -> Path:
    """Return the active constants file path."""
    return Path(constants_file)


# common box attributes available to all non-ui objects
common_box_attribs: list[dict[str, Any]] = [
    {"name": "annotation", "type": "symbol", "size": 1},
    {"name": "background", "type": "int", "size": 1},  # 0 or 1
    {"name": "color", "type": "float", "size": 4},
    {"name": "fontface", "type": "int", "size": 1},  # 0, 1, 2, 3
    {"name": "fontname", "type": "symbol", "size": 1},
    {"name": "fontsize", "type": "float", "size": 1},
    {"name": "hidden", "type": "int", "size": 1},  # 0 or 1
    {"name": "hint", "type": "symbol", "size": 1},
    {"name": "ignoreclick", "type": "int", "size": 1},  # 0 or 1
    {"name": "jspainterfile", "type": "symbol", "size": 1},
    {"name": "presentation", "type": "int", "size": 1},  # 0 or 1
    {"name": "presentation_rect", "type": "float", "size": 4},
    {"name": "textcolor", "type": "float", "size": 4},
    {"name": "textjustification", "type": "int", "size": 1},  # 0 , 1 , 2
    {"name": "varname", "type": "symbol", "size": 1},
    {"name": "style", "type": "symbol", "size": 1},
    {"name": "bgcolor", "type": "float", "size": 4},
]


unknown_obj_dict: dict[str, Any] = {
    "box": {
        "id": "obj-1",
        "maxclass": "newobj",
        "numinlets": 0,
        "numoutlets": 0,
        "patching_rect": [234.0, 81.0, 34.0, 22.0],
        "text": "UNK",
    }
}

# ***** FOR SETTING CONSTANTS ********


def set_packages_path(newpath: str) -> None:
    """Set the Packages folder path used for Max package information."""
    set_constant("packages_path", newpath)


def set_max_path(newpath: str) -> None:
    """Set the Max application path and derive its reference-pages directory."""
    refpath = str(
        Path(newpath) / "Contents" / "Resources" / "C74" / "docs" / "refpages"
    )
    refpath += "/"
    set_constant("max_refpath", refpath)


def set_wait_time(new_time: float) -> None:
    """Set the wait time used while importing Max packages."""
    set_constant("wait_time", new_time)


def set_constant(name: str, val: object) -> None:
    """Set a named constant in the backing JSON file."""
    constants_path = _constants_path()
    constants = json.loads(constants_path.read_text(encoding="utf-8"))
    constants[name] = val
    constants_path.write_text(json.dumps(constants, indent=2), encoding="utf-8")


# **** FOR GETTING CONSTANTS *****


def get_constant(name: str) -> object:
    """Return the requested constant from the backing JSON file."""
    constants = json.loads(_constants_path().read_text(encoding="utf-8"))
    return constants[name]
