DROP DATABASE IF EXISTS une6d07_catalog;
CREATE DATABASE une6d07_catalog CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci;
USE une6d07_catalog;

CREATE TABLE categories (
  category_id SMALLINT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
  name VARCHAR(80) NOT NULL UNIQUE,
  description VARCHAR(255)
) ENGINE=InnoDB;

CREATE TABLE catalog_products (
  product_id INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
  category_id SMALLINT UNSIGNED NOT NULL,
  sku CHAR(10) NOT NULL UNIQUE,
  name VARCHAR(140) NOT NULL,
  description TEXT,
  price DECIMAL(10,2) NOT NULL CHECK (price >= 0),
  stock INT UNSIGNED NOT NULL DEFAULT 0,
  weight_kg DECIMAL(7,3),
  active BOOLEAN NOT NULL DEFAULT TRUE,
  metadata JSON,
  available_from DATE,
  created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  CONSTRAINT fk_catalog_category
    FOREIGN KEY (category_id) REFERENCES categories(category_id)
    ON UPDATE CASCADE
    ON DELETE RESTRICT
) ENGINE=InnoDB;

INSERT INTO categories (name, description) VALUES
('Tecnología', 'Equipos y accesorios'),
('Formación', 'Cursos y recursos educativos');

INSERT INTO catalog_products (
  category_id,
  sku,
  name,
  description,
  price,
  stock,
  weight_kg,
  metadata,
  available_from
) VALUES
(1, 'TEC0000001', 'Teclado compacto', 'Teclado mecánico de formato reducido.', 68.90, 20, 0.720, JSON_OBJECT('color', 'azul', 'layout', 'ES'), '2026-12-01'),
(2, 'FOR0000001', 'Curso de MySQL', 'Programa práctico de bases de datos.', 95.00, 100, NULL, JSON_OBJECT('hours', 45, 'level', 6), '2026-12-05');

SELECT
  p.sku,
  p.name,
  c.name AS category,
  p.price,
  p.stock,
  p.active,
  p.metadata
FROM catalog_products AS p
INNER JOIN categories AS c ON c.category_id = p.category_id
ORDER BY p.name;
