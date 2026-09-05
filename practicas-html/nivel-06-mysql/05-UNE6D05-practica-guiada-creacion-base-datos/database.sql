DROP DATABASE IF EXISTS une6d05_academy;
CREATE DATABASE une6d05_academy CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci;
USE une6d05_academy;

CREATE TABLE system_modules (
  module_id INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
  module_code CHAR(6) NOT NULL UNIQUE,
  module_name VARCHAR(120) NOT NULL,
  enabled BOOLEAN NOT NULL DEFAULT TRUE,
  created_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB;

CREATE TABLE system_events (
  event_id BIGINT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
  module_id INT UNSIGNED NOT NULL,
  event_name VARCHAR(120) NOT NULL,
  event_payload JSON,
  occurred_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
  CONSTRAINT fk_events_modules
    FOREIGN KEY (module_id) REFERENCES system_modules(module_id)
    ON UPDATE CASCADE
    ON DELETE CASCADE
) ENGINE=InnoDB;

INSERT INTO system_modules (module_code, module_name) VALUES
('AUTH01', 'Autenticación'),
('COUR01', 'Cursos'),
('PROG01', 'Progreso');

INSERT INTO system_events (module_id, event_name, event_payload) VALUES
(1, 'user_login', JSON_OBJECT('user_id', 101, 'success', TRUE)),
(2, 'course_opened', JSON_OBJECT('course_id', 5)),
(3, 'lesson_completed', JSON_OBJECT('lesson_id', 18, 'score', 95));

SHOW TABLES;

SELECT
  m.module_code,
  m.module_name,
  e.event_name,
  e.event_payload,
  e.occurred_at
FROM system_modules AS m
INNER JOIN system_events AS e ON e.module_id = m.module_id
ORDER BY e.occurred_at;
