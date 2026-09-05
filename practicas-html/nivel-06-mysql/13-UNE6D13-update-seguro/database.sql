DROP DATABASE IF EXISTS une6d13_update;
CREATE DATABASE une6d13_update CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci;
USE une6d13_update;

CREATE TABLE employees (
  employee_id INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
  full_name VARCHAR(120) NOT NULL,
  department VARCHAR(80) NOT NULL,
  salary DECIMAL(10,2) NOT NULL CHECK (salary > 0),
  active BOOLEAN NOT NULL DEFAULT TRUE,
  updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
) ENGINE=InnoDB;

INSERT INTO employees (full_name, department, salary) VALUES
('Ana Pérez', 'Desarrollo', 3200.00),
('Luis Gómez', 'Soporte', 2500.00),
('Marta Díaz', 'Marketing', 2850.00),
('Carlos León', 'Desarrollo', 3500.00);

SELECT *
FROM employees
WHERE employee_id = 2;

START TRANSACTION;

UPDATE employees
SET department = 'Operaciones',
    salary = 2750.00
WHERE employee_id = 2
  AND active = TRUE;

SELECT ROW_COUNT() AS updated_rows;

COMMIT;

UPDATE employees
SET salary = ROUND(salary * 1.05, 2)
WHERE department = 'Desarrollo'
  AND active = TRUE;

SELECT
  employee_id,
  full_name,
  department,
  salary,
  active,
  updated_at
FROM employees
ORDER BY employee_id;
