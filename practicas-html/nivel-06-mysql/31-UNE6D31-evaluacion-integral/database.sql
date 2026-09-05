DROP DATABASE IF EXISTS une6d31_evaluation;
CREATE DATABASE une6d31_evaluation
CHARACTER SET utf8mb4
COLLATE utf8mb4_0900_ai_ci;

USE une6d31_evaluation;

CREATE TABLE clients (
    client_id BIGINT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    full_name VARCHAR(120) NOT NULL,
    email VARCHAR(160) NOT NULL UNIQUE,
    active BOOLEAN NOT NULL DEFAULT TRUE
) ENGINE = InnoDB;

CREATE TABLE projects (
    project_id BIGINT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    client_id BIGINT UNSIGNED NOT NULL,
    project_name VARCHAR(150) NOT NULL,
    status ENUM('planned', 'active', 'completed', 'cancelled') NOT NULL DEFAULT 'planned',
    budget DECIMAL(12, 2) NOT NULL,
    start_date DATE NOT NULL,
    due_date DATE NOT NULL,
    CONSTRAINT chk_evaluation_budget CHECK (budget >= 0),
    CONSTRAINT chk_evaluation_dates CHECK (due_date >= start_date),
    CONSTRAINT fk_evaluation_project_client
        FOREIGN KEY (client_id) REFERENCES clients(client_id)
        ON UPDATE CASCADE
        ON DELETE RESTRICT
) ENGINE = InnoDB;

CREATE TABLE tasks (
    task_id BIGINT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    project_id BIGINT UNSIGNED NOT NULL,
    task_name VARCHAR(160) NOT NULL,
    status ENUM('pending', 'in_progress', 'completed') NOT NULL DEFAULT 'pending',
    progress TINYINT UNSIGNED NOT NULL DEFAULT 0,
    assigned_to VARCHAR(120) NOT NULL,
    due_date DATE NOT NULL,
    CONSTRAINT uq_evaluation_project_task UNIQUE (project_id, task_name),
    CONSTRAINT chk_evaluation_progress CHECK (progress <= 100),
    CONSTRAINT fk_evaluation_task_project
        FOREIGN KEY (project_id) REFERENCES projects(project_id)
        ON UPDATE CASCADE
        ON DELETE CASCADE
) ENGINE = InnoDB;

CREATE TABLE task_history (
    history_id BIGINT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    task_id BIGINT UNSIGNED NOT NULL,
    previous_status VARCHAR(20) NOT NULL,
    new_status VARCHAR(20) NOT NULL,
    previous_progress TINYINT UNSIGNED NOT NULL,
    new_progress TINYINT UNSIGNED NOT NULL,
    changed_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    changed_by VARCHAR(288) NOT NULL,
    CONSTRAINT fk_evaluation_history_task
        FOREIGN KEY (task_id) REFERENCES tasks(task_id)
        ON UPDATE CASCADE
        ON DELETE CASCADE
) ENGINE = InnoDB;

INSERT INTO clients (full_name, email)
VALUES
    ('Ana Torres', 'ana@example.com'),
    ('Bruno Díaz', 'bruno@example.com');

INSERT INTO projects (
    client_id,
    project_name,
    status,
    budget,
    start_date,
    due_date
)
VALUES
    (1, 'Portal de aprendizaje', 'active', 18000.00, '2026-08-01', '2026-11-30'),
    (2, 'Panel de ventas', 'active', 12500.00, '2026-08-15', '2026-10-31');

INSERT INTO tasks (
    project_id,
    task_name,
    status,
    progress,
    assigned_to,
    due_date
)
VALUES
    (1, 'Diseñar base de datos', 'completed', 100, 'Carla', '2026-08-15'),
    (1, 'Crear API', 'in_progress', 60, 'Diego', '2026-09-30'),
    (1, 'Construir interfaz', 'pending', 0, 'Elena', '2026-10-31'),
    (2, 'Modelar indicadores', 'in_progress', 40, 'Fabio', '2026-09-20'),
    (2, 'Crear visualizaciones', 'pending', 0, 'Gabriela', '2026-10-15');

DELIMITER $$

CREATE TRIGGER trg_evaluation_task_consistency
BEFORE UPDATE ON tasks
FOR EACH ROW
BEGIN
    IF NEW.status = 'completed' AND NEW.progress <> 100 THEN
        SIGNAL SQLSTATE '45000'
            SET MESSAGE_TEXT = 'Una tarea completada debe tener progreso de 100';
    END IF;

    IF NEW.status <> 'completed' AND NEW.progress = 100 THEN
        SIGNAL SQLSTATE '45000'
            SET MESSAGE_TEXT = 'Una tarea con progreso de 100 debe estar completada';
    END IF;
END$$

CREATE TRIGGER trg_evaluation_task_history
AFTER UPDATE ON tasks
FOR EACH ROW
BEGIN
    IF NOT (OLD.status <=> NEW.status)
       OR NOT (OLD.progress <=> NEW.progress) THEN
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
            CURRENT_USER()
        );
    END IF;
END$$

CREATE PROCEDURE complete_task (
    IN p_task_id BIGINT UNSIGNED
)
BEGIN
    DECLARE v_project_id BIGINT UNSIGNED DEFAULT NULL;

    DECLARE EXIT HANDLER FOR SQLEXCEPTION
    BEGIN
        ROLLBACK;
        RESIGNAL;
    END;

    START TRANSACTION;

    SELECT project_id
    INTO v_project_id
    FROM tasks
    WHERE task_id = p_task_id
    FOR UPDATE;

    IF v_project_id IS NULL THEN
        SIGNAL SQLSTATE '45000'
            SET MESSAGE_TEXT = 'La tarea no existe';
    END IF;

    UPDATE tasks
    SET status = 'completed',
        progress = 100
    WHERE task_id = p_task_id;

    UPDATE projects
    SET status = CASE
        WHEN NOT EXISTS (
            SELECT 1
            FROM tasks
            WHERE project_id = v_project_id
              AND status <> 'completed'
        ) THEN 'completed'
        ELSE 'active'
    END
    WHERE project_id = v_project_id;

    COMMIT;
END$$

DELIMITER ;

CALL complete_task(2);

CREATE OR REPLACE VIEW v_project_progress AS
SELECT
    p.project_id,
    p.project_name,
    p.status,
    c.full_name AS client_name,
    COUNT(t.task_id) AS task_count,
    SUM(t.status = 'completed') AS completed_tasks,
    COALESCE(ROUND(AVG(t.progress), 2), 0) AS average_progress,
    p.budget,
    p.start_date,
    p.due_date
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
    p.start_date,
    p.due_date;

SELECT
    project_id,
    project_name,
    status,
    client_name,
    task_count,
    completed_tasks,
    average_progress,
    budget,
    start_date,
    due_date
FROM v_project_progress
ORDER BY project_id;

SELECT
    task_id,
    project_id,
    task_name,
    status,
    progress,
    assigned_to,
    due_date
FROM tasks
ORDER BY project_id, task_id;

SELECT
    history_id,
    task_id,
    previous_status,
    new_status,
    previous_progress,
    new_progress,
    changed_at,
    changed_by
FROM task_history
ORDER BY history_id;
