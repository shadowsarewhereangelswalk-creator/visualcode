DROP SCHEMA IF EXISTS une7d09_data_types CASCADE;
CREATE SCHEMA une7d09_data_types;
SET search_path TO une7d09_data_types, public;

CREATE TABLE professional_profiles (
    profile_id bigint GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    public_id uuid NOT NULL UNIQUE,
    username varchar(60) NOT NULL UNIQUE,
    full_name text NOT NULL,
    biography text,
    hourly_rate numeric(10, 2) NOT NULL CHECK (hourly_rate >= 0),
    years_experience smallint NOT NULL DEFAULT 0 CHECK (years_experience >= 0),
    available boolean NOT NULL DEFAULT true,
    birth_date date,
    last_access timestamptz,
    response_time interval,
    skills text[] NOT NULL DEFAULT '{}',
    preferences jsonb NOT NULL DEFAULT '{}'::jsonb,
    last_ip inet,
    created_at timestamptz NOT NULL DEFAULT CURRENT_TIMESTAMP
);

INSERT INTO professional_profiles (
    public_id, username, full_name, biography, hourly_rate, years_experience,
    available, birth_date, last_access, response_time, skills, preferences, last_ip
)
VALUES (
    '2f1b47d0-6483-4f94-8a2d-114bb369e17b',
    'karen.dev',
    'Karen Agostini',
    'Profesional enfocada en proyectos digitales.',
    45.00,
    6,
    true,
    '1990-05-15',
    '2027-01-09 14:30:00-04',
    INTERVAL '2 hours 15 minutes',
    ARRAY['HTML', 'CSS', 'JavaScript', 'PostgreSQL'],
    '{"language":"es","notifications":true,"theme":"dark"}'::jsonb,
    '192.0.2.25'
);

SELECT
    profile_id, public_id, username, full_name, hourly_rate, available, skills,
    preferences ->> 'language' AS preferred_language, last_ip, created_at
FROM professional_profiles;
