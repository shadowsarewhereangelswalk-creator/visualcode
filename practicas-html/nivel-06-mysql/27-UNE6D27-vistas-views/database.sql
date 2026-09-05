DROP DATABASE IF EXISTS une6d27_views;
CREATE DATABASE une6d27_views
CHARACTER SET utf8mb4
COLLATE utf8mb4_0900_ai_ci;

USE une6d27_views;

CREATE TABLE products (
    product_id BIGINT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    category_name VARCHAR(100) NOT NULL,
    product_name VARCHAR(140) NOT NULL,
    price DECIMAL(10, 2) NOT NULL,
    stock INT UNSIGNED NOT NULL DEFAULT 0,
    active BOOLEAN NOT NULL DEFAULT TRUE,
    CONSTRAINT chk_view_product_price CHECK (price >= 0)
) ENGINE = InnoDB;

INSERT INTO products (category_name, product_name, price, stock, active)
VALUES
    ('Audio', 'Audífonos inalámbricos', 79.90, 18, TRUE),
    ('Audio', 'Micrófono USB', 119.00, 7, TRUE),
    ('Video', 'Cámara web HD', 69.50, 0, TRUE),
    ('Accesorios', 'Hub USB-C', 49.90, 12, FALSE),
    ('Accesorios', 'Soporte para laptop', 39.00, 25, TRUE);

CREATE OR REPLACE VIEW v_active_products AS
SELECT
    product_id,
    category_name,
    product_name,
    price,
    stock,
    active
FROM products
WHERE active = TRUE
WITH CASCADED CHECK OPTION;

CREATE OR REPLACE VIEW v_category_summary AS
SELECT
    category_name,
    COUNT(*) AS active_products,
    SUM(stock) AS available_units,
    ROUND(AVG(price), 2) AS average_price,
    MIN(price) AS minimum_price,
    MAX(price) AS maximum_price
FROM products
WHERE active = TRUE
GROUP BY category_name;

UPDATE v_active_products
SET price = 74.90,
    stock = 20
WHERE product_id = 1;

SELECT
    product_id,
    category_name,
    product_name,
    price,
    stock
FROM v_active_products
ORDER BY category_name, product_name;

SELECT
    category_name,
    active_products,
    available_units,
    average_price,
    minimum_price,
    maximum_price
FROM v_category_summary
ORDER BY category_name;
