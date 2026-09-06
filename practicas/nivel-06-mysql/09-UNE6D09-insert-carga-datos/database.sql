DROP DATABASE IF EXISTS une6d09_insert;
CREATE DATABASE une6d09_insert CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci;
USE une6d09_insert;

CREATE TABLE contacts (
  contact_id INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
  full_name VARCHAR(120) NOT NULL,
  email VARCHAR(160) NOT NULL UNIQUE,
  phone VARCHAR(30),
  city VARCHAR(80) NOT NULL,
  active BOOLEAN NOT NULL DEFAULT TRUE,
  created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB;

INSERT INTO contacts (full_name, email, phone, city)
VALUES ('Ana Pérez', 'ana@example.com', '+1 305 555 0101', 'Miami');

INSERT INTO contacts
SET full_name = 'Luis Gómez',
    email = 'luis@example.com',
    phone = '+1 305 555 0102',
    city = 'Doral';

INSERT INTO contacts (full_name, email, phone, city, active) VALUES
('Marta Díaz', 'marta@example.com', NULL, 'Tampa', TRUE),
('Carlos León', 'carlos@example.com', '+1 813 555 0104', 'Tampa', TRUE),
('Elena Ruiz', 'elena@example.com', '+1 786 555 0105', 'Miami', FALSE);

SELECT
  contact_id,
  full_name,
  email,
  phone,
  city,
  active,
  created_at
FROM contacts
ORDER BY contact_id;
