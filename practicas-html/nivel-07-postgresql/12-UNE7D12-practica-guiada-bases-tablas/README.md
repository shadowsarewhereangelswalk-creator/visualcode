# UNE7D12 — Ejercicio guiado de creación de bases y tablas

Clase 12 del Nivel 7 — PostgreSQL.

- **Objetivo:** Comprender y aplicar ejercicio guiado de creación de bases y tablas dentro del objetivo del Nivel 7.
- **Conceptos:** Ejercicio guiado de creación de bases y tablas
- **Herramientas:** PostgreSQL, psql, pgAdmin, SQL
- **Proyecto del nivel:** Migración a PostgreSQL
- **Ejercicio:** Realizar un ejemplo guiado de ejercicio guiado de creación de bases y tablas.
- **Entregable:** Resolver una práctica corta y responder preguntas de comprobación.
- **Archivos:** `database.sql` y `create-database.psql`

Abre `database.sql` en pgAdmin o ejecútalo con psql. El archivo recrea únicamente el esquema `une7d12_academy` e incluye estructura, datos y consultas de comprobación terminadas.

## Ejecución completa con psql

Conéctate a una base administrativa y ejecuta:

```bash
psql -d postgres -f create-database.psql
```

El script crea la base, cambia la conexión y construye todas las tablas relacionadas.
