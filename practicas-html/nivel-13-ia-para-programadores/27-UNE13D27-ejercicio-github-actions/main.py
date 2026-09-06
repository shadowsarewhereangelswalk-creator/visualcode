from pathlib import Path
contenido='''name: validate\non: [push]\njobs:\n  check:\n    runs-on: ubuntu-latest\n    steps:\n      - uses: actions/checkout@v4\n      - run: python main.py\n'''
Path("workflow.yml").write_text(contenido,encoding="utf-8")
print("workflow.yml creado")
