# Workspace of SIMD

A workspace by @danniesim while working with the Wellcome Collection Digital Platform and Machine Learning team.

## Poetry

To be able to import the `wc_simd` module from code, from the repo root, run:
`poetry install`

If `requirements.txt` is needed:

- Install exporter: `poetry self add poetry-plugin-export`
- Export `requirements.txt`: `poetry export --without-hashes --format=requirements.txt > requirements.txt`
