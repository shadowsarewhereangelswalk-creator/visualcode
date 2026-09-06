DROP SCHEMA IF EXISTS une7d01_lab CASCADE;
CREATE SCHEMA une7d01_lab;
SET search_path TO une7d01_lab, public;

CREATE TABLE learning_goals (
    goal_id bigint GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    title text NOT NULL UNIQUE,
    category text NOT NULL CHECK (category IN ('Diseño', 'Consultas', 'Automatización', 'Migración')),
    completed boolean NOT NULL DEFAULT false,
    created_at timestamptz NOT NULL DEFAULT CURRENT_TIMESTAMP
);

INSERT INTO learning_goals (title, category)
VALUES
    ('Diseñar modelos Entidad-Relación', 'Diseño'),
    ('Construir consultas CRUD', 'Consultas'),
    ('Crear funciones y triggers en PL/pgSQL', 'Automatización'),
    ('Migrar un esquema relacional', 'Migración');

SELECT
    current_database() AS database_name,
    current_user AS database_user,
    current_setting('server_version') AS postgresql_version;

SELECT
    goal_id,
    title,
    category,
    completed,
    created_at
FROM learning_goals
ORDER BY goal_id;
