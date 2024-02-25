"""Named types.

This library defines the [`Named`][named.typing.Named] protocol for types
that contain the `__name__` attribute, abstracting the attribute itself away.

It also provides the [`get_name`][named.typing.get_name] function to fetch
the name of the item provided, along with [`get_type_name`][named.typing.get_type_name], such that

```python
get_type_item(item)
# is equivalent to
get_name(type(item))
```

Lastly, there is the type guard function called [`is_named`][named.typing.is_named], which checks
for the presence of `__name__` attribute
(which is exported in the [`NAME`][named.typing.NAME] constant).
"""

__description__ = "Named types."
__url__ = "https://github.com/nekitdev/named"

__title__ = "named"
__author__ = "nekitdev"
__license__ = "MIT"
__version__ = "1.4.0"

from named.core import (
    MODULE,
    NAME,
    Moduled,
    Named,
    get_module,
    get_name,
    get_type_module,
    get_type_name,
    has_module,
    has_name,
    is_moduled,
    is_named,
    set_module,
    set_name,
    set_type_module,
    set_type_name,
)

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
