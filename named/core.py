from builtins import hasattr as has_attribute
from typing import Any, Protocol, runtime_checkable

from typing_extensions import TypeIs

__all__ = (
    # named
    "NAME",
    "Named",
    "get_name",
    "get_type_name",
    "has_name",
    "is_named",
    "set_name",
    "set_type_name",
    # moduled
    "MODULE",
    "Moduled",
    "get_module",
    "get_type_module",
    "has_module",
    "is_moduled",
    "set_module",
    "set_type_module",
)


NAME = "__name__"
"""The literal `__name__` string."""


@runtime_checkable
class Named(Protocol):
    """The named protocol for types that contain the `__name__` attribute."""

    __name__: str


def get_name(item: Named) -> str:
    """Fetches the `__name__` of the [`Named`][named.core.Named] `item`.

    Arguments:
        item: The item to fetch the name of.

    Returns:
        The name of the item.
    """
    return item.__name__


def set_name(item: Named, name: str) -> None:
    """Sets the `__name__` of the [`Named`][named.core.Named] `item`.

    Arguments:
        item: The item to set the name of.
        name: The name to set on the item.
    """
    item.__name__ = name


def get_type_name(item: Any) -> str:
    """Fetches the `__name__` of the `item` type.

    Arguments:
        item: The item to fetch the type name of.

    Returns:
        The name of the item type.
    """
    return get_name(type(item))  # type: ignore


def set_type_name(item: Any, name: str) -> None:
    """Sets the `__name__` of the `item` type.

    Arguments:
        item: The item to set the type name of.
        name: The name to set on the item type.
    """
    set_name(type(item), name)  # type: ignore


def is_named(item: Any) -> TypeIs[Named]:
    """Checks if the `item` implements the [`Named`][named.core.Named] protocol.

    Arguments:
        item: The item to check.

    Returns:
        Whether the item implements the [`Named`][named.core.Named] protocol.
    """
    return has_attribute(item, NAME)


has_name = is_named
"""An alias of [`is_named`][named.core.is_named]."""


MODULE = "__module__"
"""The literal `__module__` string."""


@runtime_checkable
class Moduled(Protocol):
    """The moduled protocol for types that contain the `__module__` attribute."""

    __module__: str


def get_module(item: Moduled) -> str:
    """Fetches the `__module__` of the [`Moduled`][named.core.Moduled] `item`.

    Arguments:
        item: The item to fetch the module of.

    Returns:
        The module of the item.
    """
    return item.__module__


def set_module(item: Moduled, module: str) -> None:
    """Sets the `__module__` of the [`Moduled`][named.core.Moduled] `item`.

    Arguments:
        item: The item to set the module of.
        module: The module to set on the item.
    """
    item.__module__ = module


def get_type_module(item: Any) -> str:
    """Fetches the `__module__` of the `item` type.

    Arguments:
        item: The item to fetch the type module of.

    Returns:
        The module of the item type.
    """
    return get_module(type(item))  # type: ignore


def set_type_module(item: Any, module: str) -> None:
    """Sets the `__module__` of the `item` type.

    Arguments:
        item: The item to set the type module of.
        module: The module to set on the item type.
    """
    set_module(type(item), module)  # type: ignore


def is_moduled(item: Any) -> TypeIs[Moduled]:
    """Checks if the `item` implements the [`Moduled`][named.core.Moduled] protocol.

    Arguments:
        item: The item to check.

    Returns:
        Whether the item implements the [`Moduled`][named.core.Moduled] protocol.
    """
    return has_attribute(item, MODULE)


has_module = is_moduled
"""An alias of [`is_moduled`][named.core.is_moduled]."""
