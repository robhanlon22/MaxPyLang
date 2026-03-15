"""Pre-instantiated MaxObject stubs for all imported packages."""
# ruff: noqa: F403
import contextlib
import warnings

from maxpylang.exceptions import UnknownObjectWarning

# Suppress warnings while loading stubs.
with warnings.catch_warnings():
    warnings.simplefilter("ignore", UnknownObjectWarning)
    with contextlib.suppress(ImportError):
        from .jit import *
    with contextlib.suppress(ImportError):
        from .max import *
    with contextlib.suppress(ImportError):
        from .msp import *
