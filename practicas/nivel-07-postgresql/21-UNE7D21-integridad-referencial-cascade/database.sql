DROP SCHEMA IF EXISTS une7d21_cascade CASCADE;
CREATE SCHEMA une7d21_cascade;
SET search_path TO une7d21_cascade, public;

CREATE TABLE customers (
    customer_id bigint GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    full_name text NOT NULL,
    email text NOT NULL UNIQUE
);

CREATE TABLE orders (
    order_id bigint GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    customer_id bigint NOT NULL,
    order_number varchar(20) NOT NULL UNIQUE,
    status text NOT NULL DEFAULT 'pending'
        CHECK (status IN ('pending', 'paid', 'cancelled')),
    CONSTRAINT fk_cascade_order_customer
        FOREIGN KEY (customer_id)
        REFERENCES customers(customer_id)
        ON UPDATE CASCADE
        ON DELETE RESTRICT
);

CREATE TABLE order_items (
    order_item_id bigint GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    order_id bigint NOT NULL,
    product_name text NOT NULL,
    quantity integer NOT NULL CHECK (quantity > 0),
    unit_price numeric(10, 2) NOT NULL CHECK (unit_price >= 0),
    CONSTRAINT fk_cascade_item_order
        FOREIGN KEY (order_id)
        REFERENCES orders(order_id)
        ON UPDATE CASCADE
        ON DELETE CASCADE
);

CREATE TABLE shipments (
    shipment_id bigint GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    order_id bigint NOT NULL UNIQUE,
    tracking_code text NOT NULL UNIQUE,
    shipped_at timestamptz,
    CONSTRAINT fk_cascade_shipment_order
        FOREIGN KEY (order_id)
        REFERENCES orders(order_id)
        ON UPDATE CASCADE
        ON DELETE CASCADE
);

INSERT INTO customers (full_name, email)
VALUES ('Ana Torres', 'ana@example.com');

INSERT INTO orders (customer_id, order_number, status)
VALUES
    (1, 'ORD-2027-001', 'paid'),
    (1, 'ORD-TEMP-001', 'pending');

INSERT INTO order_items (order_id, product_name, quantity, unit_price)
VALUES
    (1, 'Curso PostgreSQL', 1, 120.00),
    (1, 'Guía SQL', 2, 24.00),
    (2, 'Registro temporal', 1, 1.00);

INSERT INTO shipments (order_id, tracking_code, shipped_at)
VALUES
    (1, 'TRACK-PG-001', CURRENT_TIMESTAMP),
    (2, 'TRACK-TEMP-001', NULL);

SELECT
    o.order_number,
    COUNT(oi.order_item_id) AS item_count,
    SUM(oi.quantity * oi.unit_price) AS order_total,
    s.tracking_code
FROM orders AS o
INNER JOIN order_items AS oi
    ON oi.order_id = o.order_id
LEFT JOIN shipments AS s
    ON s.order_id = o.order_id
GROUP BY
    o.order_id,
    o.order_number,
    s.tracking_code
ORDER BY o.order_number;

DELETE FROM orders
WHERE order_number = 'ORD-TEMP-001'
RETURNING order_id, order_number;

SELECT
    (SELECT COUNT(*) FROM orders) AS orders_remaining,
    (SELECT COUNT(*) FROM order_items) AS items_remaining,
    (SELECT COUNT(*) FROM shipments) AS shipments_remaining;
