DROP SCHEMA IF EXISTS une7d10_types_practice CASCADE;
CREATE SCHEMA une7d10_types_practice;
SET search_path TO une7d10_types_practice, public;

CREATE TYPE membership_status AS ENUM ('trial', 'active', 'paused', 'cancelled');

CREATE TABLE memberships (
    membership_id bigint GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    member_code char(8) NOT NULL UNIQUE,
    full_name text NOT NULL,
    email text NOT NULL UNIQUE,
    status membership_status NOT NULL DEFAULT 'trial',
    monthly_fee numeric(8, 2) NOT NULL CHECK (monthly_fee >= 0),
    interests text[] NOT NULL DEFAULT '{}',
    profile_data jsonb NOT NULL DEFAULT '{}'::jsonb,
    access_network cidr,
    active_period daterange NOT NULL,
    created_at timestamptz NOT NULL DEFAULT CURRENT_TIMESTAMP
);

INSERT INTO memberships (
    member_code, full_name, email, status, monthly_fee, interests,
    profile_data, access_network, active_period
)
VALUES
    ('MEM00001', 'Ana Torres', 'ana@example.com', 'active', 29.90, ARRAY['SQL', 'Datos'], '{"level":7,"certificate":false}'::jsonb, '192.0.2.0/24', daterange('2027-01-01', '2027-06-30', '[]')),
    ('MEM00002', 'Bruno Díaz', 'bruno@example.com', 'trial', 0.00, ARRAY['Backend', 'APIs'], '{"level":7,"certificate":true}'::jsonb, '198.51.100.0/24', daterange('2027-01-10', '2027-01-24', '[]'));

UPDATE memberships
SET
    interests = array_append(interests, 'PostgreSQL'),
    profile_data = jsonb_set(profile_data, '{last_module}', '"PL/pgSQL"')
WHERE member_code = 'MEM00001';

SELECT
    membership_id, member_code, full_name, status, monthly_fee, interests,
    profile_data, access_network, lower(active_period) AS starts_on,
    upper(active_period) AS ends_on
FROM memberships
ORDER BY membership_id;
