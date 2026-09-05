DROP DATABASE IF EXISTS une6d16_delete;
CREATE DATABASE une6d16_delete CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci;
USE une6d16_delete;

CREATE TABLE access_sessions (
  session_id BIGINT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
  user_email VARCHAR(160) NOT NULL,
  token_hash CHAR(64) NOT NULL UNIQUE,
  last_activity DATETIME NOT NULL,
  revoked BOOLEAN NOT NULL DEFAULT FALSE
) ENGINE=InnoDB;

CREATE TABLE deleted_sessions (
  archive_id BIGINT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
  original_session_id BIGINT UNSIGNED NOT NULL,
  user_email VARCHAR(160) NOT NULL,
  token_hash CHAR(64) NOT NULL,
  last_activity DATETIME NOT NULL,
  archived_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB;

INSERT INTO access_sessions (user_email, token_hash, last_activity, revoked) VALUES
('ana@example.com', SHA2('token-ana', 256), '2026-12-15 10:00:00', FALSE),
('luis@example.com', SHA2('token-luis', 256), '2026-10-01 08:00:00', TRUE),
('marta@example.com', SHA2('token-marta', 256), '2026-09-15 12:00:00', TRUE),
('carlos@example.com', SHA2('token-carlos', 256), '2026-12-14 16:30:00', FALSE);

SELECT session_id, user_email, last_activity, revoked
FROM access_sessions
WHERE revoked = TRUE
  AND last_activity < '2026-11-01';

START TRANSACTION;

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
FROM access_sessions
WHERE revoked = TRUE
  AND last_activity < '2026-11-01';

DELETE FROM access_sessions
WHERE revoked = TRUE
  AND last_activity < '2026-11-01';

SELECT ROW_COUNT() AS deleted_rows;

COMMIT;

SELECT * FROM access_sessions ORDER BY session_id;
SELECT * FROM deleted_sessions ORDER BY archive_id;
