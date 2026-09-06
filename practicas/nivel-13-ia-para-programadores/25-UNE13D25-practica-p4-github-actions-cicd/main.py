from pathlib import Path
workflow='''name: ci\non:\n  push:\n  pull_request:\njobs:\n  test:\n    runs-on: ubuntu-latest\n    steps:\n      - uses: actions/checkout@v4\n      - uses: actions/setup-python@v5\n        with:\n          python-version: "3.12"\n      - run: python -m unittest discover\n'''
Path("ci.yml").write_text(workflow,encoding="utf-8")
print(Path("ci.yml").read_text(encoding="utf-8"))
