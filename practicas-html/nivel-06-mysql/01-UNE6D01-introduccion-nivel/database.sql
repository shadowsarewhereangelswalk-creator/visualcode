DROP DATABASE IF EXISTS une6d01_lab;
CREATE DATABASE une6d01_lab CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci;
USE une6d01_lab;

CREATE TABLE learning_goals (
  goal_id INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
  title VARCHAR(120) NOT NULL,
  category ENUM('Diseño','Consultas','Automatización','Integridad') NOT NULL,
  completed BOOLEAN NOT NULL DEFAULT FALSE,
  created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB;

INSERT INTO learning_goals (title, category) VALUES
('Diseñar tablas relacionadas', 'Diseño'),
('Construir consultas CRUD', 'Consultas'),
('Crear procedimientos y triggers', 'Automatización'),
('Aplicar transacciones seguras', 'Integridad');

SELECT goal_id, title, category, completed, created_at
FROM learning_goals
ORDER BY goal_id;
