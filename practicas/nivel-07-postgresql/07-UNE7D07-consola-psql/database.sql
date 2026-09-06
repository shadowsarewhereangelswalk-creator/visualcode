DROP SCHEMA IF EXISTS une7d07_psql CASCADE;
CREATE SCHEMA une7d07_psql;
SET search_path TO une7d07_psql, public;

CREATE TABLE products (
    product_id bigint GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    sku text NOT NULL UNIQUE,
    product_name text NOT NULL,
    price numeric(10, 2) NOT NULL CHECK (price >= 0),
    active boolean NOT NULL DEFAULT true
);

INSERT INTO products (sku, product_name, price, active)
VALUES
    ('PSQL-001', 'Curso PostgreSQL', 120.00, true),
    ('PSQL-002', 'Guía de comandos', 24.00, true),
    ('PSQL-003', 'Laboratorio archivado', 18.00, false);

SELECT product_id, sku, product_name, price, active
FROM products
ORDER BY product_id;
