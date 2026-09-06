CREATE DATABASE IF NOT EXISTS practica_une6d19;
USE practica_une6d19;
DROP TABLE IF EXISTS tareas;
CREATE TABLE tareas (
  id INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
  titulo VARCHAR(120) NOT NULL,
  completada BOOLEAN NOT NULL DEFAULT FALSE
);
INSERT INTO tareas(titulo) VALUES ('Diseñar tabla'),('Insertar datos'),('Consultar identificadores');
SELECT id,titulo,completada FROM tareas ORDER BY id;
DELETE FROM tareas WHERE id=2;
INSERT INTO tareas(titulo) VALUES ('Nueva tarea');
SELECT id,titulo FROM tareas ORDER BY id;
