DROP SCHEMA IF EXISTS une7d12_academy CASCADE;
CREATE SCHEMA une7d12_academy;
SET search_path TO une7d12_academy, public;

CREATE TABLE instructors (
    instructor_id bigint GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    full_name text NOT NULL,
    email text NOT NULL UNIQUE
);

CREATE TABLE courses (
    course_id bigint GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    instructor_id bigint NOT NULL,
    course_code varchar(12) NOT NULL UNIQUE,
    title text NOT NULL,
    capacity integer NOT NULL CHECK (capacity > 0),
    published boolean NOT NULL DEFAULT false,
    CONSTRAINT fk_course_instructor
        FOREIGN KEY (instructor_id)
        REFERENCES instructors(instructor_id)
        ON UPDATE CASCADE
        ON DELETE RESTRICT
);

CREATE TABLE lessons (
    lesson_id bigint GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    course_id bigint NOT NULL,
    lesson_number integer NOT NULL CHECK (lesson_number > 0),
    title text NOT NULL,
    duration_minutes integer NOT NULL CHECK (duration_minutes > 0),
    UNIQUE (course_id, lesson_number),
    CONSTRAINT fk_lesson_course
        FOREIGN KEY (course_id)
        REFERENCES courses(course_id)
        ON UPDATE CASCADE
        ON DELETE CASCADE
);

INSERT INTO instructors (full_name, email)
VALUES ('Elena Torres', 'elena@example.com');

INSERT INTO courses (instructor_id, course_code, title, capacity, published)
VALUES (1, 'PG-N7-001', 'PostgreSQL Aplicado', 25, true);

INSERT INTO lessons (course_id, lesson_number, title, duration_minutes)
VALUES (1, 1, 'Modelo Entidad-Relación', 90), (1, 2, 'Tipos de datos', 90), (1, 3, 'Consultas CRUD', 120);

SELECT
    c.course_code, c.title AS course_title, i.full_name AS instructor_name,
    COUNT(l.lesson_id) AS lesson_count, SUM(l.duration_minutes) AS total_minutes
FROM courses AS c
INNER JOIN instructors AS i ON i.instructor_id = c.instructor_id
LEFT JOIN lessons AS l ON l.course_id = c.course_id
GROUP BY c.course_id, c.course_code, c.title, i.full_name
ORDER BY c.course_code;
