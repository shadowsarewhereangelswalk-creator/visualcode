# UNE10D28 — Fundamentos de publicación de prueba en PyPI

Clase 28 del Nivel 10 — Python III: Flask.

- **Práctica:** Fundamentos de publicación de prueba en PyPI
- **Resultado terminado:** Paquete de slugs listo para construir, comprobar y subir a TestPyPI.
- **Herramientas:** Python, Flask y Visual Studio Code
- **Proyecto del nivel:** Servicio Flask

1. Crea y activa un entorno virtual.
2. Ejecuta `python -m pip install -r requirements.txt`.
3. Ejecuta `python -m pytest`.
4. Ejecuta `python -m build`.
5. Ejecuta `python -m twine check dist/*`.
6. Crea un token en TestPyPI y ejecuta `python -m twine upload --repository testpypi dist/*`.
7. Instala el paquete con `python -m pip install --index-url https://test.pypi.org/simple/ --extra-index-url https://pypi.org/simple ai-career-slug-demo`.

Comprueba la estructura y la lógica independiente con `python app.py --check`.

