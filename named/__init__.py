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
__version__ = "1.1.0"

from named.typing import NAME, Named, get_name, get_type_name, is_named

__all__ = ("NAME", "Named", "get_name", "get_type_name", "is_named")
