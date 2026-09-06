DROP SCHEMA IF EXISTS une7d08_psql_practice CASCADE;
CREATE SCHEMA une7d08_psql_practice;
SET search_path TO une7d08_psql_practice, public;

CREATE TABLE departments (
    department_id bigint GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    department_name text NOT NULL UNIQUE
);

CREATE TABLE employees (
    employee_id bigint GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    department_id bigint NOT NULL,
    full_name text NOT NULL,
    email text NOT NULL UNIQUE,
    salary numeric(10, 2) NOT NULL CHECK (salary > 0),
    hired_on date NOT NULL,
    CONSTRAINT fk_employee_department
        FOREIGN KEY (department_id)
        REFERENCES departments(department_id)
        ON UPDATE CASCADE
        ON DELETE RESTRICT
);

INSERT INTO departments (department_name)
VALUES ('Desarrollo'), ('Datos'), ('Diseño');

INSERT INTO employees (department_id, full_name, email, salary, hired_on)
VALUES
    (1, 'Ana Torres', 'ana@example.com', 4200.00, '2026-04-10'),
    (2, 'Bruno Díaz', 'bruno@example.com', 3900.00, '2026-06-15'),
    (1, 'Carla Méndez', 'carla@example.com', 4500.00, '2026-08-01'),
    (3, 'Diego Ruiz', 'diego@example.com', 3600.00, '2026-09-20');

SELECT e.employee_id, e.full_name, e.email, d.department_name, e.salary, e.hired_on
FROM employees AS e
INNER JOIN departments AS d ON d.department_id = e.department_id
ORDER BY d.department_name, e.full_name;
