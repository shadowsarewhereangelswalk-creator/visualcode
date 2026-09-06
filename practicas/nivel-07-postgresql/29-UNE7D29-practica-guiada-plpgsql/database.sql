DROP SCHEMA IF EXISTS une7d29_order_function CASCADE;
CREATE SCHEMA une7d29_order_function;
SET search_path TO une7d29_order_function, public;

CREATE TABLE customers (
    customer_id bigint GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    full_name text NOT NULL,
    email text NOT NULL UNIQUE
);

CREATE TABLE products (
    product_id bigint GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    product_name text NOT NULL,
    price numeric(10, 2) NOT NULL CHECK (price >= 0),
    stock integer NOT NULL DEFAULT 0 CHECK (stock >= 0),
    active boolean NOT NULL DEFAULT true
);

CREATE TABLE orders (
    order_id bigint GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    customer_id bigint NOT NULL,
    status text NOT NULL DEFAULT 'pending'
        CHECK (status IN ('pending', 'paid', 'cancelled')),
    total numeric(12, 2) NOT NULL CHECK (total >= 0),
    created_at timestamptz NOT NULL DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT fk_function_order_customer
        FOREIGN KEY (customer_id)
        REFERENCES customers(customer_id)
        ON UPDATE CASCADE
        ON DELETE RESTRICT
);

CREATE TABLE order_items (
    order_item_id bigint GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    order_id bigint NOT NULL,
    product_id bigint NOT NULL,
    quantity integer NOT NULL CHECK (quantity > 0),
    unit_price numeric(10, 2) NOT NULL CHECK (unit_price >= 0),
    CONSTRAINT fk_function_item_order
        FOREIGN KEY (order_id)
        REFERENCES orders(order_id)
        ON UPDATE CASCADE
        ON DELETE CASCADE,
    CONSTRAINT fk_function_item_product
        FOREIGN KEY (product_id)
        REFERENCES products(product_id)
        ON UPDATE CASCADE
        ON DELETE RESTRICT
);

CREATE OR REPLACE FUNCTION create_single_product_order(
    requested_customer_id bigint,
    requested_product_id bigint,
    requested_quantity integer
)
RETURNS bigint
LANGUAGE plpgsql
AS $function$
DECLARE
    selected_price numeric(10, 2);
    selected_stock integer;
    new_order_id bigint;
BEGIN
    IF requested_quantity IS NULL OR requested_quantity <= 0 THEN
        RAISE EXCEPTION 'La cantidad debe ser mayor que cero';
    END IF;

    SELECT price, stock
    INTO STRICT selected_price, selected_stock
    FROM products
    WHERE product_id = requested_product_id
      AND active = true
    FOR UPDATE;

    IF selected_stock < requested_quantity THEN
        RAISE EXCEPTION 'No hay existencias suficientes';
    END IF;

    INSERT INTO orders (
        customer_id,
        total
    )
    VALUES (
        requested_customer_id,
        selected_price * requested_quantity
    )
    RETURNING order_id INTO new_order_id;

    INSERT INTO order_items (
        order_id,
        product_id,
        quantity,
        unit_price
    )
    VALUES (
        new_order_id,
        requested_product_id,
        requested_quantity,
        selected_price
    );

    UPDATE products
    SET stock = stock - requested_quantity
    WHERE product_id = requested_product_id;

    RETURN new_order_id;
EXCEPTION
    WHEN no_data_found THEN
        RAISE EXCEPTION 'El producto no existe o está inactivo';
END;
$function$;

INSERT INTO customers (full_name, email)
VALUES
    ('Ana Torres', 'ana@example.com'),
    ('Bruno Díaz', 'bruno@example.com');

INSERT INTO products (product_name, price, stock)
VALUES
    ('Curso PostgreSQL', 120.00, 20),
    ('Guía PL/pgSQL', 32.00, 35);

SELECT create_single_product_order(1, 1, 2) AS new_order_id;
SELECT create_single_product_order(2, 2, 1) AS new_order_id;

SELECT
    o.order_id,
    c.full_name AS customer_name,
    p.product_name,
    oi.quantity,
    oi.unit_price,
    o.total,
    o.status,
    o.created_at
FROM orders AS o
INNER JOIN customers AS c
    ON c.customer_id = o.customer_id
INNER JOIN order_items AS oi
    ON oi.order_id = o.order_id
INNER JOIN products AS p
    ON p.product_id = oi.product_id
ORDER BY o.order_id;
