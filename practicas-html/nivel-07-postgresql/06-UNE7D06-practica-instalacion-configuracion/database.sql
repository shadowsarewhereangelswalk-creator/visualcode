DROP SCHEMA IF EXISTS une7d06_installation_check CASCADE;
CREATE SCHEMA une7d06_installation_check;
SET search_path TO une7d06_installation_check, public;

CREATE TABLE server_health_checks (
    check_id bigint GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    check_name text NOT NULL,
    expected_value text NOT NULL,
    actual_value text NOT NULL,
    passed boolean NOT NULL,
    checked_at timestamptz NOT NULL DEFAULT CURRENT_TIMESTAMP
);

INSERT INTO server_health_checks (check_name, expected_value, actual_value, passed)
VALUES
    ('PostgreSQL disponible', 'Versión 14 o superior', current_setting('server_version'), current_setting('server_version_num')::integer >= 140000),
    ('Codificación del servidor', 'UTF8', current_setting('server_encoding'), current_setting('server_encoding') = 'UTF8'),
    ('Conexión activa', 'Base y usuario identificados', current_database() || ' / ' || current_user, current_database() IS NOT NULL AND current_user IS NOT NULL),
    ('Zona horaria disponible', 'Valor configurado', current_setting('TimeZone'), length(current_setting('TimeZone')) > 0);

CREATE TABLE installation_evidence (
    evidence_id bigint GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    message text NOT NULL,
    created_at timestamptz NOT NULL DEFAULT CURRENT_TIMESTAMP
);

INSERT INTO installation_evidence (message)
VALUES ('PostgreSQL está instalado, conectado y listo para las prácticas del Nivel 7');

SELECT check_name, expected_value, actual_value, passed, checked_at
FROM server_health_checks
ORDER BY check_id;

SELECT *
FROM installation_evidence;
