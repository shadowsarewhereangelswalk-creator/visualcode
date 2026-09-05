DROP SCHEMA IF EXISTS une7d16_update_delete CASCADE;
CREATE SCHEMA une7d16_update_delete;
SET search_path TO une7d16_update_delete, public;

CREATE TABLE inventory (
    product_id bigint GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    sku text NOT NULL UNIQUE,
    product_name text NOT NULL,
    price numeric(10, 2) NOT NULL CHECK (price >= 0),
    stock integer NOT NULL DEFAULT 0 CHECK (stock >= 0),
    status text NOT NULL DEFAULT 'active' CHECK (status IN ('active', 'paused', 'sold_out')),
    updated_at timestamptz NOT NULL DEFAULT CURRENT_TIMESTAMP
);

INSERT INTO inventory (sku, product_name, price, stock, status)
VALUES
    ('INV-001', 'Curso PostgreSQL', 120.00, 12, 'active'),
    ('INV-002', 'Guía SQL', 24.00, 3, 'active'),
    ('INV-003', 'Plantilla temporal', 15.00, 1, 'paused'),
    ('INV-004', 'Producto agotado', 19.00, 0, 'active');

BEGIN;

UPDATE inventory
SET stock = stock + 10, price = 22.50, updated_at = CURRENT_TIMESTAMP
WHERE sku = 'INV-002'
RETURNING product_id, sku, price, stock, updated_at;

UPDATE inventory
SET status = 'sold_out', updated_at = CURRENT_TIMESTAMP
WHERE stock = 0
RETURNING product_id, sku, status;

DELETE FROM inventory
WHERE sku = 'INV-003' AND status = 'paused'
RETURNING product_id, sku, product_name;

COMMIT;

SELECT product_id, sku, product_name, price, stock, status, updated_at
FROM inventory
ORDER BY product_id;
