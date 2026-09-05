DROP DATABASE IF EXISTS une6d04_workspace;
CREATE DATABASE une6d04_workspace
  CHARACTER SET utf8mb4
  COLLATE utf8mb4_0900_ai_ci;

USE une6d04_workspace;

CREATE TABLE database_settings (
  setting_id INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
  setting_name VARCHAR(80) NOT NULL UNIQUE,
  setting_value VARCHAR(160) NOT NULL
) ENGINE=InnoDB;

INSERT INTO database_settings (setting_name, setting_value) VALUES
('project_name', 'Aplicación real'),
('environment', 'development'),
('charset', 'utf8mb4'),
('collation', 'utf8mb4_0900_ai_ci');

SELECT DATABASE() AS active_database;
SELECT
  DEFAULT_CHARACTER_SET_NAME AS character_set_name,
  DEFAULT_COLLATION_NAME AS collation_name
FROM information_schema.SCHEMATA
WHERE SCHEMA_NAME = 'une6d04_workspace';

SELECT setting_name, setting_value
FROM database_settings
ORDER BY setting_name;
