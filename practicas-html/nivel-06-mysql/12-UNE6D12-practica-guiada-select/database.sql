DROP DATABASE IF EXISTS une6d12_reports;
CREATE DATABASE une6d12_reports CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci;
USE une6d12_reports;

CREATE TABLE sales (
  sale_id INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
  customer_name VARCHAR(120) NOT NULL,
  city VARCHAR(80) NOT NULL,
  product VARCHAR(120) NOT NULL,
  category VARCHAR(80) NOT NULL,
  quantity INT UNSIGNED NOT NULL,
  unit_price DECIMAL(10,2) NOT NULL,
  sold_on DATE NOT NULL,
  status ENUM('Pagada','Pendiente','Cancelada') NOT NULL
) ENGINE=InnoDB;

INSERT INTO sales (customer_name, city, product, category, quantity, unit_price, sold_on, status) VALUES
('Ana Pérez', 'Miami', 'Curso SQL', 'Formación', 1, 95.00, '2026-12-01', 'Pagada'),
('Luis Gómez', 'Tampa', 'Plantilla Web', 'Recursos', 2, 28.00, '2026-12-02', 'Pagada'),
('Marta Díaz', 'Miami', 'Curso JavaScript', 'Formación', 1, 120.00, '2026-12-03', 'Pendiente'),
('Carlos León', 'Orlando', 'Kit UI', 'Recursos', 3, 42.00, '2026-12-03', 'Pagada'),
('Elena Ruiz', 'Tampa', 'Curso SQL', 'Formación', 1, 95.00, '2026-12-04', 'Cancelada'),
('Sara Mora', 'Miami', 'Guía SEO', 'Recursos', 2, 18.50, '2026-12-05', 'Pagada');

SELECT sale_id, customer_name, product, status
FROM sales
WHERE customer_name LIKE '%a%'
ORDER BY customer_name;

SELECT sale_id, customer_name, city, quantity * unit_price AS line_total
FROM sales
WHERE city IN ('Miami', 'Tampa')
  AND status = 'Pagada'
  AND unit_price BETWEEN 20 AND 100
ORDER BY line_total DESC;

SELECT
  category,
  COUNT(*) AS sale_count,
  SUM(quantity) AS units,
  SUM(quantity * unit_price) AS revenue
FROM sales
WHERE status = 'Pagada'
GROUP BY category
HAVING revenue >= 50
ORDER BY revenue DESC;
