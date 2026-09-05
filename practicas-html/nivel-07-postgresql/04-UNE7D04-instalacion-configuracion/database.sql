DROP SCHEMA IF EXISTS une7d04_environment CASCADE;
CREATE SCHEMA une7d04_environment;
SET search_path TO une7d04_environment, public;

CREATE TABLE environment_checks (
    check_id bigint GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    setting_name text NOT NULL UNIQUE,
    setting_value text NOT NULL,
    checked_at timestamptz NOT NULL DEFAULT CURRENT_TIMESTAMP
);

INSERT INTO environment_checks (setting_name, setting_value)
VALUES
    ('database', current_database()),
    ('user', current_user),
    ('server_version', current_setting('server_version')),
    ('server_encoding', current_setting('server_encoding')),
    ('client_encoding', current_setting('client_encoding')),
    ('time_zone', current_setting('TimeZone')),
    ('port', current_setting('port'));

SELECT version() AS complete_version;

SELECT setting_name, setting_value, checked_at
FROM environment_checks
ORDER BY setting_name;
