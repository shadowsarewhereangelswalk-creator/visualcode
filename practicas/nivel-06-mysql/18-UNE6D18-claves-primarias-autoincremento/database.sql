CREATE DATABASE IF NOT EXISTS ai_career_tracker;
USE ai_career_tracker;

CREATE TABLE IF NOT EXISTS cursos (
  id INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
  nombre VARCHAR(120) NOT NULL
);

CREATE TABLE IF NOT EXISTS lecciones (
  id INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
  curso_id INT UNSIGNED NOT NULL,
  titulo VARCHAR(160) NOT NULL,
  CONSTRAINT fk_lecciones_curso FOREIGN KEY (curso_id) REFERENCES cursos(id)
);

INSERT INTO cursos(nombre) VALUES ('Programación Full Stack con Python e IA');
SET @curso_id = LAST_INSERT_ID();
INSERT INTO lecciones(curso_id,titulo) VALUES (@curso_id,'Claves primarias y autoincremento');

SELECT c.id,c.nombre,l.id AS leccion_id,l.titulo
FROM cursos c JOIN lecciones l ON l.curso_id=c.id;
