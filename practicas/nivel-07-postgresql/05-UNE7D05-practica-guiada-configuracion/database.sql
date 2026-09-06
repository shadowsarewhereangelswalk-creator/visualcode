SET application_name TO 'UNE7D05 PostgreSQL Lab';
SET TIME ZONE 'UTC';

DROP SCHEMA IF EXISTS une7d05_configuration CASCADE;
CREATE SCHEMA une7d05_configuration;
SET search_path TO une7d05_configuration, public;

CREATE TABLE session_configuration (
    configuration_id bigint GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    application_name text NOT NULL,
    database_name text NOT NULL,
    user_name text NOT NULL,
    time_zone text NOT NULL,
    transaction_isolation text NOT NULL,
    client_encoding text NOT NULL,
    recorded_at timestamptz NOT NULL DEFAULT CURRENT_TIMESTAMP
);

INSERT INTO session_configuration (
    application_name,
    database_name,
    user_name,
    time_zone,
    transaction_isolation,
    client_encoding
)
VALUES (
    current_setting('application_name'),
    current_database(),
    current_user,
    current_setting('TimeZone'),
    current_setting('transaction_isolation'),
    current_setting('client_encoding')
);

SELECT name, setting, unit, context
FROM pg_settings
WHERE lower(name) IN (
    'application_name',
    'client_encoding',
    'max_connections',
    'port',
    'server_version',
    'timezone'
)
ORDER BY name;

SELECT *
FROM session_configuration;
