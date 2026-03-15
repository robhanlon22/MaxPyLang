"""Utilities for importing Max object metadata and generating object stubs."""

from __future__ import annotations

import builtins
import collections
import importlib
import json
import keyword
import logging
import shutil
import textwrap
import time
import webbrowser
from pathlib import Path
from typing import TYPE_CHECKING, Any, Literal, Protocol, cast

from .maxpatch import MaxPatch
from .tools.constants import (
    get_constant,
    import_tools,
    obj_info_folder,
    obj_io_folder,
)

common_box_standin: list[dict[str, str]] = [{"name": "COMMON"}]
available_argtypes: list[str] = ["int", "symbol", "number", "list", "any", "float"]
known_aliases: dict[str, str] = {
    "t": "trigger",
    "sel": "select",
    "b": "bangbang",
}

if TYPE_CHECKING:
    from collections.abc import Iterable


class _ElementLike(Protocol):
    attrib: dict[str, str]

    def find(self, path: str) -> _ElementLike | None: ...

    def findall(self, path: str) -> list[_ElementLike]: ...

    def itertext(self) -> Iterable[str]: ...


class _ElementTreeLike(Protocol):
    def getroot(self) -> _ElementLike: ...


JSONValue = Any
JSONDict = dict[str, Any]
PackagePaths = dict[str, Path]
ArgSpec = dict[str, Any]
ArgSections = dict[str, list[ArgSpec]]
AttribList = list[dict[str, Any]]
ArgStatus = Literal["required", "optional"]
JSONFileData = Any

_DOC_WIDTH = 88
_json_width = 2
_LOGGER = logging.getLogger(__name__)
try:
    _xml_parser = importlib.import_module("defusedxml.ElementTree")
except ModuleNotFoundError:  # pragma: no cover
    _xml_parser = importlib.import_module("xml.etree.ElementTree")


def import_objs(*packages: str, overwrite: bool = False) -> None:
    """Import objects from MaxMSP packages."""
    Path(obj_info_folder).mkdir(parents=True, exist_ok=True)
    package_paths = get_package_paths(list(packages))
    package_info_folders = prep_make_info_folders(
        package_paths,
        overwrite=overwrite,
    )
    save_obj_info(package_paths, package_info_folders)
    generate_stubs(package_paths, package_info_folders)


def get_package_paths(packages: Iterable[str]) -> PackagePaths:
    """Build filesystem locations for Max package reference files."""
    vanilla_refpath = Path(cast("str", get_constant("max_refpath")))
    packages_refpath = Path(cast("str", get_constant("packages_path")))

    resolved_packages: list[str] = []
    for package in packages:
        if package == "vanilla":
            resolved_packages.extend(["max", "msp", "jit"])
        else:
            resolved_packages.append(package)

    package_paths: PackagePaths = {}
    for package in resolved_packages:
        if package in {"max", "msp", "jit"}:
            package_paths[package] = vanilla_refpath / f"{package}-ref"
        else:
            package_paths[package] = packages_refpath / package / "docs"

    return package_paths


def prep_make_info_folders(
    package_paths: PackagePaths,
    *,
    overwrite: bool = False,
) -> PackagePaths:
    """Prepare obj-info output folders for imported packages."""
    obj_info_root = Path(obj_info_folder)
    obj_info_root.mkdir(parents=True, exist_ok=True)

    package_info_folders: PackagePaths = {}
    for package, package_path_value in package_paths.items():
        package_path = Path(package_path_value)
        if not package_path.exists():
            _LOGGER.error("package %s not found", package)
            continue

        package_info_folder = obj_info_root / package
        if package_info_folder.exists():
            if not overwrite:
                _LOGGER.info("%s previously imported, skipping...", package)
                continue
            _LOGGER.info("prepping to re-import %s", package)
            shutil.rmtree(package_info_folder)
        else:
            _LOGGER.info("prepping to import %s", package)

        package_info_folder.mkdir()
        package_info_folders[package] = package_info_folder

    return package_info_folders


