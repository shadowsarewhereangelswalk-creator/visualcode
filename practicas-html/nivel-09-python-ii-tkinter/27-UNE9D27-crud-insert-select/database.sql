CREATE DATABASE IF NOT EXISTS ai_career CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
USE ai_career;

CREATE TABLE IF NOT EXISTS clientes (
    id INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(120) NOT NULL,
    correo VARCHAR(160) NOT NULL UNIQUE,
    telefono VARCHAR(30) NOT NULL,
    servicio VARCHAR(100) NOT NULL,
    activo BOOLEAN NOT NULL DEFAULT TRUE,
    creado_en TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    actualizado_en TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
) ENGINE = InnoDB;

INSERT IGNORE INTO clientes (nombre, correo, telefono, servicio)
VALUES
    ('Ana Torres', 'ana@ejemplo.com', '+58 412-555-0198', 'Automatización'),
    ('Luis Pérez', 'luis@ejemplo.com', '+1 305-555-0124', 'Landing page');
