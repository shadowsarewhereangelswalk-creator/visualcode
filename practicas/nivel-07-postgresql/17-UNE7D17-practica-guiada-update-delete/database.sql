DROP SCHEMA IF EXISTS une7d17_cleanup CASCADE;
CREATE SCHEMA une7d17_cleanup;
SET search_path TO une7d17_cleanup, public;

CREATE TABLE access_sessions (
    session_id bigint GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    user_email text NOT NULL,
    token_hash char(64) NOT NULL UNIQUE,
    last_activity timestamptz NOT NULL,
    revoked boolean NOT NULL DEFAULT false
);

CREATE TABLE deleted_sessions (
    archive_id bigint GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    original_session_id bigint NOT NULL,
    user_email text NOT NULL,
    token_hash char(64) NOT NULL,
    last_activity timestamptz NOT NULL,
    archived_at timestamptz NOT NULL DEFAULT CURRENT_TIMESTAMP
);

INSERT INTO access_sessions (
    user_email,
    token_hash,
    last_activity,
    revoked
)
VALUES
    (
        'ana@example.com',
        repeat('a', 64),
        '2027-01-16 10:00:00-04',
        false
    ),
    (
        'bruno@example.com',
        repeat('b', 64),
        '2026-10-01 08:00:00-04',
        true
    ),
    (
        'carla@example.com',
        repeat('c', 64),
        '2026-09-15 12:00:00-04',
        true
    ),
    (
        'diego@example.com',
        repeat('d', 64),
        '2027-01-15 16:30:00-04',
        false
    );

UPDATE access_sessions
SET revoked = true
WHERE user_email = 'diego@example.com'
  AND last_activity < '2027-01-16 00:00:00-04'
RETURNING session_id, user_email, revoked;

WITH deleted AS (
    DELETE FROM access_sessions
    WHERE revoked = true
      AND last_activity < '2027-01-01 00:00:00-04'
    RETURNING
        session_id,
        user_email,
        token_hash,
        last_activity
)
INSERT INTO deleted_sessions (
    original_session_id,
    user_email,
    token_hash,
    last_activity
)
SELECT
    session_id,
    user_email,
    token_hash,
    last_activity
FROM deleted
RETURNING archive_id, original_session_id, user_email, archived_at;

SELECT
    session_id,
    user_email,
    last_activity,
    revoked
FROM access_sessions
ORDER BY session_id;

SELECT
    archive_id,
    original_session_id,
    user_email,
    archived_at
FROM deleted_sessions
ORDER BY archive_id;
