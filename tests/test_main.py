"""Pytest-only test suite for favision."""

import pytest

from favision import main


def test_main_runs(capsys: pytest.CaptureFixture[str]) -> None:
    """main() prints the greeting without raising."""
    assert callable(main)
    main()
    captured = capsys.readouterr()
    assert "Hello from favision!" in captured.out


def test_main_returns_none() -> None:
    main()
