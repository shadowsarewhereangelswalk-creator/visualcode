DROP SCHEMA IF EXISTS une7d25_inventory_trigger CASCADE;
CREATE SCHEMA une7d25_inventory_trigger;
SET search_path TO une7d25_inventory_trigger, public;

CREATE TABLE products (
    product_id bigint GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    sku text NOT NULL UNIQUE,
    product_name text NOT NULL,
    stock integer NOT NULL DEFAULT 0 CHECK (stock >= 0),
    updated_at timestamptz NOT NULL DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE stock_movements (
    movement_id bigint GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    product_id bigint NOT NULL,
    quantity_change integer NOT NULL CHECK (quantity_change <> 0),
    reason text NOT NULL,
    resulting_stock integer NOT NULL,
    created_by text NOT NULL DEFAULT current_user,
    created_at timestamptz NOT NULL DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT fk_movement_product
        FOREIGN KEY (product_id)
        REFERENCES products(product_id)
        ON UPDATE CASCADE
        ON DELETE RESTRICT
);

CREATE OR REPLACE FUNCTION apply_stock_movement()
RETURNS trigger
LANGUAGE plpgsql
AS $function$
DECLARE
    current_stock integer;
    next_stock integer;
BEGIN
    SELECT stock
    INTO STRICT current_stock
    FROM products
    WHERE product_id = NEW.product_id
    FOR UPDATE;

    next_stock := current_stock + NEW.quantity_change;

    IF next_stock < 0 THEN
        RAISE EXCEPTION 'El movimiento dejaría un stock negativo';
    END IF;

    UPDATE products
    SET
        stock = next_stock,
        updated_at = CURRENT_TIMESTAMP
    WHERE product_id = NEW.product_id;

    NEW.resulting_stock := next_stock;
    NEW.created_by := current_user;

    RETURN NEW;
EXCEPTION
    WHEN no_data_found THEN
        RAISE EXCEPTION 'El producto indicado no existe';
END;
$function$;

CREATE TRIGGER trg_apply_stock_movement
BEFORE INSERT ON stock_movements
FOR EACH ROW
EXECUTE FUNCTION apply_stock_movement();

INSERT INTO products (sku, product_name, stock)
VALUES
    ('STK-001', 'Curso PostgreSQL', 20),
    ('STK-002', 'Guía PL/pgSQL', 35);

INSERT INTO stock_movements (
    product_id,
    quantity_change,
    reason
)
VALUES
    (1, 8, 'Reposición de inventario'),
    (1, -3, 'Venta confirmada'),
    (2, -5, 'Entrega de pedidos');

SELECT
    product_id,
    sku,
    product_name,
    stock,
    updated_at
FROM products
ORDER BY product_id;

SELECT
    movement_id,
    product_id,
    quantity_change,
    reason,
    resulting_stock,
    created_by,
    created_at
FROM stock_movements
ORDER BY movement_id;
