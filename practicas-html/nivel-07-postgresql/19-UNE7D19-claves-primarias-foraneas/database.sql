DROP SCHEMA IF EXISTS une7d19_keys CASCADE;
CREATE SCHEMA une7d19_keys;
SET search_path TO une7d19_keys, public;

CREATE TABLE departments (
    department_id bigint GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    department_code varchar(10) NOT NULL UNIQUE,
    department_name text NOT NULL UNIQUE
);

CREATE TABLE employees (
    employee_id bigint GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    department_id bigint,
    employee_code varchar(12) NOT NULL UNIQUE,
    full_name text NOT NULL,
    email text NOT NULL UNIQUE,
    CONSTRAINT fk_key_employee_department
        FOREIGN KEY (department_id)
        REFERENCES departments(department_id)
        ON UPDATE CASCADE
        ON DELETE SET NULL
);

CREATE TABLE projects (
    project_id bigint GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    owner_id bigint NOT NULL,
    project_code varchar(12) NOT NULL UNIQUE,
    project_name text NOT NULL,
    CONSTRAINT fk_key_project_owner
        FOREIGN KEY (owner_id)
        REFERENCES employees(employee_id)
        ON UPDATE CASCADE
        ON DELETE RESTRICT
);

CREATE TABLE project_members (
    project_id bigint NOT NULL,
    employee_id bigint NOT NULL,
    assigned_on date NOT NULL DEFAULT CURRENT_DATE,
    member_role text NOT NULL,
    PRIMARY KEY (project_id, employee_id),
    CONSTRAINT fk_key_member_project
        FOREIGN KEY (project_id)
        REFERENCES projects(project_id)
        ON UPDATE CASCADE
        ON DELETE CASCADE,
    CONSTRAINT fk_key_member_employee
        FOREIGN KEY (employee_id)
        REFERENCES employees(employee_id)
        ON UPDATE CASCADE
        ON DELETE CASCADE
);

INSERT INTO departments (department_code, department_name)
VALUES
    ('DEV', 'Desarrollo'),
    ('DATA', 'Datos');

INSERT INTO employees (department_id, employee_code, full_name, email)
VALUES
    (1, 'EMP-0001', 'Ana Torres', 'ana@example.com'),
    (1, 'EMP-0002', 'Bruno Díaz', 'bruno@example.com'),
    (2, 'EMP-0003', 'Carla Méndez', 'carla@example.com');

INSERT INTO projects (owner_id, project_code, project_name)
VALUES (1, 'PRJ-PG-001', 'Migración PostgreSQL');

INSERT INTO project_members (project_id, employee_id, member_role)
VALUES
    (1, 1, 'Propietaria'),
    (1, 2, 'Desarrollador'),
    (1, 3, 'Especialista de datos');

SELECT
    p.project_code,
    p.project_name,
    owner.full_name AS owner_name,
    member.full_name AS member_name,
    pm.member_role,
    d.department_name
FROM projects AS p
INNER JOIN employees AS owner
    ON owner.employee_id = p.owner_id
INNER JOIN project_members AS pm
    ON pm.project_id = p.project_id
INNER JOIN employees AS member
    ON member.employee_id = pm.employee_id
LEFT JOIN departments AS d
    ON d.department_id = member.department_id
ORDER BY member.full_name;
