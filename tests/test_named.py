import pytest

import named
from named.core import (
    get_module,
    get_name,
    get_type_module,
    get_type_name,
    is_moduled,
    is_named,
    set_module,
    set_name,
    set_type_module,
    set_type_name,
)

INT = "int"
NAMED = "named"

TYPE = "type"
MODULE = "module"

BUILTINS = "builtins"
NAMED_CORE = "named.core"

NAME = "Name"


class Type:
    pass


instance = Type()


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


def test_is_moduled() -> None:
    assert is_moduled(int)
    assert not is_moduled(42)
    assert not is_moduled(named)
    assert is_moduled(is_moduled)


def test_get_module() -> None:
    assert get_module(int) == BUILTINS

    with pytest.raises(AttributeError):
        get_module(69)  # type: ignore

    with pytest.raises(AttributeError):
        get_module(named)  # type: ignore

    assert get_module(get_module) == NAMED_CORE


def test_get_type_module() -> None:
    assert get_type_module(int) == BUILTINS
    assert get_type_module(named) == BUILTINS
    assert get_type_module(13) == BUILTINS


def test_set_name() -> None:
    with pytest.raises(TypeError):
        set_name(int, NAME)

    set_name(Type, NAME)

    assert get_name(Type) == NAME


def test_set_type_name() -> None:
    with pytest.raises(TypeError):
        set_type_name(42, NAME)

    set_type_name(instance, NAME)

    assert get_type_name(instance) == NAME


def test_set_module() -> None:
    with pytest.raises(TypeError):
        set_module(int, MODULE)

    set_module(Type, MODULE)

    assert get_module(Type) == MODULE


def test_set_type_module() -> None:
    with pytest.raises(TypeError):
        set_type_module(69, MODULE)

    set_type_module(instance, MODULE)

    assert get_type_module(instance) == MODULE
