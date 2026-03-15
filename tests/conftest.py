"""Shared pytest fixtures."""

import logging

import pytest


@pytest.fixture(autouse=True)
def _capture_maxpylang_logs(caplog: pytest.LogCaptureFixture) -> None:
    """Capture MaxPyLang logs at INFO level by default."""
    caplog.set_level(logging.INFO, logger="maxpylang")
