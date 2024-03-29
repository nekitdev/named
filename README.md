# `named`

[![License][License Badge]][License]
[![Version][Version Badge]][Package]
[![Downloads][Downloads Badge]][Package]
[![Discord][Discord Badge]][Discord]

[![Documentation][Documentation Badge]][Documentation]
[![Check][Check Badge]][Actions]
[![Test][Test Badge]][Actions]
[![Coverage][Coverage Badge]][Coverage]

> *Named types.*

## Installing

**Python 3.8 or above is required.**

### pip

Installing the library with `pip` is quite simple:

```console
$ pip install named
```

Alternatively, the library can be installed from source:

```console
$ git clone https://github.com/nekitdev/named.git
$ cd named
$ python -m pip install .
```

### poetry

You can add `named` as a dependency with the following command:

```console
$ poetry add named
```

Or by directly specifying it in the configuration like so:

```toml
[tool.poetry.dependencies]
named = "^1.4.2"
```

Alternatively, you can add it directly from the source:

```toml
[tool.poetry.dependencies.named]
git = "https://github.com/nekitdev/named.git"
```

## Example

```python
>>> from named import get_name, get_type_name, is_named
>>> print(is_named(int))
True
>>> print(get_name(int))
int
>>> print(is_named(42))
False
>>> print(get_type_name(42))
int
```

## Documentation

You can find the documentation [here][Documentation].

## Support

If you need support with the library, you can send an [email][Email]
or refer to the official [Discord server][Discord].

## Changelog

You can find the changelog [here][Changelog].

## Security Policy

You can find the Security Policy of `named` [here][Security].

## Contributing

If you are interested in contributing to `named`, make sure to take a look at the
[Contributing Guide][Contributing Guide], as well as the [Code of Conduct][Code of Conduct].

## License

`named` is licensed under the MIT License terms. See [License][License] for details.

[Email]: mailto:support@nekit.dev

[Discord]: https://nekit.dev/chat

[Actions]: https://github.com/nekitdev/named/actions

[Changelog]: https://github.com/nekitdev/named/blob/main/CHANGELOG.md
[Code of Conduct]: https://github.com/nekitdev/named/blob/main/CODE_OF_CONDUCT.md
[Contributing Guide]: https://github.com/nekitdev/named/blob/main/CONTRIBUTING.md
[Security]: https://github.com/nekitdev/named/blob/main/SECURITY.md

[License]: https://github.com/nekitdev/named/blob/main/LICENSE

[Package]: https://pypi.org/project/named
[Coverage]: https://codecov.io/gh/nekitdev/named
[Documentation]: https://nekitdev.github.io/named

[Discord Badge]: https://img.shields.io/discord/728012506899021874
[License Badge]: https://img.shields.io/pypi/l/named
[Version Badge]: https://img.shields.io/pypi/v/named
[Downloads Badge]: https://img.shields.io/pypi/dm/named

[Documentation Badge]: https://github.com/nekitdev/named/workflows/docs/badge.svg
[Check Badge]: https://github.com/nekitdev/named/workflows/check/badge.svg
[Test Badge]: https://github.com/nekitdev/named/workflows/test/badge.svg
[Coverage Badge]: https://codecov.io/gh/nekitdev/named/branch/main/graph/badge.svg
