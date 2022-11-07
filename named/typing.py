from builtins import hasattr as has_attribute
from typing import Any

from typing_extensions import Protocol, TypeGuard, runtime_checkable

__all__ = ("NAME", "Named", "get_name", "get_type_name", "is_named")


NAME = "__name__"
"""The literal `__name__` string."""


@runtime_checkable
class Named(Protocol):
    """The named protocol for types that contain the `__name__` attribute."""
    __name__: str


def get_name(item: Named) -> str:
    """Fetches the `__name__` of the [`Named`][named.typing.Named] `item`.

    Arguments:
        item: The item to fetch the name of.

    Returns:
        The name of the item.
    """
    return item.__name__


def get_type_name(item: Any) -> str:
    """Fetches the `__name__` of the `item` type.

    Arguments:
        item: The item to fetch the type name of.

    Returns:
        The name of the item type.
    """
    return get_name(type(item))  # type: ignore


def is_named(item: Any) -> TypeGuard[Named]:
    """Checks if the `item` implements the [`Named`][named.typing.Named] protocol.

    Arguments:
        item: The item to check.

    Returns:
        Whether the item implements the [`Named`][named.typing.Named] protocol.
    """
    return has_attribute(item, NAME)
