DROP SCHEMA IF EXISTS une7d27_rules_practice CASCADE;
CREATE SCHEMA une7d27_rules_practice;
SET search_path TO une7d27_rules_practice, public;

CREATE TABLE customers (
    customer_id bigint GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    full_name text NOT NULL,
    email text NOT NULL UNIQUE,
    active boolean NOT NULL DEFAULT true,
    deleted_at timestamptz
);

CREATE VIEW active_customers AS
SELECT
    customer_id,
    full_name,
    email
FROM customers
WHERE active = true
  AND deleted_at IS NULL;

CREATE RULE soft_delete_customer AS
ON DELETE TO customers
DO INSTEAD
UPDATE customers
SET
    active = false,
    deleted_at = CURRENT_TIMESTAMP
WHERE customers.customer_id = OLD.customer_id;

INSERT INTO customers (full_name, email)
VALUES
    ('Ana Torres', 'ana@example.com'),
    ('Bruno Díaz', 'bruno@example.com'),
    ('Carla Méndez', 'carla@example.com');

DELETE FROM customers
WHERE email = 'bruno@example.com';

SELECT
    customer_id,
    full_name,
    email
FROM active_customers
ORDER BY customer_id;

SELECT
    customer_id,
    full_name,
    email,
    active,
    deleted_at
FROM customers
ORDER BY customer_id;