def save_obj_info(
    package_paths: PackagePaths,
    package_info_folders: PackagePaths,
) -> None:
    """Save per-object default, argument, attribute, and I/O metadata."""
    obj_aliases = dict(known_aliases)

    for package, info_folder_value in package_info_folders.items():
        _LOGGER.info("importing %s objects...", package)
        ref_folder = Path(package_paths[package])
        info_folder = Path(info_folder_value)
        obj_refs = sorted(ref_folder.glob("*.maxref.xml"))
        obj_refs = [ref for ref in obj_refs if not is_unlisted(ref)]
        obj_names = [_object_name_from_ref(ref) for ref in obj_refs]

        default_obj_info = get_default_obj_info(package, obj_refs, obj_names)
        obj_aliases.update(get_obj_aliases(default_obj_info, obj_names))
        objarg_info = get_objarg_info(obj_refs, obj_names)
        objattrib_info = get_objattrib_info(obj_refs, obj_names)
        objinout_info = get_objinout_info(package, obj_names)
        obj_doc_info = get_obj_doc_info(obj_refs, obj_names)

        for name in obj_names:
            obj_info = {
                "default": default_obj_info[name],
                "args": objarg_info[name],
                "attribs": objattrib_info[name],
                "in/out": objinout_info[name],
                "doc": obj_doc_info[name],
            }
            _write_json(info_folder / f"{name}.json", obj_info)
        _LOGGER.info("%s object info files saved", len(obj_names))

    _write_json(Path(obj_info_folder) / "obj_aliases.json", obj_aliases)
    _LOGGER.info("object aliases saved successfully")


def is_unlisted(ref: Path) -> bool:
    """Return ``True`` if an object is marked as unlisted."""
    root = _parse_xml(ref).getroot()
    return root.attrib.get("category") == "Unlisted"


def get_obj_aliases(
    default_info: dict[str, JSONDict], names: list[str]
) -> dict[str, str]:
    """Map default text labels back to their object names."""
    aliases: dict[str, str] = {}
    for name in names:
        default_text = default_info.get(name, {}).get("box", {}).get("text")
        if default_text and default_text != name:
            aliases[default_text] = name

    return aliases


def get_default_obj_info(
    package: str,
    refs: list[Path],
    names: list[str],
) -> dict[str, JSONDict]:
    """Place objects in a patch and extract saved default arguments."""
    wait_time = float(cast("str | int | float", get_constant("wait_time")))
    patch = MaxPatch(verbose=False)
    add_save_close(patch)
    add_barebones_objs(refs, patch)

    defaults_file = Path(f"defaults_{package}.maxpat")
    patch.save(filename=str(defaults_file), verbose=False)
    _open_defaults_file(defaults_file)
    time.sleep(wait_time)

    with defaults_file.open() as f:
        patchdict: JSONDict = json.load(f)

    patchboxes = patchdict["patcher"]["boxes"][6:]
    obj_info: dict[str, JSONDict] = dict(zip(names, patchboxes))

    if defaults_file.exists():
        defaults_file.unlink()

    return obj_info


def _open_defaults_file(defaults_file: Path) -> None:
    """Open the generated maxpat file for one-shot Max patch evaluation."""
    webbrowser.open(defaults_file.resolve().as_uri())


def add_barebones_objs(refs: list[Path], patch: MaxPatch) -> None:
    """Add a barebones instance of every object into patch for metadata export."""
    for ref in refs:
        root = _parse_xml(ref).getroot()
        patch.add_barebones_obj(root.attrib["name"])


def add_save_close(patch: MaxPatch) -> None:
    """Add template objects that save and close the patch."""
    tools = _read_json(Path(import_tools))
    patcher = patch.__dict__["_patcher_dict"]
    patcher["patcher"]["boxes"] = tools["boxes"]
    patcher["patcher"]["lines"] = tools["lines"]


def get_objarg_info(refs: list[Path], names: list[str]) -> dict[str, ArgSections]:
    """Gather required and optional object arguments."""
    objarg_info: dict[str, ArgSections] = collections.defaultdict(
        lambda: {"required": [], "optional": []}
    )

    for ref, name in zip(refs, names):
        root = _parse_xml(ref).getroot()
        objarg_info[name]["required"] = get_objargs_by_flag(root, "[@optional='0']")
        objarg_info[name]["optional"] = get_objargs_by_flag(root, "[@optional='1']")

    return objarg_info


def get_objargs_by_flag(root: _ElementLike, flag: str) -> list[ArgSpec]:
    """Extract object arguments from an XML element matching a flag."""
    findstring = "./objarglist/objarg" + flag
    args: list[ArgSpec] = []

    for objarg in root.findall(findstring):
        objarg_info: ArgSpec = dict(objarg.attrib)
        if not (
            objarg_info["name"] == "OBJARG_NAME"
            and objarg_info["type"] == "OBJARG_TYPE"
        ):
            if "type" not in objarg_info:
                objarg_info["type"] = []
            else:
                objarg_info["type"] = [
                    argtype
                    for argtype in available_argtypes
                    if argtype in objarg_info["type"]
                ]
            objarg_info.pop("optional", None)
            args.append(objarg_info)

    return args


