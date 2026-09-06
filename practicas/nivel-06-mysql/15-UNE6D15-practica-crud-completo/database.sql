DROP DATABASE IF EXISTS une6d15_crud;
CREATE DATABASE une6d15_crud CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci;
USE une6d15_crud;

CREATE TABLE tasks (
  task_id INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
  title VARCHAR(160) NOT NULL,
  priority ENUM('Baja','Media','Alta') NOT NULL DEFAULT 'Media',
  status ENUM('Pendiente','En progreso','Completada') NOT NULL DEFAULT 'Pendiente',
  due_date DATE,
  created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
) ENGINE=InnoDB;

INSERT INTO tasks (title, priority, due_date) VALUES
('Diseñar el modelo relacional', 'Alta', '2026-12-10'),
('Cargar datos de prueba', 'Media', '2026-12-12'),
('Preparar consultas', 'Alta', '2026-12-14');

SELECT
  task_id,
  title,
  priority,
  status,
  due_date
FROM tasks
WHERE status <> 'Completada'
ORDER BY FIELD(priority, 'Alta', 'Media', 'Baja'), due_date;

UPDATE tasks
SET status = 'En progreso'
WHERE task_id = 1
  AND status = 'Pendiente';

UPDATE tasks
SET status = 'Completada'
WHERE task_id = 2;

INSERT INTO tasks (title, priority, due_date)
VALUES ('Registro temporal para eliminar', 'Baja', '2026-12-31');

SET @temporary_task_id = LAST_INSERT_ID();

DELETE FROM tasks
WHERE task_id = @temporary_task_id
  AND title = 'Registro temporal para eliminar';

SELECT
  task_id,
  title,
  priority,
  status,
  due_date,
  created_at,
  updated_at
FROM tasks
ORDER BY task_id;
