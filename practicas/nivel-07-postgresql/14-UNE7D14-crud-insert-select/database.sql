DROP SCHEMA IF EXISTS une7d14_insert_select CASCADE;
CREATE SCHEMA une7d14_insert_select;
SET search_path TO une7d14_insert_select, public;

CREATE TABLE categories (
    category_id bigint GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    category_name text NOT NULL UNIQUE
);

CREATE TABLE products (
    product_id bigint GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    category_id bigint NOT NULL,
    sku text NOT NULL UNIQUE,
    product_name text NOT NULL,
    price numeric(10, 2) NOT NULL CHECK (price >= 0),
    stock integer NOT NULL DEFAULT 0 CHECK (stock >= 0),
    active boolean NOT NULL DEFAULT true,
    created_at timestamptz NOT NULL DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT fk_insert_product_category FOREIGN KEY (category_id) REFERENCES categories(category_id) ON UPDATE CASCADE ON DELETE RESTRICT
);

INSERT INTO categories (category_name)
VALUES ('Formación'), ('Recursos')
RETURNING category_id, category_name;

INSERT INTO products (category_id, sku, product_name, price, stock)
VALUES
    (1, 'PG-COURSE', 'Curso PostgreSQL', 120.00, 25),
    (1, 'SQL-COURSE', 'Curso SQL', 95.00, 30),
    (2, 'ER-GUIDE', 'Guía Entidad-Relación', 28.50, 40),
    (2, 'OLD-GUIDE', 'Guía archivada', 15.00, 0)
RETURNING product_id, sku, product_name;

SELECT p.product_id, p.sku, p.product_name, c.category_name, p.price, p.stock
FROM products AS p
INNER JOIN categories AS c ON c.category_id = p.category_id
WHERE p.active = true AND p.stock > 0 AND p.price BETWEEN 20 AND 130
ORDER BY p.price DESC, p.product_name;

SELECT
    c.category_name, COUNT(p.product_id) AS product_count,
    COALESCE(SUM(p.stock), 0) AS available_units,
    COALESCE(ROUND(AVG(p.price), 2), 0) AS average_price
FROM categories AS c
LEFT JOIN products AS p ON p.category_id = c.category_id
GROUP BY c.category_id, c.category_name
ORDER BY c.category_name;
