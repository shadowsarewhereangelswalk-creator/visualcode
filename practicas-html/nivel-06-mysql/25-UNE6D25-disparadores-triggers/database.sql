DROP DATABASE IF EXISTS une6d25_triggers;
CREATE DATABASE une6d25_triggers
CHARACTER SET utf8mb4
COLLATE utf8mb4_0900_ai_ci;

USE une6d25_triggers;

CREATE TABLE employees (
    employee_id BIGINT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    full_name VARCHAR(120) NOT NULL,
    position_name VARCHAR(100) NOT NULL,
    salary DECIMAL(12, 2) NOT NULL,
    updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    CONSTRAINT chk_employee_salary CHECK (salary > 0)
) ENGINE = InnoDB;

CREATE TABLE salary_audit (
    audit_id BIGINT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    employee_id BIGINT UNSIGNED NOT NULL,
    previous_salary DECIMAL(12, 2) NOT NULL,
    new_salary DECIMAL(12, 2) NOT NULL,
    changed_by VARCHAR(288) NOT NULL,
    changed_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT fk_salary_audit_employee
        FOREIGN KEY (employee_id) REFERENCES employees(employee_id)
        ON UPDATE CASCADE
        ON DELETE RESTRICT
) ENGINE = InnoDB;

INSERT INTO employees (full_name, position_name, salary)
VALUES
    ('Ana Torres', 'Desarrolladora', 4200.00),
    ('Bruno Díaz', 'Analista de datos', 3900.00),
    ('Carla Méndez', 'Diseñadora UX', 3600.00);

DELIMITER $$

CREATE TRIGGER trg_employees_validate_salary
BEFORE UPDATE ON employees
FOR EACH ROW
BEGIN
    IF NEW.salary <= 0 THEN
        SIGNAL SQLSTATE '45000'
            SET MESSAGE_TEXT = 'El salario debe ser mayor que cero';
    END IF;
END$$

CREATE TRIGGER trg_employees_audit_salary
AFTER UPDATE ON employees
FOR EACH ROW
BEGIN
    IF NOT (OLD.salary <=> NEW.salary) THEN
        INSERT INTO salary_audit (
            employee_id,
            previous_salary,
            new_salary,
            changed_by
        )
        VALUES (
            NEW.employee_id,
            OLD.salary,
            NEW.salary,
            CURRENT_USER()
        );
    END IF;
END$$

DELIMITER ;

UPDATE employees
SET salary = 4550.00
WHERE employee_id = 1;

UPDATE employees
SET position_name = 'Analista de datos senior'
WHERE employee_id = 2;

SELECT
    employee_id,
    full_name,
    position_name,
    salary,
    updated_at
FROM employees
ORDER BY employee_id;

SELECT
    audit_id,
    employee_id,
    previous_salary,
    new_salary,
    changed_by,
    changed_at
FROM salary_audit
ORDER BY audit_id;
