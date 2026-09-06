# UNE12D30 — P5: proyecto de despliegue de una aplicación Flask o Django en la nube

Solución de referencia con Flask, Gunicorn y Docker. El proyecto puede ejecutarse localmente o desplegarse en un proveedor compatible con contenedores.

## Local

```bash
python -m venv .venv
pip install -r requirements.txt
python app.py
```

## Docker

```bash
docker build -t une12d30 .
docker run -p 8000:8000 une12d30
```

Comprueba `/salud` después del despliegue. La URL pública y las capturas son evidencia académica externa al repositorio.