def get_objattrib_info(refs: list[Path], names: list[str]) -> dict[str, AttribList]:
    """Extract object attribute metadata from XML."""
    objattrib_info: dict[str, AttribList] = collections.defaultdict(list)

    for ref, name in zip(refs, names):
        root = _parse_xml(ref).getroot()
        if root.attrib.get("category") != "U/I":
            objattrib_info[name] += common_box_standin

        for attrib in root.findall("./attributelist/attribute"):
            attrib_info = dict(attrib.attrib)
            attrib_info.pop("get", None)
            attrib_info.pop("set", None)
            objattrib_info[name].append(attrib_info)

    return objattrib_info


def get_objinout_info(package: str, names: list[str]) -> dict[str, JSONDict]:
    """Extract I/O relationship metadata for each object."""
    info_file = Path(obj_io_folder) / f"{package}_io.json"
    info: dict[str, JSONDict] = {}
    if info_file.exists():
        info = _read_json(info_file)

    return {name: info.get(name, {}) for name in names}


def strip_xml_text(element: _ElementLike | None) -> str:
    """Strip XML markup and return plain text for a node."""
    if element is None:
        return ""
    return "".join(element.itertext()).strip()


def get_obj_doc_info(refs: list[Path], names: list[str]) -> dict[str, JSONDict]:
    """Extract documentation metadata from XML reference files."""
    obj_doc_info: dict[str, JSONDict] = {}

    for ref, name in zip(refs, names):
        root = _parse_xml(ref).getroot()
        doc = _read_doc_fields(root)
        inlets = _read_xlet_metadata(root.findall("./inletlist/inlet"))
        if inlets:
            doc["inlets"] = inlets
        outlets = _read_xlet_metadata(root.findall("./outletlist/outlet"))
        if outlets:
            doc["outlets"] = outlets
        methods = root.findall("./methodlist/method")
        method_info = [_read_method_metadata(method) for method in methods]
        if method_info:
            doc["methods"] = method_info
        obj_doc_info[name] = doc

    return obj_doc_info


def _read_doc_fields(root: _ElementLike) -> JSONDict:
    """Read shared documentation sections from an XML object definition."""
    doc: JSONDict = {}
    _set_optional_text(doc, "digest", root.find("digest"))
    _set_optional_text(doc, "description", root.find("description"))
    return doc


def _read_xlet_metadata(nodes: list[_ElementLike]) -> list[JSONDict]:
    """Read inlet/outlet metadata nodes."""
    xlets: list[JSONDict] = []
    for node in nodes:
        xlet = dict(node.attrib)
        _set_optional_text(xlet, "digest", node.find("digest"))
        _set_optional_text(xlet, "description", node.find("description"))
        xlets.append(xlet)
    return xlets


def _read_method_metadata(method: _ElementLike) -> JSONDict:
    """Read method metadata and nested argument details."""
    method_info: JSONDict = dict(method.attrib)
    _set_optional_text(method_info, "digest", method.find("digest"))
    _set_optional_text(method_info, "description", method.find("description"))

    arglist = method.find("arglist")
    if arglist is not None:
        args = [dict(arg.attrib) for arg in arglist.findall("arg")]
        if args:
            method_info["args"] = args

    return method_info


def _set_optional_text(target: JSONDict, key: str, node: _ElementLike | None) -> None:
    """Add an XML text value if it is non-empty and not a placeholder."""
    value = strip_xml_text(node) if node is not None else ""
    if value and value != "TEXT_HERE":
        target[key] = value


def sanitize_py_name(max_name: str) -> str:
    """Convert a Max object name to a valid Python identifier."""
    name = max_name.replace("~", "_tilde")
    name = name.replace(".", "_").replace("-", "_")
    if name and name[0].isdigit():
        name = "_" + name
    if keyword.iskeyword(name) or name in dir(builtins):
        name = name + "_"
    return name


