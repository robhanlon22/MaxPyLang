"""Helpers for checking MaxPyLang argument datatypes."""

from collections.abc import Sequence
from typing import Callable, cast


def check_number(arg: object) -> bool:
    """Return whether ``arg`` can be interpreted as a number."""
    try:
        float(cast("str | int | float", arg))
    except (TypeError, ValueError):
        return False
    else:
        return True


def check_any(arg: object) -> bool:
    """Return ``True`` for any argument."""
    del arg
    return True


def check_int(arg: object) -> bool:
    """Return whether ``arg`` can be interpreted as an integer."""
    try:
        int(cast("str | bytes | bytearray | int | float", arg))
    except (TypeError, ValueError):
        return False
    else:
        return True


# functions associated with types, for typechecking
typecheck_funcs: dict[str, Callable[[object], bool]] = {
    "int": check_number,  # attrib
    "symbol": check_any,  # attrib
    "number": check_number,
    "list": check_any,
    "any": check_any,
    "float": check_number,  # attrib
    "atom_long": check_number,  # attrib
    "atom": check_any,  # attrib
    "int32": check_number,  # attrib
    "object": check_any,  # attrib
    "atomarray": check_any,  # attrib
}


def check_type(types: Sequence[str], arg: object) -> bool:
    """Return whether ``arg`` matches any of the named Max types."""
    return any(typecheck_funcs[t](arg) for t in types)
