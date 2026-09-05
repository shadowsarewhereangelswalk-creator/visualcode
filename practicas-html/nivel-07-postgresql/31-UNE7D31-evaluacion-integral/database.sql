DROP SCHEMA IF EXISTS une7d31_evaluation CASCADE;
CREATE SCHEMA une7d31_evaluation;
SET search_path TO une7d31_evaluation, public;

CREATE TYPE task_status AS ENUM ('pending', 'in_progress', 'completed');

CREATE TABLE clients (
    client_id bigint GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    full_name text NOT NULL,
    email text NOT NULL UNIQUE,
    active boolean NOT NULL DEFAULT true
);

CREATE TABLE projects (
    project_id bigint GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    client_id bigint NOT NULL,
    project_name text NOT NULL,
    status text NOT NULL DEFAULT 'active'
        CHECK (status IN ('active', 'completed', 'cancelled')),
    budget numeric(12, 2) NOT NULL CHECK (budget >= 0),
    starts_on date NOT NULL,
    due_on date NOT NULL,
    CHECK (due_on >= starts_on),
    CONSTRAINT fk_evaluation_project_client
        FOREIGN KEY (client_id)
        REFERENCES clients(client_id)
        ON UPDATE CASCADE
        ON DELETE RESTRICT
);

CREATE TABLE tasks (
    task_id bigint GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    project_id bigint NOT NULL,
    task_name text NOT NULL,
    status task_status NOT NULL DEFAULT 'pending',
    progress smallint NOT NULL DEFAULT 0 CHECK (progress BETWEEN 0 AND 100),
    assigned_to text NOT NULL,
    due_on date NOT NULL,
    UNIQUE (project_id, task_name),
    CONSTRAINT fk_evaluation_task_project
        FOREIGN KEY (project_id)
        REFERENCES projects(project_id)
        ON UPDATE CASCADE
        ON DELETE CASCADE
);

CREATE TABLE task_history (
    history_id bigint GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    task_id bigint NOT NULL,
    previous_status task_status NOT NULL,
    new_status task_status NOT NULL,
    previous_progress smallint NOT NULL,
    new_progress smallint NOT NULL,
    changed_by text NOT NULL,
    changed_at timestamptz NOT NULL DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT fk_evaluation_history_task
        FOREIGN KEY (task_id)
        REFERENCES tasks(task_id)
        ON UPDATE CASCADE
        ON DELETE CASCADE
);

CREATE TABLE project_archive (
    archive_id bigint GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    original_project_id bigint NOT NULL,
    client_id bigint NOT NULL,
    project_name text NOT NULL,
    deleted_by text NOT NULL,
    deleted_at timestamptz NOT NULL DEFAULT CURRENT_TIMESTAMP
);

CREATE OR REPLACE FUNCTION validate_and_audit_task()
RETURNS trigger
LANGUAGE plpgsql
AS $function$
BEGIN
    IF NEW.status = 'completed' AND NEW.progress <> 100 THEN
        RAISE EXCEPTION 'Una tarea completada debe tener progreso de 100';
    END IF;

    IF NEW.status <> 'completed' AND NEW.progress = 100 THEN
        RAISE EXCEPTION 'Una tarea con progreso de 100 debe estar completada';
    END IF;

    IF OLD.status IS DISTINCT FROM NEW.status
       OR OLD.progress IS DISTINCT FROM NEW.progress THEN
        INSERT INTO task_history (
            task_id,
            previous_status,
            new_status,
            previous_progress,
            new_progress,
            changed_by
        )
        VALUES (
            NEW.task_id,
            OLD.status,
            NEW.status,
            OLD.progress,
            NEW.progress,
            current_user
        );
    END IF;

    RETURN NEW;
END;
$function$;

CREATE OR REPLACE FUNCTION complete_task(requested_task_id bigint)
RETURNS void
LANGUAGE plpgsql
AS $function$
BEGIN
    UPDATE tasks
    SET
        status = 'completed',
        progress = 100
    WHERE task_id = requested_task_id;

    IF NOT FOUND THEN
        RAISE EXCEPTION 'La tarea no existe';
    END IF;
END;
$function$;

CREATE TRIGGER trg_validate_and_audit_task
BEFORE UPDATE ON tasks
FOR EACH ROW
EXECUTE FUNCTION validate_and_audit_task();

CREATE RULE archive_deleted_project AS
ON DELETE TO projects
DO ALSO
INSERT INTO project_archive (
    original_project_id,
    client_id,
    project_name,
    deleted_by
)
VALUES (
    OLD.project_id,
    OLD.client_id,
    OLD.project_name,
    current_user
);

INSERT INTO clients (full_name, email)
VALUES
    ('Ana Torres', 'ana@example.com'),
    ('Bruno Díaz', 'bruno@example.com');

INSERT INTO projects (
    client_id,
    project_name,
    status,
    budget,
    starts_on,
    due_on
)
VALUES
    (1, 'Migración PostgreSQL', 'active', 18000.00, '2027-01-01', '2027-04-30'),
    (2, 'Proyecto temporal', 'active', 500.00, '2027-01-15', '2027-01-31');

INSERT INTO tasks (
    project_id,
    task_name,
    status,
    progress,
    assigned_to,
    due_on
)
VALUES
    (1, 'Diseñar modelo', 'completed', 100, 'Carla', '2027-01-15'),
    (1, 'Migrar datos', 'in_progress', 60, 'Diego', '2027-03-15'),
    (1, 'Validar resultados', 'pending', 0, 'Elena', '2027-04-15'),
    (2, 'Tarea temporal', 'pending', 0, 'Fabio', '2027-01-25');

SELECT complete_task(2);

DELETE FROM projects
WHERE project_id = 2;

CREATE VIEW project_progress AS
SELECT
    p.project_id,
    p.project_name,
    p.status,
    c.full_name AS client_name,
    COUNT(t.task_id) AS task_count,
    COUNT(t.task_id) FILTER (WHERE t.status = 'completed') AS completed_tasks,
    COALESCE(ROUND(AVG(t.progress), 2), 0) AS average_progress,
    p.budget,
    p.starts_on,
    p.due_on
FROM projects AS p
INNER JOIN clients AS c
    ON c.client_id = p.client_id
LEFT JOIN tasks AS t
    ON t.project_id = p.project_id
GROUP BY
    p.project_id,
    p.project_name,
    p.status,
    c.full_name,
    p.budget,
    p.starts_on,
    p.due_on;

SELECT *
FROM project_progress
ORDER BY project_id;

SELECT
    history_id,
    task_id,
    previous_status,
    new_status,
    previous_progress,
    new_progress,
    changed_by,
    changed_at
FROM task_history
ORDER BY history_id;

SELECT
    archive_id,
    original_project_id,
    client_id,
    project_name,
    deleted_by,
    deleted_at
FROM project_archive
ORDER BY archive_id;
