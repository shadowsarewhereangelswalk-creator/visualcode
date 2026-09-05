DROP DATABASE IF EXISTS une6d21_integrity;
CREATE DATABASE une6d21_integrity CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci;
USE une6d21_integrity;

CREATE TABLE departments (
  department_id SMALLINT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
  name VARCHAR(100) NOT NULL UNIQUE
) ENGINE=InnoDB;

CREATE TABLE employees (
  employee_id INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
  department_id SMALLINT UNSIGNED,
  full_name VARCHAR(120) NOT NULL,
  email VARCHAR(160) NOT NULL UNIQUE,
  CONSTRAINT fk_employees_department
    FOREIGN KEY (department_id) REFERENCES departments(department_id)
    ON UPDATE CASCADE
    ON DELETE SET NULL
) ENGINE=InnoDB;

CREATE TABLE projects (
  project_id INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
  owner_id INT UNSIGNED NOT NULL,
  name VARCHAR(140) NOT NULL,
  CONSTRAINT fk_projects_owner
    FOREIGN KEY (owner_id) REFERENCES employees(employee_id)
    ON UPDATE CASCADE
    ON DELETE RESTRICT
) ENGINE=InnoDB;

CREATE TABLE project_members (
  project_id INT UNSIGNED NOT NULL,
  employee_id INT UNSIGNED NOT NULL,
  assigned_at DATE NOT NULL,
  PRIMARY KEY (project_id, employee_id),
  CONSTRAINT fk_members_project
    FOREIGN KEY (project_id) REFERENCES projects(project_id)
    ON UPDATE CASCADE
    ON DELETE CASCADE,
  CONSTRAINT fk_members_employee
    FOREIGN KEY (employee_id) REFERENCES employees(employee_id)
    ON UPDATE CASCADE
    ON DELETE CASCADE
) ENGINE=InnoDB;

INSERT INTO departments (name) VALUES
('Desarrollo'),
('Diseño');

INSERT INTO employees (department_id, full_name, email) VALUES
(1, 'Ana Pérez', 'ana@example.com'),
(1, 'Luis Gómez', 'luis@example.com'),
(2, 'Marta Díaz', 'marta@example.com');

INSERT INTO projects (owner_id, name) VALUES
(1, 'Portal de aprendizaje');

INSERT INTO project_members (project_id, employee_id, assigned_at) VALUES
(1, 1, '2026-12-01'),
(1, 2, '2026-12-02'),
(1, 3, '2026-12-03');

SELECT
  p.name AS project,
  owner.full_name AS owner,
  member.full_name AS member,
  d.name AS department
FROM projects AS p
INNER JOIN employees AS owner ON owner.employee_id = p.owner_id
INNER JOIN project_members AS pm ON pm.project_id = p.project_id
INNER JOIN employees AS member ON member.employee_id = pm.employee_id
LEFT JOIN departments AS d ON d.department_id = member.department_id
ORDER BY member.full_name;
