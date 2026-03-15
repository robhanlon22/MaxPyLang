"""Helpers for creating and inspecting patchcords."""

from __future__ import annotations

import logging
from typing import TYPE_CHECKING, Any, cast

from maxpylang.xlet import Inlet, Outlet

if TYPE_CHECKING:
    from maxpylang.maxobject import MaxObject
    from maxpylang.maxpatch import MaxPatch

Connection = list[Any]
_CONNECTION_WITH_MIDPOINTS = 3
_LOGGER = logging.getLogger(__name__)


def _assertion_error(message: str) -> AssertionError:
    """Build an `AssertionError` instance."""
    return AssertionError(message)


def connect(
    self: MaxPatch,
    *connections: Connection,
    verbose: bool = True,
) -> None:
    """Create patchcords between outlets and inlets."""
    del verbose
    self.check_connection_format(connections)
    valid_connections = self.check_connection_typing(connections)

    for connection in valid_connections:
        outlet = cast("Outlet", connection[0])
        inlet = cast("Inlet", connection[1])
        midpoints: list[float | None] | None = [None]
        if len(connection) == _CONNECTION_WITH_MIDPOINTS:
            midpoints = cast("list[float | None]", connection[2])

        inlet.add_source(outlet, midpoints)
        outlet.add_destination(inlet)
        _LOGGER.debug(
            "Patcher: connected: ( %s : outlet %s ---> %s : inlet %s )",
            outlet.parent.name,
            outlet.index,
            inlet.parent.name,
            inlet.index,
        )


def swap_patchcords(self: MaxPatch, new: MaxObject, old: MaxObject) -> None:
    """Swap retained patchcords from an old object to a replacement."""
    new_connections: list[Connection] = []
    old_connections: list[Connection] = []

    for old_inlet, new_inlet in zip(old.ins[: len(new.ins)], new.ins):
        for source in old_inlet.sources:
            midpoints = old_inlet.midpoint_for(source)
            old_connections.append([source, old_inlet, midpoints])
            new_connections.append([source, new_inlet, midpoints])

    for old_outlet, new_outlet in zip(old.outs[: len(new.outs)], new.outs):
        for destination in old_outlet.destinations:
            midpoints = destination.midpoint_for(old_outlet)
            old_connections.append([old_outlet, destination, midpoints])
            new_connections.append([new_outlet, destination, midpoints])

    self.delete_cords(*old_connections)
    self.connect(*new_connections)


def check_connection_format(
    self: MaxPatch,
    connections: tuple[Connection, ...] | list[Connection],
) -> None:
    """Validate connection formatting."""
    del self
    for connection in connections:
        is_valid_pair = isinstance(connection[0], Outlet) and isinstance(
            connection[1], Inlet
        )
        if not is_valid_pair:
            message = (
                "connections must be specified as "
                "(Outlet, Inlet, [optional: midpoints])"
            )
            raise _assertion_error(message)
        if len(connection) == _CONNECTION_WITH_MIDPOINTS and not isinstance(
            connection[2],
            list,
        ):
            message = "optional midpoints must be specified as list"
            raise _assertion_error(message)


def check_connection_typing(
    self: MaxPatch,
    connections: tuple[Connection, ...] | list[Connection],
) -> list[Connection]:
    """Return the currently accepted connections."""
    del self
    return list(connections)


def check_connection_exists(
    self: MaxPatch,
    connections: tuple[Connection, ...] | list[Connection],
) -> list[Connection]:
    """Filter the connection list to entries that currently exist."""
    del self
    existing_connections: list[Connection] = []
    for connection in connections:
        outlet = cast("Outlet", connection[0])
        inlet = cast("Inlet", connection[1])
        if inlet in outlet.destinations and outlet in inlet.sources:
            existing_connections.append(connection)
            continue
        _LOGGER.error(
            "PatchError: %s : outlet %s not connected to %s : inlet %s",
            outlet.parent.name,
            outlet.index,
            inlet.parent.name,
            inlet.index,
        )
    return existing_connections
