DROP DATABASE IF EXISTS une6d23_procedures;
CREATE DATABASE une6d23_procedures CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci;
USE une6d23_procedures;

CREATE TABLE products (
  product_id INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
  name VARCHAR(120) NOT NULL,
  category VARCHAR(80) NOT NULL,
  price DECIMAL(10,2) NOT NULL CHECK (price >= 0),
  active BOOLEAN NOT NULL DEFAULT TRUE
) ENGINE=InnoDB;

INSERT INTO products (name, category, price, active) VALUES
('Curso MySQL', 'Formación', 95.00, TRUE),
('Curso JavaScript', 'Formación', 120.00, TRUE),
('Guía SQL', 'Recursos', 24.00, TRUE),
('Plantilla Web', 'Recursos', 38.00, TRUE),
('Curso archivado', 'Formación', 70.00, FALSE);

DELIMITER $$

CREATE PROCEDURE products_by_price_range (
  IN p_minimum DECIMAL(10,2),
  IN p_maximum DECIMAL(10,2)
)
BEGIN
  IF p_minimum < 0 OR p_maximum < p_minimum THEN
    SIGNAL SQLSTATE '45000'
      SET MESSAGE_TEXT = 'El rango de precios no es válido';
  END IF;

  SELECT
    product_id,
    name,
    category,
    price
  FROM products
  WHERE active = TRUE
    AND price BETWEEN p_minimum AND p_maximum
  ORDER BY price, name;
END$$

CREATE PROCEDURE category_summary (
  IN p_category VARCHAR(80)
)
BEGIN
  SELECT
    category,
    COUNT(*) AS product_count,
    MIN(price) AS minimum_price,
    MAX(price) AS maximum_price,
    AVG(price) AS average_price
  FROM products
  WHERE active = TRUE
    AND category = p_category
  GROUP BY category;
END$$

DELIMITER ;

CALL products_by_price_range(20.00, 100.00);
CALL category_summary('Formación');
