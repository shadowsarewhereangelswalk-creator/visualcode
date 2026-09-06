DROP SCHEMA IF EXISTS une7d15_sales CASCADE;
CREATE SCHEMA une7d15_sales;
SET search_path TO une7d15_sales, public;

CREATE TABLE customers (
    customer_id bigint GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    full_name text NOT NULL,
    email text NOT NULL UNIQUE
);

CREATE TABLE products (
    product_id bigint GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    product_name text NOT NULL,
    price numeric(10, 2) NOT NULL CHECK (price >= 0)
);

CREATE TABLE orders (
    order_id bigint GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    customer_id bigint NOT NULL,
    status text NOT NULL DEFAULT 'pending' CHECK (status IN ('pending', 'paid', 'cancelled')),
    ordered_at timestamptz NOT NULL DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT fk_sales_order_customer FOREIGN KEY (customer_id) REFERENCES customers(customer_id) ON UPDATE CASCADE ON DELETE RESTRICT
);

CREATE TABLE order_items (
    order_id bigint NOT NULL,
    product_id bigint NOT NULL,
    quantity integer NOT NULL CHECK (quantity > 0),
    unit_price numeric(10, 2) NOT NULL CHECK (unit_price >= 0),
    PRIMARY KEY (order_id, product_id),
    CONSTRAINT fk_sales_item_order FOREIGN KEY (order_id) REFERENCES orders(order_id) ON UPDATE CASCADE ON DELETE CASCADE,
    CONSTRAINT fk_sales_item_product FOREIGN KEY (product_id) REFERENCES products(product_id) ON UPDATE CASCADE ON DELETE RESTRICT
);

INSERT INTO customers (full_name, email)
VALUES ('Ana Torres', 'ana@example.com'), ('Bruno Díaz', 'bruno@example.com');

INSERT INTO products (product_name, price)
VALUES ('Curso PostgreSQL', 120.00), ('Guía SQL', 24.00), ('Plantilla de migración', 45.00);

WITH new_order AS (
    INSERT INTO orders (customer_id, status)
    VALUES (1, 'paid')
    RETURNING order_id
)
INSERT INTO order_items (order_id, product_id, quantity, unit_price)
SELECT new_order.order_id, source.product_id, source.quantity, p.price
FROM new_order
CROSS JOIN (VALUES (1::bigint, 1), (2::bigint, 2)) AS source(product_id, quantity)
INNER JOIN products AS p ON p.product_id = source.product_id;

INSERT INTO orders (customer_id, status)
VALUES (2, 'pending');

INSERT INTO order_items (order_id, product_id, quantity, unit_price)
VALUES (2, 3, 1, 45.00);

SELECT
    o.order_id, c.full_name AS customer_name, o.status,
    COUNT(oi.product_id) AS different_products,
    SUM(oi.quantity) AS total_units,
    SUM(oi.quantity * oi.unit_price) AS order_total
FROM orders AS o
INNER JOIN customers AS c ON c.customer_id = o.customer_id
INNER JOIN order_items AS oi ON oi.order_id = o.order_id
GROUP BY o.order_id, c.full_name, o.status
ORDER BY o.order_id;
