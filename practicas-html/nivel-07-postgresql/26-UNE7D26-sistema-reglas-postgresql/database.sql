DROP SCHEMA IF EXISTS une7d26_rules CASCADE;
CREATE SCHEMA une7d26_rules;
SET search_path TO une7d26_rules, public;

CREATE TABLE products (
    product_id bigint GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    sku text NOT NULL UNIQUE,
    product_name text NOT NULL,
    price numeric(10, 2) NOT NULL CHECK (price >= 0),
    active boolean NOT NULL DEFAULT true
);

CREATE TABLE price_change_log (
    log_id bigint GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    product_id bigint NOT NULL,
    previous_price numeric(10, 2) NOT NULL,
    new_price numeric(10, 2) NOT NULL,
    changed_by text NOT NULL,
    changed_at timestamptz NOT NULL DEFAULT CURRENT_TIMESTAMP
);

CREATE RULE log_product_price_update AS
ON UPDATE TO products
WHERE OLD.price IS DISTINCT FROM NEW.price
DO ALSO
INSERT INTO price_change_log (
    product_id,
    previous_price,
    new_price,
    changed_by
)
VALUES (
    OLD.product_id,
    OLD.price,
    NEW.price,
    current_user
);

INSERT INTO products (sku, product_name, price)
VALUES
    ('RULE-001', 'Curso PostgreSQL', 120.00),
    ('RULE-002', 'Guía SQL', 24.00);

UPDATE products
SET price = CASE
    WHEN sku = 'RULE-001' THEN 115.00
    WHEN sku = 'RULE-002' THEN 22.50
    ELSE price
END
WHERE sku IN ('RULE-001', 'RULE-002');

SELECT
    product_id,
    sku,
    product_name,
    price,
    active
FROM products
ORDER BY product_id;

SELECT
    log_id,
    product_id,
    previous_price,
    new_price,
    changed_by,
    changed_at
FROM price_change_log
ORDER BY log_id;
