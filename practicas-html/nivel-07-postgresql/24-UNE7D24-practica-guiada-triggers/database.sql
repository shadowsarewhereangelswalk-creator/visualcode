DROP SCHEMA IF EXISTS une7d24_employee_triggers CASCADE;
CREATE SCHEMA une7d24_employee_triggers;
SET search_path TO une7d24_employee_triggers, public;

CREATE TABLE employees (
    employee_id bigint GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    full_name text NOT NULL,
    email text NOT NULL UNIQUE,
    position_name text NOT NULL,
    salary numeric(12, 2) NOT NULL CHECK (salary > 0),
    updated_at timestamptz NOT NULL DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE salary_history (
    history_id bigint GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    employee_id bigint NOT NULL,
    previous_salary numeric(12, 2) NOT NULL,
    new_salary numeric(12, 2) NOT NULL,
    changed_by text NOT NULL,
    changed_at timestamptz NOT NULL DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT fk_salary_history_employee
        FOREIGN KEY (employee_id)
        REFERENCES employees(employee_id)
        ON UPDATE CASCADE
        ON DELETE CASCADE
);

CREATE OR REPLACE FUNCTION prepare_employee_row()
RETURNS trigger
LANGUAGE plpgsql
AS $function$
BEGIN
    NEW.full_name := btrim(NEW.full_name);
    NEW.email := lower(btrim(NEW.email));
    NEW.updated_at := CURRENT_TIMESTAMP;

    IF NEW.salary <= 0 THEN
        RAISE EXCEPTION 'El salario debe ser mayor que cero';
    END IF;

    RETURN NEW;
END;
$function$;

CREATE OR REPLACE FUNCTION record_salary_change()
RETURNS trigger
LANGUAGE plpgsql
AS $function$
BEGIN
    INSERT INTO salary_history (
        employee_id,
        previous_salary,
        new_salary,
        changed_by
    )
    VALUES (
        NEW.employee_id,
        OLD.salary,
        NEW.salary,
        current_user
    );

    RETURN NEW;
END;
$function$;

CREATE TRIGGER trg_employees_prepare
BEFORE INSERT OR UPDATE ON employees
FOR EACH ROW
EXECUTE FUNCTION prepare_employee_row();

CREATE TRIGGER trg_employees_salary_history
AFTER UPDATE OF salary ON employees
FOR EACH ROW
WHEN (OLD.salary IS DISTINCT FROM NEW.salary)
EXECUTE FUNCTION record_salary_change();

INSERT INTO employees (full_name, email, position_name, salary)
VALUES
    ('  Ana Torres  ', 'ANA@EXAMPLE.COM', 'Desarrolladora', 4200.00),
    ('Bruno Díaz', 'BRUNO@EXAMPLE.COM', 'Analista de datos', 3900.00);

UPDATE employees
SET
    salary = 4550.00,
    position_name = 'Desarrolladora senior'
WHERE employee_id = 1;

SELECT
    employee_id,
    full_name,
    email,
    position_name,
    salary,
    updated_at
FROM employees
ORDER BY employee_id;

SELECT
    history_id,
    employee_id,
    previous_salary,
    new_salary,
    changed_by,
    changed_at
FROM salary_history
ORDER BY history_id;
