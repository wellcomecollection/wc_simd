# Workspace of SIMD

A workspace by [@danniesim](https://github.com/danniesim) while working with the Wellcome Collection Digital Platform and Machine Learning team.

This workspace is meant to be used with VS Code.

## UV and Python Package

 The source of the `wc_simd` Python package is found in [src/wc_simd](./src/wc_simd/)

I use UV for Python dependency management, you may install it with this line `curl -LsSf https://astral.sh/uv/install.sh | sh`.

To be able to import the `wc_simd` module from code and install Python dependencies, run: `uv sync` from the repo root.

If `requirements.txt` is needed, run: `uv run pip freeze > requirements.txt`

## Notebooks

Explorations and experiments found in [notebooks](./notebooks/).

## Data Directory

Bespoke data files are placed in [data](./data). Files that can be imported from other sources are found in [data/imports](./data/imports/). See: [Data Import Index](./data/imports/data_import_index.md)

## Local Spark with Hadoop and Hive

See [this](./docs/local_hive_spark.md)

## Tests

I use [pytest](https://docs.pytest.org/) for testing. Tests can be found in [tests](./tests/).

## Lint and Spellcheck

I use LTeX and Markdown Lint to keep my docs and comments sane. Here are my [recommended VS Code extensions](./.vscode/extensions.json)
