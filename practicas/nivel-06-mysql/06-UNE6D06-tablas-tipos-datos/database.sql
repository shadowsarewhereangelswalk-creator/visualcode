DROP DATABASE IF EXISTS une6d06_types;
CREATE DATABASE une6d06_types CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci;
USE une6d06_types;

CREATE TABLE professional_profiles (
  profile_id BIGINT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
  username VARCHAR(60) NOT NULL UNIQUE,
  full_name VARCHAR(140) NOT NULL,
  biography TEXT,
  birth_date DATE,
  years_experience TINYINT UNSIGNED NOT NULL DEFAULT 0,
  hourly_rate DECIMAL(10,2) NOT NULL DEFAULT 0.00,
  rating DECIMAL(3,2) CHECK (rating BETWEEN 0 AND 5),
  available BOOLEAN NOT NULL DEFAULT TRUE,
  specialty ENUM('Frontend','Backend','Datos','Automatización') NOT NULL,
  skills JSON NOT NULL,
  last_access DATETIME,
  created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB;

INSERT INTO professional_profiles (
  username,
  full_name,
  biography,
  birth_date,
  years_experience,
  hourly_rate,
  rating,
  available,
  specialty,
  skills,
  last_access
) VALUES (
  'karen.dev',
  'Karen Agostini',
  'Profesional enfocada en proyectos digitales.',
  '1990-05-15',
  5,
  35.00,
  4.85,
  TRUE,
  'Frontend',
  JSON_ARRAY('HTML', 'CSS', 'JavaScript', 'MySQL'),
  NOW()
);

DESCRIBE professional_profiles;

SELECT
  username,
  full_name,
  years_experience,
  hourly_rate,
  rating,
  available,
  specialty,
  JSON_LENGTH(skills) AS skill_count,
  created_at
FROM professional_profiles;
