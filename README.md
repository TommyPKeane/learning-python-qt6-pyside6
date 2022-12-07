# Examples of Qt Applications with `pyside6` for `Qt6` in Python

This is an example/tutorial repository of Open-Source (GPL) Qt Applications using `pyside6` and Python on top of `Qt6`, which retains the GPLv2 Licensing (see the [`LICENSE`](./LICENSE) file).

<!-- MarkdownTOC -->

- Developer Setup
- Examples
    - `example_basic`
- Creating New Examples with `cookiecutter`
- Reference Links

<!-- /MarkdownTOC -->

## Developer Setup

1. `direnv allow`
1. `pip install --upgrade pip`
1. `pip install poetry`
1. `poetry install`

For each example, it is not necessary that you have `qmake` in your `PATH` in order to install `pyside6`, but if you want to use all of the `Qt6` features and create a built/exported application, you made need to download and install the `Qt6` open-source installer.

The Qt Installer -- [`https://www.qt.io/download-open-source`](https://www.qt.io/download-open-source) -- should be downloaded and run before doing any of the above.

## Examples

This repository contains several isolated examples of `Qt6` Applications using `pyside6`, which are each summarized here in this section of the README.

### `example_basic`

Simple example of an application that generates a window with a few basic callbacks. This example is meant to be a catchall introduction to `pyside6` development without getting too deeply into any specifics.

## Creating New Examples with `cookiecutter`

The top-level directory for this repository is setup with `direnv`, `poetry`, and a scaffolding package for Python called `cookiecutter`, which allows for easy creation of new examples with a bunch of common code and files.

To create a new example directory here, run the following:

1. `cookiecutter ./_cookiecutter-template`
1. Fill-out new values for each entry

## Reference Links

- direnv: [`https://direnv.net/`](https://direnv.net/)
- Qt Online Installer: [`https://www.qt.io/download-open-source`](https://www.qt.io/download-open-source)
- Qt Offline Installers: [`https://www.qt.io/offline-installers`](https://www.qt.io/offline-installers)
- `pyside6` PyPI Package: [`https://pypi.org/project/PySide6/`](https://pypi.org/project/PySide6/)
- `pyside6` Documentatoin: [`https://doc.qt.io/qtforpython/quickstart.html`](https://doc.qt.io/qtforpython/quickstart.html)
