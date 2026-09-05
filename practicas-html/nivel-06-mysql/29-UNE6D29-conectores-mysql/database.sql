DROP DATABASE IF EXISTS une6d29_connectors;
CREATE DATABASE une6d29_connectors
CHARACTER SET utf8mb4
COLLATE utf8mb4_0900_ai_ci;

USE une6d29_connectors;

CREATE TABLE contacts (
    contact_id BIGINT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    full_name VARCHAR(120) NOT NULL,
    email VARCHAR(160) NOT NULL UNIQUE,
    city VARCHAR(100) NOT NULL,
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
) ENGINE = InnoDB;

INSERT INTO contacts (full_name, email, city)
VALUES
    ('Ana Torres', 'ana@example.com', 'Bogotá'),
    ('Bruno Díaz', 'bruno@example.com', 'Medellín'),
    ('Carla Méndez', 'carla@example.com', 'Cali');

SELECT
    contact_id,
    full_name,
    email,
    city,
    created_at
FROM contacts
ORDER BY contact_id;
