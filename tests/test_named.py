import pytest

import named
from named import get_name, get_type_name, is_named

INT = "int"
NAMED = "named"

TYPE = "type"
MODULE = "module"


def test_is_named() -> None:
    assert is_named(int)
    assert is_named(named)
    assert not is_named(7)


def test_get_name() -> None:
    assert get_name(int) == INT
    assert get_name(named) == NAMED

    with pytest.raises(AttributeError):
        get_name(13)  # type: ignore


def test_get_type_name() -> None:
    assert get_type_name(int) == TYPE
    assert get_type_name(named) == MODULE
    assert get_type_name(42) == INT
