"""Helpers for deleting patch objects and patchcords."""

from __future__ import annotations

import sys
from typing import TYPE_CHECKING

from maxpylang.xlet import Inlet, Outlet

if TYPE_CHECKING:
    from collections.abc import Sequence

    from maxpylang.maxpatch import MaxPatch

Connection = list[object]


def _assertion_error(message: str) -> AssertionError:
    """Build an `AssertionError` instance."""
    return AssertionError(message)


def _write_stdout(*parts: object) -> None:
    """Write a space-joined line to stdout."""
    sys.stdout.write(" ".join(str(part) for part in parts) + "\n")


def delete(
    self: MaxPatch,
    objs: Sequence[str] | None = None,
    cords: Sequence[Connection] | None = None,
    *,
    verbose: bool = True,
) -> None:
    """Delete objects and/or patchcords from the patch."""
    obj_ids = list(objs or [])
    cord_list = list(cords or [])

    for obj_id in obj_ids:
        if isinstance(obj_id, str):
            continue
        message = "objects to delete must be given as strings 'obj-num'"
        raise _assertion_error(message)

    self.check_connection_format(cord_list)
    existing_cords = self.check_connection_exists(cord_list)
    self.delete_cords(*existing_cords, verbose=verbose)
    self.delete_objs(*obj_ids, verbose=verbose)


def delete_get_extra_cords(self: MaxPatch, *objs: str) -> list[Connection]:
    """Return patchcords attached to the objects being deleted."""
    cords: list[Connection] = []
    for obj_id in objs:
        if obj_id not in self._objs:
            continue
        obj = self._objs[obj_id]
        for outlet in obj.outs:
            cords.extend([outlet, destination] for destination in outlet.destinations)
        for inlet in obj.ins:
            cords.extend([source, inlet] for source in inlet.sources)

    self.check_connection_format(cords)
    return cords


def delete_cords(_self: MaxPatch, *cords: Connection, verbose: bool = True) -> None:
    """Delete patchcords from the patch."""
    for cord in cords:
        outlet = cord[0]
        inlet = cord[1]
        if not isinstance(outlet, Outlet) or not isinstance(inlet, Inlet):
            message = "cords must be specified as (Outlet, Inlet) pairs"
            raise _assertion_error(message)

        inlet.remove_source(outlet)
        outlet.remove_destination(inlet)

        if verbose:
            _write_stdout(
                "disconnected: (",
                outlet.parent.name,
                ": outlet",
                outlet.index,
                "-/->",
                inlet.parent.name,
                ": inlet",
                inlet.index,
                ")",
            )


def delete_objs(self: MaxPatch, *objs: str, verbose: bool = True) -> None:
    """Delete objects and any attached patchcords."""
    obj_ids = list(objs)
    for obj_id in obj_ids.copy():
        if obj_id in self.objs:
            continue
        _write_stdout("delete error:", obj_id, "not in patch")
        obj_ids.remove(obj_id)

    cords_to_delete = self.delete_get_extra_cords(*obj_ids)
    self.delete_cords(*cords_to_delete)

    for obj_id in obj_ids:
        obj_name = self._objs[obj_id].name
        del self._objs[obj_id]
        if verbose:
            _write_stdout("object deleted:", obj_id, obj_name)

    self._num_objs = len(self._objs)
