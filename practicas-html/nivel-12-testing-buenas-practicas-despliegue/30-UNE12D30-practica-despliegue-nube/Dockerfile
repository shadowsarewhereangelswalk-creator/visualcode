FROM python:3.12-slim AS builder
WORKDIR /build
COPY requirements.txt .
RUN pip wheel --no-cache-dir --wheel-dir /wheels -r requirements.txt

FROM python:3.12-slim AS runtime
WORKDIR /app
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV PORT=10000
RUN useradd --uid 10001 --create-home appuser
COPY --from=builder /wheels /wheels
RUN pip install --no-cache-dir /wheels/*
COPY --chown=appuser:appuser deployment_app deployment_app
COPY --chown=appuser:appuser wsgi.py app.py ./
USER 10001
EXPOSE 10000
HEALTHCHECK --interval=30s --timeout=3s --start-period=5s --retries=3 CMD python -c "from urllib.request import urlopen; urlopen('http://127.0.0.1:10000/health', timeout=2)"
CMD ["sh", "-c", "gunicorn --bind 0.0.0.0:${PORT} --workers 2 --threads 2 --timeout 60 wsgi:app"]

