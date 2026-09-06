# UNE7D11 — Fundamentos de creación de bases y tablas

Clase 11 del Nivel 7 — PostgreSQL.

- **Objetivo:** Comprender y aplicar fundamentos de creación de bases y tablas dentro del objetivo del Nivel 7.
- **Conceptos:** Fundamentos de creación de bases y tablas
- **Herramientas:** PostgreSQL, psql, pgAdmin, SQL
- **Proyecto del nivel:** Migración a PostgreSQL
- **Ejercicio:** Realizar un ejemplo guiado de fundamentos de creación de bases y tablas.
- **Entregable:** Resolver una práctica corta y responder preguntas de comprobación.
- **Archivos:** `database.sql` y `create-database.psql`

Abre `database.sql` en pgAdmin o ejecútalo con psql. El archivo recrea únicamente el esquema `une7d11_app` e incluye estructura, datos y consultas de comprobación terminadas.

## Crear la base completa con psql

Conéctate a una base administrativa, abre una terminal en esta carpeta y ejecuta:

```bash
psql -d postgres -f create-database.psql
```

El archivo crea `une7d11_workspace`, se conecta a ella y ejecuta `database.sql`.
