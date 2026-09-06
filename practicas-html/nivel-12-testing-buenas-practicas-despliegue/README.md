# Nivel 12 — Testing, buenas prácticas y despliegue

Este nivel contiene 30 clases con prácticas completas. Cada clase está separada en su propia carpeta e incluye código terminado y sin comentarios.

| Clase | ID oficial | Práctica | Tecnologías |
|---:|---|---|---|
| 1 | UNE12D01 | [Introducción al Nivel 12: objetivos, herramientas y proyecto del mes](01-UNE12D01-introduccion-nivel/README.md) | pytest y Python |
| 2 | UNE12D02 | [Fundamentos de principios de testing y pirámide de pruebas](02-UNE12D02-principios-testing/README.md) | pytest y Python |
| 3 | UNE12D03 | [Ejercicio guiado de principios de testing y pirámide de pruebas](03-UNE12D03-practica-piramide-pruebas/README.md) | pytest, mocks y Python |
| 4 | UNE12D04 | [Fundamentos de pruebas unitarias con unittest](04-UNE12D04-unittest/README.md) | unittest y Python |
| 5 | UNE12D05 | [Ejercicio guiado de pruebas unitarias con unittest](05-UNE12D05-practica-unittest/README.md) | unittest y Python |
| 6 | UNE12D06 | [Fundamentos de pruebas unitarias con pytest](06-UNE12D06-pytest/README.md) | pytest y Python |
| 7 | UNE12D07 | [Ejercicio guiado de pruebas unitarias con pytest](07-UNE12D07-practica-pytest/README.md) | pytest y Python |
| 8 | UNE12D08 | [Práctica P1: suite de pruebas unitarias con pytest para un proyecto propio](08-UNE12D08-practica-suite-pytest/README.md) | pytest, JSON y Python |
| 9 | UNE12D09 | [Fundamentos de fixtures, parametrización y mocks](09-UNE12D09-fixtures-parametrizacion-mocks/README.md) | pytest, fixtures y mocks |
| 10 | UNE12D10 | [Ejercicio guiado de fixtures, parametrización y mocks](10-UNE12D10-practica-fixtures-mocks/README.md) | pytest, fixtures y mocks |
| 11 | UNE12D11 | [Fundamentos de linters y análisis estático](11-UNE12D11-linters-analisis-estatico/README.md) | Ruff, pytest y Python |
| 12 | UNE12D12 | [Ejercicio guiado de linters y análisis estático](12-UNE12D12-practica-linters/README.md) | Ruff, pytest y Python |
| 13 | UNE12D13 | [Fundamentos de formateo automático de código](13-UNE12D13-formateo-automatico/README.md) | Black, pytest y Python |
| 14 | UNE12D14 | [Ejercicio guiado de formateo automático de código](14-UNE12D14-practica-formateo/README.md) | Black, pytest y Python |
| 15 | UNE12D15 | [Práctica P2: configuración de un entorno virtual y requirements.txt](15-UNE12D15-practica-entorno-requirements/README.md) | venv, requirements, Ruff y Black |
| 16 | UNE12D16 | [Fundamentos de cobertura de código](16-UNE12D16-cobertura-codigo/README.md) | Coverage.py y pytest |
| 17 | UNE12D17 | [Ejercicio guiado de cobertura de código](17-UNE12D17-practica-cobertura/README.md) | Coverage.py y pytest |
| 18 | UNE12D18 | [Fundamentos de entornos virtuales](18-UNE12D18-entornos-virtuales/README.md) | venv, pytest y Python |
| 19 | UNE12D19 | [Ejercicio guiado de entornos virtuales](19-UNE12D19-practica-entornos-virtuales/README.md) | venv, pytest y Python |
| 20 | UNE12D20 | [Fundamentos de requirements.txt y gestión de dependencias](20-UNE12D20-requirements-dependencias/README.md) | Packaging, requirements y pytest |
| 21 | UNE12D21 | [Fundamentos de Git: commits, ramas y merges](21-UNE12D21-git-commits-ramas-merges/README.md) | Git, pytest y Python |
| 22 | UNE12D22 | [Práctica P3: repositorio Git con flujo de ramas y pull requests](22-UNE12D22-practica-git-flujo-pr/README.md) | Git, pytest y GitHub |
| 23 | UNE12D23 | [Fundamentos de GitHub: repositorios, pull requests y revisión](23-UNE12D23-github-repos-pr-revision/README.md) | GitHub, CODEOWNERS y pytest |
| 24 | UNE12D24 | [Fundamentos de integración continua con GitHub Actions](24-UNE12D24-integracion-continua-actions/README.md) | GitHub Actions, Ruff, Black, Coverage.py y pytest |
| 25 | UNE12D25 | [Fundamentos de fundamentos de Docker](25-UNE12D25-fundamentos-docker/README.md) | Docker, Flask y Gunicorn |
| 26 | UNE12D26 | [Práctica P4: contenerización de una aplicación Python con Docker](26-UNE12D26-practica-docker-python/README.md) | Docker, Compose, Flask y Gunicorn |
| 27 | UNE12D27 | [Fundamentos de Dockerfile e imagen de una aplicación Python](27-UNE12D27-dockerfile-imagen-python/README.md) | Docker, Flask y Gunicorn |
| 28 | UNE12D28 | [Fundamentos de contenedores, variables de entorno y puertos](28-UNE12D28-contenedores-variables-puertos/README.md) | Docker, Compose y Flask |
| 29 | UNE12D29 | [Fundamentos de despliegue de Flask o Django en la nube](29-UNE12D29-despliegue-flask-nube/README.md) | Flask, Gunicorn, Docker y Render |
| 30 | UNE12D30 | [Práctica P5: proyecto de despliegue de una aplicación Flask o Django en la nube](30-UNE12D30-practica-despliegue-nube/README.md) | Flask, pytest, GitHub Actions, Docker, Compose y Render |

Las cinco prácticas principales corresponden a las clases 8, 15, 22, 26 y 30. El proyecto final es una aplicación Flask preparada para pruebas, análisis estático, formateo, cobertura, integración continua, ejecución con Gunicorn, contenerización con Docker y despliegue en la nube.

Todas las clases incluyen `app.py`, `requirements.txt` y el modo de comprobación `python app.py --check`. El nivel reúne 109 casos de prueba; las clases 16, 17, 24 y 30 alcanzan cobertura total del código medido.