def _build_docstring(max_name: str, obj_info: JSONDict) -> str:
    """Build a short wrapped docstring for a generated object constant."""
    doc = obj_info.get("doc", {})
    args = obj_info.get("args", {})
    attribs = obj_info.get("attribs", [])

    lines: list[str] = []
    name_with_digest = f"{max_name} - {doc.get('digest', '')}".rstrip(" -")
    lines.append(name_with_digest)
    _append_optional_text(lines, doc.get("description"))
    _append_args(lines, args)
    _append_inlets(lines, doc.get("inlets"))
    _append_outlets(lines, doc.get("outlets"))
    _append_methods(lines, doc.get("methods"))
    _append_attributes(lines, attribs)

    return "\n".join(_wrap_lines(lines))


def _append_optional_text(lines: list[str], value: str | None) -> None:
    """Append a wrapped description paragraph when present."""
    if not value:
        return
    lines.append("")
    lines.extend(_wrap_lines([value]))


def _append_args(lines: list[str], args: JSONValue) -> None:
    """Append formatted required and optional argument lines."""
    if not isinstance(args, dict):
        return

    required_args = args.get("required", [])
    optional_args = args.get("optional", [])
    if not isinstance(required_args, list):
        required_args = []
    if not isinstance(optional_args, list):
        optional_args = []
    if not required_args and not optional_args:
        return

    lines.append("")
    lines.append("Args:")
    lines.extend(_iter_arg_lines(required_args, "required"))
    lines.extend(_iter_arg_lines(optional_args, "optional"))


def _iter_arg_lines(args: list[ArgSpec], status: ArgStatus) -> Iterable[str]:
    """Yield wrapped argument lines in required/optional format."""
    for arg in args:
        arg_type_value = arg.get("type", [])
        if isinstance(arg_type_value, list):
            arg_type = ", ".join(arg_type_value)
        else:
            arg_type = arg_type_value
        yield f"{arg.get('name', '?')} ({arg_type}, {status})"


def _append_inlets(lines: list[str], inlets: list[JSONDict] | None) -> None:
    """Append inlet metadata lines."""
    if not inlets:
        return
    lines.append("")
    lines.append("Inlets:")
    for idx, inlet in enumerate(inlets):
        line = _io_line(idx, inlet)
        lines.extend(_wrap_lines([line], prefix="  "))


def _append_outlets(lines: list[str], outlets: list[JSONDict] | None) -> None:
    """Append outlet metadata lines."""
    if not outlets:
        return
    lines.append("")
    lines.append("Outlets:")
    for idx, outlet in enumerate(outlets):
        line = _io_line(idx, outlet)
        lines.extend(_wrap_lines([line], prefix="  "))


def _append_methods(lines: list[str], methods: list[JSONDict] | None) -> None:
    """Append messages section."""
    if not methods:
        return
    method_names = [method.get("name", "") for method in methods if method.get("name")]
    if not method_names:
        return
    lines.append("")
    lines.append("Messages:")
    lines.extend(_wrap_lines([", ".join(method_names)], prefix="  "))


def _append_attributes(lines: list[str], attribs: list[dict[str, Any]]) -> None:
    """Append attributes section."""
    attrib_names = [
        attrib.get("name", "")
        for attrib in attribs
        if attrib.get("name") and attrib.get("name") != "COMMON"
    ]
    if not attrib_names:
        return
    lines.append("")
    lines.append("Attributes:")
    lines.extend(_wrap_lines([", ".join(attrib_names)], prefix="  "))


def _io_line(index: int, metadata: JSONDict) -> str:
    """Format an inlet or outlet metadata row."""
    idx = metadata.get("id", str(index))
    io_type = metadata.get("type", "")
    digest = metadata.get("digest", "")
    if io_type and digest:
        return f"{idx} ({io_type}): {digest}"
    if io_type:
        return f"{idx} ({io_type})"
    if digest:
        return f"{idx}: {digest}"
    return str(idx)


def _wrap_lines(lines: list[str], prefix: str = "") -> list[str]:
    """Wrap non-empty text to the configured line width."""
    wrapped: list[str] = []
    for original_line in lines:
        line = " ".join(str(original_line).split())
        if not line:
            wrapped.append("")
            continue
        available_width = _DOC_WIDTH - 4 - len(prefix)
        if len(line) <= available_width:
            wrapped.append(f"{prefix}{line}")
            continue
        wrapped.extend(
            f"{prefix}{wrapped_line}"
            for wrapped_line in textwrap.wrap(
                line,
                width=available_width,
                break_long_words=False,
                break_on_hyphens=False,
            )
        )
    return wrapped


