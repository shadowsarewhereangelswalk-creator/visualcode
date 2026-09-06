DROP SCHEMA IF EXISTS une7d18_crud_cascade CASCADE;
CREATE SCHEMA une7d18_crud_cascade;
SET search_path TO une7d18_crud_cascade, public;

CREATE TABLE teams (
    team_id bigint GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    team_name text NOT NULL UNIQUE
);

CREATE TABLE projects (
    project_id bigint GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    team_id bigint NOT NULL,
    project_name text NOT NULL,
    status text NOT NULL DEFAULT 'active'
        CHECK (status IN ('active', 'completed', 'cancelled')),
    CONSTRAINT fk_crud_project_team
        FOREIGN KEY (team_id)
        REFERENCES teams(team_id)
        ON UPDATE CASCADE
        ON DELETE RESTRICT
);

CREATE TABLE tasks (
    task_id bigint GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    project_id bigint NOT NULL,
    task_name text NOT NULL,
    status text NOT NULL DEFAULT 'pending'
        CHECK (status IN ('pending', 'in_progress', 'completed')),
    priority smallint NOT NULL DEFAULT 2 CHECK (priority BETWEEN 1 AND 3),
    UNIQUE (project_id, task_name),
    CONSTRAINT fk_crud_task_project
        FOREIGN KEY (project_id)
        REFERENCES projects(project_id)
        ON UPDATE CASCADE
        ON DELETE CASCADE
);

CREATE TABLE task_notes (
    note_id bigint GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    task_id bigint NOT NULL,
    note_text text NOT NULL,
    created_at timestamptz NOT NULL DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT fk_crud_note_task
        FOREIGN KEY (task_id)
        REFERENCES tasks(task_id)
        ON UPDATE CASCADE
        ON DELETE CASCADE
);

INSERT INTO teams (team_name)
VALUES ('Equipo PostgreSQL');

INSERT INTO projects (team_id, project_name)
VALUES
    (1, 'Migración principal'),
    (1, 'Proyecto temporal');

INSERT INTO tasks (project_id, task_name, status, priority)
VALUES
    (1, 'Diseñar esquema', 'completed', 1),
    (1, 'Migrar datos', 'in_progress', 1),
    (2, 'Tarea temporal', 'pending', 3);

INSERT INTO task_notes (task_id, note_text)
VALUES
    (1, 'Modelo revisado y aprobado'),
    (2, 'Carga de prueba en curso'),
    (3, 'Este registro debe desaparecer por CASCADE');

SELECT
    p.project_name,
    t.task_id,
    t.task_name,
    t.status,
    COUNT(n.note_id) AS note_count
FROM projects AS p
INNER JOIN tasks AS t
    ON t.project_id = p.project_id
LEFT JOIN task_notes AS n
    ON n.task_id = t.task_id
GROUP BY
    p.project_id,
    p.project_name,
    t.task_id,
    t.task_name,
    t.status
ORDER BY p.project_name, t.task_id;

UPDATE tasks
SET status = 'completed'
WHERE task_id = 2
  AND status = 'in_progress'
RETURNING task_id, task_name, status;

DELETE FROM projects
WHERE project_id = 2
  AND project_name = 'Proyecto temporal'
RETURNING project_id, project_name;

SELECT
    (SELECT COUNT(*) FROM projects) AS projects_remaining,
    (SELECT COUNT(*) FROM tasks) AS tasks_remaining,
    (SELECT COUNT(*) FROM task_notes) AS notes_remaining;
