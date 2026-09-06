DROP DATABASE IF EXISTS une6d24_enrollment;
CREATE DATABASE une6d24_enrollment CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci;
USE une6d24_enrollment;

CREATE TABLE students (
  student_id INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
  full_name VARCHAR(120) NOT NULL,
  email VARCHAR(160) NOT NULL UNIQUE
) ENGINE=InnoDB;

CREATE TABLE courses (
  course_id INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
  title VARCHAR(140) NOT NULL,
  capacity SMALLINT UNSIGNED NOT NULL,
  enrolled_count SMALLINT UNSIGNED NOT NULL DEFAULT 0
) ENGINE=InnoDB;

CREATE TABLE enrollments (
  enrollment_id BIGINT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
  student_id INT UNSIGNED NOT NULL,
  course_id INT UNSIGNED NOT NULL,
  enrolled_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
  UNIQUE KEY uk_student_course (student_id, course_id),
  CONSTRAINT fk_enrollment_student
    FOREIGN KEY (student_id) REFERENCES students(student_id)
    ON UPDATE CASCADE
    ON DELETE RESTRICT,
  CONSTRAINT fk_enrollment_course
    FOREIGN KEY (course_id) REFERENCES courses(course_id)
    ON UPDATE CASCADE
    ON DELETE RESTRICT
) ENGINE=InnoDB;

INSERT INTO students (full_name, email) VALUES
('Ana Pérez', 'ana@example.com'),
('Luis Gómez', 'luis@example.com');

INSERT INTO courses (title, capacity) VALUES
('MySQL aplicado', 3),
('JavaScript avanzado', 2);

DELIMITER $$

CREATE PROCEDURE enroll_student (
  IN p_student_id INT UNSIGNED,
  IN p_course_id INT UNSIGNED,
  OUT p_enrollment_id BIGINT UNSIGNED
)
BEGIN
  DECLARE v_capacity SMALLINT UNSIGNED DEFAULT NULL;
  DECLARE v_enrolled SMALLINT UNSIGNED DEFAULT 0;
  DECLARE EXIT HANDLER FOR SQLEXCEPTION
  BEGIN
    ROLLBACK;
    RESIGNAL;
  END;

  START TRANSACTION;

  SELECT capacity, enrolled_count
  INTO v_capacity, v_enrolled
  FROM courses
  WHERE course_id = p_course_id
  FOR UPDATE;

  IF v_capacity IS NULL THEN
    SIGNAL SQLSTATE '45000'
      SET MESSAGE_TEXT = 'El curso no existe';
  END IF;

  IF v_enrolled >= v_capacity THEN
    SIGNAL SQLSTATE '45000'
      SET MESSAGE_TEXT = 'El curso no tiene cupos disponibles';
  END IF;

  INSERT INTO enrollments (student_id, course_id)
  VALUES (p_student_id, p_course_id);

  SET p_enrollment_id = LAST_INSERT_ID();

  UPDATE courses
  SET enrolled_count = enrolled_count + 1
  WHERE course_id = p_course_id;

  COMMIT;
END$$

DELIMITER ;

CALL enroll_student(1, 1, @enrollment_id);
SELECT @enrollment_id AS new_enrollment_id;

SELECT
  e.enrollment_id,
  s.full_name AS student,
  c.title AS course,
  e.enrolled_at
FROM enrollments AS e
INNER JOIN students AS s ON s.student_id = e.student_id
INNER JOIN courses AS c ON c.course_id = e.course_id;