def generate_stubs(
    _package_paths: PackagePaths,
    package_info_folders: PackagePaths,
) -> None:
    """Write generated object stub modules for each imported package."""
    objects_dir = Path(__file__).resolve().parent / "objects"
    objects_dir.mkdir(parents=True, exist_ok=True)

    for package, info_folder_value in package_info_folders.items():
        info_folder = Path(info_folder_value)
        json_files = [
            path
            for path in sorted(info_folder.glob("*.json"))
            if path.name != "obj_aliases.json"
        ]
        if not json_files:
            continue

        names_map: dict[str, str] = {}
        obj_infos: dict[str, JSONDict] = {}

        for json_file in json_files:
            max_name = _object_name_from_ref(json_file)
            obj_info = _read_json(json_file)
            py_name = sanitize_py_name(max_name)
            names_map[py_name] = max_name
            obj_infos[max_name] = obj_info

        stub_lines = _build_stub_lines(names_map, obj_infos)
        stub_path = objects_dir / f"{package}.py"
        stub_path.write_text("\n".join(stub_lines) + "\n")
        _LOGGER.info(
            "stub module generated: objects/%s.py (%s objects)",
            package,
            len(names_map),
        )

    init_lines = _build_objects_init_lines(objects_dir)
    (objects_dir / "__init__.py").write_text("\n".join(init_lines) + "\n")
    _LOGGER.info("stub generation complete")


def _build_stub_lines(
    names_map: dict[str, str],
    obj_infos: dict[str, JSONDict],
) -> list[str]:
    """Compose the Python source for a single package stub module."""
    all_names = sorted(names_map)
    lines = [
        '"""Generated MaxObject stubs."""',
        "",
        "from contextlib import redirect_stdout",
        "from io import StringIO",
        "from maxpylang.maxobject import MaxObject",
        "",
        "__all__ = [",
    ]
    lines.extend(f"    {name!r}," for name in all_names)
    lines.append("]")
    lines.append("")
    lines.append("_NAMES = {")
    lines.extend(
        f"    {py_name!r}: {max_name!r},"
        for py_name in all_names
        for max_name in [names_map[py_name]]
    )
    lines.append("}")
    lines.append("")
    lines.append("_output = StringIO()")
    lines.append("with redirect_stdout(_output):")

    for py_name in all_names:
        max_name = names_map[py_name]
        obj_info = obj_infos[max_name]
        docstring = _build_docstring(max_name, obj_info).replace('"""', '\\"""')
        lines.append(f"    {py_name} = MaxObject({max_name!r})")
        lines.append(f'    {py_name}.__doc__ = """')
        for doc_line in docstring.splitlines():
            if doc_line:
                lines.append(f"    {doc_line}")
            else:
                lines.append("")
        lines.append('    """')
        lines.append("")
    lines.append("")
    lines.append("del _output")
    return lines


def _build_objects_init_lines(objects_dir: Path) -> list[str]:
    """Compose the package init file to import all generated stubs."""
    existing_stubs = [path.stem for path in sorted(objects_dir.glob("*.py"))]
    init_lines = [
        '"""Pre-instantiated MaxObject stubs for all imported packages."""',
        "# ruff: noqa: F403",
        "import warnings",
        "import contextlib",
        "from maxpylang.exceptions import UnknownObjectWarning",
        "",
        "# Suppress warnings while loading stubs.",
        "with warnings.catch_warnings():",
        '    warnings.simplefilter("ignore", UnknownObjectWarning)',
    ]
    for stem in sorted(existing_stubs):
        if stem == "__init__":
            continue
        init_lines.extend(
            [
                "    with contextlib.suppress(ImportError):",
                f"        from .{stem} import *",
            ]
        )

    return init_lines


def _object_name_from_ref(ref: Path) -> str:
    """Convert a Max reference filename to the object's canonical name."""
    stem = ref.stem
    return stem.removesuffix(".maxref")


def _read_json(path: Path) -> JSONDict:
    """Read a JSON file into a dictionary."""
    with path.open(encoding="utf-8") as f:
        return cast("JSONDict", json.load(f))


def _write_json(path: Path, data: JSONFileData) -> None:
    """Write JSON data to disk with consistent indentation."""
    with path.open("w", encoding="utf-8") as f:
        json.dump(data, f, indent=_json_width)


def _parse_xml(path: str | Path) -> _ElementTreeLike:
    """Parse an XML file with the configured parser."""
    return cast("_ElementTreeLike", _xml_parser.parse(Path(path).as_posix()))
