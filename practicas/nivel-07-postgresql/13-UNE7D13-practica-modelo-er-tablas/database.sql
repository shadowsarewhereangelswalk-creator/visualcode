DROP SCHEMA IF EXISTS une7d13_project_model CASCADE;
CREATE SCHEMA une7d13_project_model;
SET search_path TO une7d13_project_model, public;

CREATE TABLE clients (
    client_id bigint GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    full_name text NOT NULL,
    email text NOT NULL UNIQUE,
    company_name text
);

CREATE TABLE team_members (
    member_id bigint GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    full_name text NOT NULL,
    email text NOT NULL UNIQUE,
    specialty text NOT NULL
);

CREATE TABLE projects (
    project_id bigint GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    client_id bigint NOT NULL,
    project_name text NOT NULL,
    status text NOT NULL DEFAULT 'planned' CHECK (status IN ('planned', 'active', 'completed', 'cancelled')),
    budget numeric(12, 2) NOT NULL CHECK (budget >= 0),
    starts_on date NOT NULL,
    due_on date NOT NULL,
    CHECK (due_on >= starts_on),
    CONSTRAINT fk_project_client FOREIGN KEY (client_id) REFERENCES clients(client_id) ON UPDATE CASCADE ON DELETE RESTRICT
);

CREATE TABLE project_members (
    project_id bigint NOT NULL,
    member_id bigint NOT NULL,
    project_role text NOT NULL,
    assigned_on date NOT NULL DEFAULT CURRENT_DATE,
    PRIMARY KEY (project_id, member_id),
    CONSTRAINT fk_project_members_project FOREIGN KEY (project_id) REFERENCES projects(project_id) ON UPDATE CASCADE ON DELETE CASCADE,
    CONSTRAINT fk_project_members_member FOREIGN KEY (member_id) REFERENCES team_members(member_id) ON UPDATE CASCADE ON DELETE RESTRICT
);

CREATE TABLE tasks (
    task_id bigint GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    project_id bigint NOT NULL,
    assigned_member_id bigint,
    task_name text NOT NULL,
    status text NOT NULL DEFAULT 'pending' CHECK (status IN ('pending', 'in_progress', 'completed')),
    due_on date NOT NULL,
    UNIQUE (project_id, task_name),
    CONSTRAINT fk_task_project FOREIGN KEY (project_id) REFERENCES projects(project_id) ON UPDATE CASCADE ON DELETE CASCADE,
    CONSTRAINT fk_task_member FOREIGN KEY (assigned_member_id) REFERENCES team_members(member_id) ON UPDATE CASCADE ON DELETE SET NULL
);

INSERT INTO clients (full_name, email, company_name)
VALUES ('Ana Torres', 'ana@example.com', 'Horizonte Digital');

INSERT INTO team_members (full_name, email, specialty)
VALUES ('Bruno Díaz', 'bruno@example.com', 'Backend'), ('Carla Méndez', 'carla@example.com', 'Datos');

INSERT INTO projects (client_id, project_name, status, budget, starts_on, due_on)
VALUES (1, 'Migración PostgreSQL', 'active', 15000.00, '2027-01-10', '2027-04-30');

INSERT INTO project_members (project_id, member_id, project_role)
VALUES (1, 1, 'Líder técnico'), (1, 2, 'Especialista de datos');

INSERT INTO tasks (project_id, assigned_member_id, task_name, status, due_on)
VALUES
    (1, 2, 'Diseñar esquema objetivo', 'completed', '2027-01-31'),
    (1, 1, 'Construir migración', 'in_progress', '2027-03-15'),
    (1, NULL, 'Validar resultados', 'pending', '2027-04-15');

SELECT
    p.project_name, c.company_name, tm.full_name AS team_member, pm.project_role,
    COUNT(t.task_id) AS assigned_tasks
FROM projects AS p
INNER JOIN clients AS c ON c.client_id = p.client_id
INNER JOIN project_members AS pm ON pm.project_id = p.project_id
INNER JOIN team_members AS tm ON tm.member_id = pm.member_id
LEFT JOIN tasks AS t ON t.project_id = p.project_id AND t.assigned_member_id = tm.member_id
GROUP BY p.project_id, p.project_name, c.company_name, tm.member_id, tm.full_name, pm.project_role
ORDER BY tm.full_name;
