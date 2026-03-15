"""Classes for inlets and outlets attached to Max objects."""

from __future__ import annotations

from typing import TYPE_CHECKING, Optional, Union

if TYPE_CHECKING:
    from .maxobject import MaxObject

Midpoint = Optional[list[Optional[float]]]
XletTypes = Union[list[str], str, None]


def _parent_name(parent: object) -> str:
    """Resolve a readable parent name for repr output."""
    name = getattr(parent, "name", None)
    if isinstance(name, str):
        return name
    private_name = getattr(parent, "_name", None)
    if isinstance(private_name, str):
        return private_name
    namespace = getattr(parent, "__dict__", None)
    if isinstance(namespace, dict):
        dict_name = namespace.get("_name")
        if isinstance(dict_name, str):
            return dict_name
        nested_namespace = namespace.get("__dict__")
        if isinstance(nested_namespace, dict):
            nested_name = nested_namespace.get("_name")
            if isinstance(nested_name, str):
                return nested_name
    return str(parent)


class Inlet:
    """Represent an inlet and the patchcords routed into it."""

    def __init__(
        self,
        parent: MaxObject,
        index: int,
        sources: list[Outlet] | None = None,
        midpoints: list[Midpoint] | None = None,
        types: XletTypes = None,
    ) -> None:
        """Initialize an inlet for the given parent object."""
        self._parent = parent  # parent MaxObject
        self._sources = sources or []  # list of Outlets
        self._midpoints = (
            midpoints or []
        )  # list of midpoints (this info only in inlet of outlet, inlet pair)
        self._types: XletTypes = [] if types is None else types  # allowed types
        self._index = index  # index in parent object, starting from 0

    # some properties for getting info...
    @property
    def parent(self) -> MaxObject:
        """Return the parent object that owns this inlet."""
        return self._parent

    @property
    def sources(self) -> list[Outlet]:
        """Return source outlets connected to this inlet."""
        return self._sources

    @property
    def midpoints(self) -> list[Midpoint]:
        """Return stored midpoint coordinates for inlet patchcords."""
        return self._midpoints

    @property
    def types(self) -> XletTypes:
        """Return the accepted inlet connection types."""
        return self._types

    @property
    def index(self) -> int:
        """Return the inlet index within the parent object."""
        return self._index

    # for printing out...
    def __repr__(self) -> str:
        """Return a readable summary of the inlet and its sources."""
        # report parent, index, and types
        rep = (
            f"{_parent_name(self.parent)}: inlet {self.index}, "
            f"types taken: {self.types}"
        )

        # report sources and existing midpoints
        for source_index, source in enumerate(self._sources):
            rep += f"\n\tsource: {_parent_name(source.parent)}: outlet {source.index}"
            midpoint = (
                self._midpoints[source_index]
                if source_index < len(self._midpoints)
                else None
            )
            if midpoint is not None:
                rep += ", midpoints: " + str(midpoint)

        return rep

    def add_source(self, source: Outlet, midpoints: Midpoint) -> None:
        """Attach a source outlet and its midpoint data."""
        self._sources.append(source)
        self._midpoints.append(midpoints)

    def remove_source(self, source: Outlet) -> Midpoint:
        """Detach a source outlet and return its stored midpoint entry."""
        source_index = self._sources.index(source)
        midpoint = self._midpoints.pop(source_index)
        del self._sources[source_index]
        return midpoint

    def midpoint_for(self, source: Outlet) -> Midpoint:
        """Return the midpoint entry for a source outlet."""
        return self._midpoints[self._sources.index(source)]

    def set_types(self, types: XletTypes) -> None:
        """Replace the inlet type information."""
        self._types = types


class Outlet:
    """Represent an outlet and the patchcords routed out of it."""

    def __init__(
        self,
        parent: MaxObject,
        index: int,
        destinations: list[Inlet] | None = None,
        types: XletTypes = None,
    ) -> None:
        """Initialize an outlet for the given parent object."""
        self._parent = parent  # parent MaxObject
        self._destinations = destinations or []  # list of Inlets
        self._types: XletTypes = [] if types is None else types  # output types
        self._index = index  # index in parent object, starting from 0

    # some properties for getting info...
    @property
    def parent(self) -> MaxObject:
        """Return the parent object that owns this outlet."""
        return self._parent

    @property
    def destinations(self) -> list[Inlet]:
        """Return destination inlets connected to this outlet."""
        return self._destinations

    @property
    def types(self) -> XletTypes:
        """Return the emitted outlet connection types."""
        return self._types

    @property
    def index(self) -> int:
        """Return the outlet index within the parent object."""
        return self._index

    # for printing out...
    def __repr__(self) -> str:
        """Return a readable summary of the outlet and its destinations."""
        # report parent, index, and types
        rep = (
            f"{_parent_name(self.parent)}: outlet {self.index}, "
            f"types output: {self.types}"
        )

        # report destinations
        for destination in self._destinations:
            rep += (
                "\n\tdestination: "
                + _parent_name(destination.parent)
                + ": inlet "
                + str(destination.index)
            )
            midpoint = (
                destination.midpoint_for(self) if self in destination.sources else None
            )
            if midpoint is not None:
                rep += ", midpoints: " + str(midpoint)

        return rep

    def add_destination(self, destination: Inlet) -> None:
        """Attach a destination inlet."""
        self._destinations.append(destination)

    def remove_destination(self, destination: Inlet) -> None:
        """Detach a destination inlet."""
        self._destinations.remove(destination)

    def set_types(self, types: XletTypes) -> None:
        """Replace the outlet type information."""
        self._types = types
