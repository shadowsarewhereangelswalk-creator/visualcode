DROP SCHEMA IF EXISTS une7d23_triggers CASCADE;
CREATE SCHEMA une7d23_triggers;
SET search_path TO une7d23_triggers, public;

CREATE TABLE products (
    product_id bigint GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    sku text NOT NULL UNIQUE,
    product_name text NOT NULL,
    price numeric(10, 2) NOT NULL CHECK (price >= 0),
    stock integer NOT NULL DEFAULT 0 CHECK (stock >= 0),
    updated_at timestamptz NOT NULL DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE product_audit (
    audit_id bigint GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    product_id bigint,
    operation_name text NOT NULL,
    previous_data jsonb,
    new_data jsonb,
    changed_by text NOT NULL,
    changed_at timestamptz NOT NULL DEFAULT CURRENT_TIMESTAMP
);

CREATE OR REPLACE FUNCTION audit_product_changes()
RETURNS trigger
LANGUAGE plpgsql
AS $function$
BEGIN
    IF TG_OP = 'INSERT' THEN
        INSERT INTO product_audit (
            product_id,
            operation_name,
            new_data,
            changed_by
        )
        VALUES (
            NEW.product_id,
            TG_OP,
            to_jsonb(NEW),
            current_user
        );
        RETURN NEW;
    ELSIF TG_OP = 'UPDATE' THEN
        INSERT INTO product_audit (
            product_id,
            operation_name,
            previous_data,
            new_data,
            changed_by
        )
        VALUES (
            NEW.product_id,
            TG_OP,
            to_jsonb(OLD),
            to_jsonb(NEW),
            current_user
        );
        RETURN NEW;
    ELSE
        INSERT INTO product_audit (
            product_id,
            operation_name,
            previous_data,
            changed_by
        )
        VALUES (
            OLD.product_id,
            TG_OP,
            to_jsonb(OLD),
            current_user
        );
        RETURN OLD;
    END IF;
END;
$function$;

CREATE TRIGGER trg_products_audit
AFTER INSERT OR UPDATE OR DELETE ON products
FOR EACH ROW
EXECUTE FUNCTION audit_product_changes();

INSERT INTO products (sku, product_name, price, stock)
VALUES
    ('TRG-001', 'Curso PostgreSQL', 120.00, 20),
    ('TRG-002', 'Guía PL/pgSQL', 32.00, 35);

UPDATE products
SET
    price = 115.00,
    stock = 24,
    updated_at = CURRENT_TIMESTAMP
WHERE sku = 'TRG-001';

DELETE FROM products
WHERE sku = 'TRG-002';

SELECT
    audit_id,
    product_id,
    operation_name,
    previous_data,
    new_data,
    changed_by,
    changed_at
FROM product_audit
ORDER BY audit_id;
