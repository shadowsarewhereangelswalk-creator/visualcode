DROP SCHEMA IF EXISTS une7d22_course_cascade CASCADE;
CREATE SCHEMA une7d22_course_cascade;
SET search_path TO une7d22_course_cascade, public;

CREATE TABLE instructors (
    instructor_id bigint GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    full_name text NOT NULL,
    email text NOT NULL UNIQUE
);

CREATE TABLE courses (
    course_id bigint GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    instructor_id bigint,
    course_code varchar(15) NOT NULL UNIQUE,
    title text NOT NULL,
    CONSTRAINT fk_course_cascade_instructor
        FOREIGN KEY (instructor_id)
        REFERENCES instructors(instructor_id)
        ON UPDATE CASCADE
        ON DELETE SET NULL
);

CREATE TABLE lessons (
    lesson_id bigint GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    course_id bigint NOT NULL,
    lesson_number integer NOT NULL CHECK (lesson_number > 0),
    title text NOT NULL,
    UNIQUE (course_id, lesson_number),
    CONSTRAINT fk_lesson_cascade_course
        FOREIGN KEY (course_id)
        REFERENCES courses(course_id)
        ON UPDATE CASCADE
        ON DELETE CASCADE
);

CREATE TABLE lesson_resources (
    resource_id bigint GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    lesson_id bigint NOT NULL,
    resource_name text NOT NULL,
    resource_url text NOT NULL,
    CONSTRAINT fk_resource_cascade_lesson
        FOREIGN KEY (lesson_id)
        REFERENCES lessons(lesson_id)
        ON UPDATE CASCADE
        ON DELETE CASCADE
);

INSERT INTO instructors (full_name, email)
VALUES ('Elena Torres', 'elena@example.com');

INSERT INTO courses (instructor_id, course_code, title)
VALUES
    (1, 'PG-N7', 'PostgreSQL Aplicado'),
    (1, 'TEMP-N7', 'Curso temporal');

INSERT INTO lessons (course_id, lesson_number, title)
VALUES
    (1, 1, 'Tipos de datos'),
    (1, 2, 'Integridad referencial'),
    (2, 1, 'Lección temporal');

INSERT INTO lesson_resources (lesson_id, resource_name, resource_url)
VALUES
    (1, 'Referencia de tipos', 'https://www.postgresql.org/docs/current/datatype.html'),
    (2, 'Referencia de restricciones', 'https://www.postgresql.org/docs/current/ddl-constraints.html'),
    (3, 'Recurso temporal', 'https://example.com/temporary');

DELETE FROM courses
WHERE course_code = 'TEMP-N7'
RETURNING course_id, course_code;

DELETE FROM instructors
WHERE instructor_id = 1
RETURNING instructor_id, full_name;

SELECT
    c.course_code,
    c.title,
    c.instructor_id,
    COUNT(DISTINCT l.lesson_id) AS lesson_count,
    COUNT(r.resource_id) AS resource_count
FROM courses AS c
LEFT JOIN lessons AS l
    ON l.course_id = c.course_id
LEFT JOIN lesson_resources AS r
    ON r.lesson_id = l.lesson_id
GROUP BY
    c.course_id,
    c.course_code,
    c.title,
    c.instructor_id
ORDER BY c.course_code;
