# UNE12D24 — Fundamentos de integración continua con GitHub Actions

Clase 24 del Nivel 12 — Testing, buenas prácticas y despliegue.

- **Práctica:** Fundamentos de integración continua con GitHub Actions
- **Resultado terminado:** Pipeline CI para dos versiones de Python con calidad y cobertura completas.
- **Herramientas:** GitHub Actions, Ruff, Black, Coverage.py y pytest y Visual Studio Code
- **Proyecto del nivel:** Aplicación desplegada

1. Crea el entorno con `python -m venv .venv`.
2. Activa el entorno virtual.
3. Ejecuta `python -m pip install -r requirements.txt`.
4. Ejecuta `python app.py`.
5. Ejecuta `python -m pytest`.

Ejecuta `ruff check .` para validar el análisis estático.

Ejecuta `black --check .` para comprobar el formato.

Ejecuta `coverage run -m pytest` y `coverage report` para comprobar la cobertura.

Comprueba la estructura con `python app.py --check`.

