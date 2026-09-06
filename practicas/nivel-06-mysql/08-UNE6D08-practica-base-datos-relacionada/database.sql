DROP DATABASE IF EXISTS une6d08_learning;
CREATE DATABASE une6d08_learning CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci;
USE une6d08_learning;

CREATE TABLE users (
  user_id INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
  full_name VARCHAR(140) NOT NULL,
  email VARCHAR(160) NOT NULL UNIQUE,
  role ENUM('Estudiante','Instructor','Administrador') NOT NULL DEFAULT 'Estudiante',
  active BOOLEAN NOT NULL DEFAULT TRUE,
  created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB;

CREATE TABLE courses (
  course_id INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
  instructor_id INT UNSIGNED NOT NULL,
  title VARCHAR(160) NOT NULL,
  description TEXT,
  price DECIMAL(10,2) NOT NULL DEFAULT 0.00 CHECK (price >= 0),
  published BOOLEAN NOT NULL DEFAULT FALSE,
  CONSTRAINT fk_courses_instructor
    FOREIGN KEY (instructor_id) REFERENCES users(user_id)
    ON UPDATE CASCADE
    ON DELETE RESTRICT
) ENGINE=InnoDB;

CREATE TABLE lessons (
  lesson_id INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
  course_id INT UNSIGNED NOT NULL,
  lesson_number SMALLINT UNSIGNED NOT NULL,
  title VARCHAR(160) NOT NULL,
  duration_minutes SMALLINT UNSIGNED NOT NULL,
  UNIQUE KEY uk_lesson_number (course_id, lesson_number),
  CONSTRAINT fk_lessons_course
    FOREIGN KEY (course_id) REFERENCES courses(course_id)
    ON UPDATE CASCADE
    ON DELETE CASCADE
) ENGINE=InnoDB;

CREATE TABLE enrollments (
  enrollment_id BIGINT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
  student_id INT UNSIGNED NOT NULL,
  course_id INT UNSIGNED NOT NULL,
  enrolled_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
  progress DECIMAL(5,2) NOT NULL DEFAULT 0.00 CHECK (progress BETWEEN 0 AND 100),
  status ENUM('Activo','Completado','Cancelado') NOT NULL DEFAULT 'Activo',
  UNIQUE KEY uk_student_course (student_id, course_id),
  CONSTRAINT fk_enrollments_student
    FOREIGN KEY (student_id) REFERENCES users(user_id)
    ON UPDATE CASCADE
    ON DELETE RESTRICT,
  CONSTRAINT fk_enrollments_course
    FOREIGN KEY (course_id) REFERENCES courses(course_id)
    ON UPDATE CASCADE
    ON DELETE RESTRICT
) ENGINE=InnoDB;

INSERT INTO users (full_name, email, role) VALUES
('Laura Méndez', 'laura@example.com', 'Instructor'),
('Ana Pérez', 'ana@example.com', 'Estudiante'),
('Luis Gómez', 'luis@example.com', 'Estudiante');

INSERT INTO courses (instructor_id, title, description, price, published) VALUES
(1, 'MySQL aplicado', 'Base de datos para una aplicación real.', 120.00, TRUE);

INSERT INTO lessons (course_id, lesson_number, title, duration_minutes) VALUES
(1, 1, 'Modelo relacional', 90),
(1, 2, 'Creación de tablas', 90),
(1, 3, 'Consultas CRUD', 90);

INSERT INTO enrollments (student_id, course_id, progress) VALUES
(2, 1, 66.67),
(3, 1, 33.33);

SELECT
  e.enrollment_id,
  u.full_name AS student,
  c.title AS course,
  i.full_name AS instructor,
  e.progress,
  e.status,
  COUNT(l.lesson_id) AS lesson_count
FROM enrollments AS e
INNER JOIN users AS u ON u.user_id = e.student_id
INNER JOIN courses AS c ON c.course_id = e.course_id
INNER JOIN users AS i ON i.user_id = c.instructor_id
LEFT JOIN lessons AS l ON l.course_id = c.course_id
GROUP BY e.enrollment_id, u.full_name, c.title, i.full_name, e.progress, e.status
ORDER BY e.enrollment_id;
