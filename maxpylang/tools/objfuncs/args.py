"""Helpers for validating and coercing `MaxObject` text arguments."""

from __future__ import annotations

import warnings
from typing import TYPE_CHECKING, Union

import tabulate  # type: ignore[import-untyped]

from maxpylang.exceptions import UnknownObjectWarning
from maxpylang.tools import typechecks as tc
from maxpylang.tools.misc import write_stdout

if TYPE_CHECKING:
    from collections.abc import Sequence

    from maxpylang.maxobject import MaxObject

Atom = Union[str, int, float]
ArgSpec = dict[str, object]
ArgInfo = dict[str, list[ArgSpec]]


def args_valid(
    self: MaxObject,
    name: str,
    args: Sequence[Atom],
    arg_info: ArgInfo,
) -> bool:
    """Check text arguments against argument info."""
    args_req = arg_info["required"]
    args_opt = arg_info["optional"]

    if len(args_req) > len(args):
        req_table = tabulate.tabulate(
            [[x["name"], x["type"]] for x in args_req],
            ["req arg", "type"],
            tablefmt="pretty",
        )
        warnings.warn(
            f"'{name}': missing required arguments\n{req_table}",
            UnknownObjectWarning,
            stacklevel=4,
        )
        return False

    req_types = [arg["type"] for arg in args_req]
    if not all(
        tc.check_type(type_info, arg)
        for type_info, arg in zip(req_types, args[: len(args_req)])
    ):
        req_table = tabulate.tabulate(
            [[x["name"], x["type"]] for x in args_req],
            ["req arg", "type"],
            tablefmt="pretty",
        )
        warnings.warn(
            f"'{name}': bad type(s) for required arguments\n{req_table}",
            UnknownObjectWarning,
            stacklevel=4,
        )
        return False

    opt_types = [arg["type"] for arg in args_opt]
    if not all(
        tc.check_type(type_info, arg)
        for type_info, arg in zip(opt_types, args[len(args_req) :])
    ):
        req_table = tabulate.tabulate(
            [[x["name"], x["type"]] for x in args_req],
            ["req arg", "type"],
            tablefmt="pretty",
        )
        opt_table = tabulate.tabulate(
            [[x["name"], x["type"]] for x in args_opt],
            ["opt arg", "type"],
            tablefmt="pretty",
        )
        warnings.warn(
            f"'{name}': bad type(s) for optional arguments\n{req_table}\n{opt_table}",
            UnknownObjectWarning,
            stacklevel=4,
        )
        return False

    if self.arg_warning and args_req:
        write_stdout(
            "(arg_warning):",
            name,
            ": args may have special reqs, check official docs for details",
        )

    return True


def get_typed_args(_self: MaxObject, args: Sequence[str]) -> list[Atom]:
    """Convert string arguments into ints or floats when possible."""
    typed_args: list[Atom] = []
    for arg in args:
        if tc.check_int(arg):
            typed_args.append(int(arg))
        elif tc.check_number(arg):
            typed_args.append(float(arg))
        else:
            typed_args.append(arg)
    return typed_args
