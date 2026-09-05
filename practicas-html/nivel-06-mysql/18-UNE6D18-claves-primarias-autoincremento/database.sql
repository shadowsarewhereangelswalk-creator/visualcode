DROP DATABASE IF EXISTS une6d18_primary_keys;
CREATE DATABASE une6d18_primary_keys
CHARACTER SET utf8mb4
COLLATE utf8mb4_0900_ai_ci;

USE une6d18_primary_keys;

CREATE TABLE support_tickets (
    ticket_id BIGINT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    public_code VARCHAR(20) NOT NULL UNIQUE,
    requester_email VARCHAR(160) NOT NULL,
    subject VARCHAR(180) NOT NULL,
    priority ENUM('low', 'medium', 'high') NOT NULL DEFAULT 'medium',
    status ENUM('open', 'in_progress', 'closed') NOT NULL DEFAULT 'open',
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
) ENGINE = InnoDB AUTO_INCREMENT = 1001;

INSERT INTO support_tickets (public_code, requester_email, subject, priority)
VALUES
    ('TKT-1001', 'ana@example.com', 'No puedo iniciar sesión', 'high'),
    ('TKT-1002', 'bruno@example.com', 'Actualizar datos de perfil', 'low'),
    ('TKT-1003', 'carla@example.com', 'Error al procesar el pago', 'high');

INSERT INTO support_tickets (public_code, requester_email, subject)
VALUES ('TKT-1004', 'diego@example.com', 'Consulta sobre mi suscripción');

SELECT
    ticket_id,
    public_code,
    requester_email,
    subject,
    priority,
    status,
    created_at
FROM support_tickets
ORDER BY ticket_id;

SELECT AUTO_INCREMENT
FROM information_schema.TABLES
WHERE TABLE_SCHEMA = 'une6d18_primary_keys'
  AND TABLE_NAME = 'support_tickets';
