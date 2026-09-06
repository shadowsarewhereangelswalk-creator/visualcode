DROP DATABASE IF EXISTS une6d11_select;
CREATE DATABASE une6d11_select CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci;
USE une6d11_select;

CREATE TABLE job_offers (
  offer_id INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
  title VARCHAR(140) NOT NULL,
  area ENUM('Desarrollo','Marketing','Video','Automatización') NOT NULL,
  work_mode ENUM('Remoto','Híbrido','Presencial') NOT NULL,
  salary DECIMAL(10,2) NOT NULL,
  published_on DATE NOT NULL,
  active BOOLEAN NOT NULL DEFAULT TRUE
) ENGINE=InnoDB;

INSERT INTO job_offers (title, area, work_mode, salary, published_on, active) VALUES
('Desarrollador Frontend', 'Desarrollo', 'Remoto', 3200.00, '2026-12-01', TRUE),
('Especialista SEO', 'Marketing', 'Híbrido', 2800.00, '2026-12-02', TRUE),
('Editor de video con IA', 'Video', 'Remoto', 3000.00, '2026-12-03', TRUE),
('Analista de automatización', 'Automatización', 'Remoto', 3600.00, '2026-12-04', TRUE),
('Coordinador de contenidos', 'Marketing', 'Presencial', 2400.00, '2026-11-25', FALSE),
('Desarrollador Backend', 'Desarrollo', 'Híbrido', 3900.00, '2026-12-05', TRUE);

SELECT *
FROM job_offers;

SELECT offer_id, title, area, salary
FROM job_offers
WHERE active = TRUE
  AND work_mode = 'Remoto'
  AND salary >= 3000
ORDER BY salary DESC, title ASC;

SELECT offer_id, title, published_on
FROM job_offers
WHERE published_on BETWEEN '2026-12-01' AND '2026-12-31'
ORDER BY published_on DESC
LIMIT 3;
