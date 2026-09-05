DROP SCHEMA IF EXISTS une7d03_store_model CASCADE;
CREATE SCHEMA une7d03_store_model;
SET search_path TO une7d03_store_model, public;

CREATE TABLE customers (
    customer_id bigint GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    full_name text NOT NULL,
    email text NOT NULL UNIQUE
);

CREATE TABLE customer_addresses (
    address_id bigint GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    customer_id bigint NOT NULL,
    label text NOT NULL,
    city text NOT NULL,
    address_line text NOT NULL,
    is_primary boolean NOT NULL DEFAULT false,
    UNIQUE (customer_id, label),
    UNIQUE (address_id, customer_id),
    CONSTRAINT fk_addresses_customer
        FOREIGN KEY (customer_id)
        REFERENCES customers(customer_id)
        ON UPDATE CASCADE
        ON DELETE CASCADE
);

CREATE TABLE products (
    product_id bigint GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    sku text NOT NULL UNIQUE,
    product_name text NOT NULL,
    price numeric(10, 2) NOT NULL CHECK (price >= 0),
    stock integer NOT NULL DEFAULT 0 CHECK (stock >= 0)
);

CREATE TABLE orders (
    order_id bigint GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    customer_id bigint NOT NULL,
    shipping_address_id bigint NOT NULL,
    status text NOT NULL DEFAULT 'pending'
        CHECK (status IN ('pending', 'paid', 'shipped', 'delivered', 'cancelled')),
    ordered_at timestamptz NOT NULL DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT fk_orders_customer
        FOREIGN KEY (customer_id)
        REFERENCES customers(customer_id)
        ON UPDATE CASCADE
        ON DELETE RESTRICT,
    CONSTRAINT fk_orders_address_customer
        FOREIGN KEY (shipping_address_id, customer_id)
        REFERENCES customer_addresses(address_id, customer_id)
        ON UPDATE CASCADE
        ON DELETE RESTRICT
);

CREATE TABLE order_items (
    order_id bigint NOT NULL,
    product_id bigint NOT NULL,
    quantity integer NOT NULL CHECK (quantity > 0),
    unit_price numeric(10, 2) NOT NULL CHECK (unit_price >= 0),
    PRIMARY KEY (order_id, product_id),
    CONSTRAINT fk_items_order
        FOREIGN KEY (order_id)
        REFERENCES orders(order_id)
        ON UPDATE CASCADE
        ON DELETE CASCADE,
    CONSTRAINT fk_items_product
        FOREIGN KEY (product_id)
        REFERENCES products(product_id)
        ON UPDATE CASCADE
        ON DELETE RESTRICT
);

INSERT INTO customers (full_name, email)
VALUES ('Ana Torres', 'ana@example.com'), ('Bruno Díaz', 'bruno@example.com');

INSERT INTO customer_addresses (customer_id, label, city, address_line, is_primary)
VALUES
    (1, 'Casa', 'Caracas', 'Avenida Principal 120', true),
    (2, 'Oficina', 'Valencia', 'Centro Empresarial 45', true);

INSERT INTO products (sku, product_name, price, stock)
VALUES
    ('PG-001', 'Curso PostgreSQL', 120.00, 30),
    ('PG-002', 'Guía de modelado', 28.50, 50),
    ('PG-003', 'Plantilla de migración', 45.00, 20);

INSERT INTO orders (customer_id, shipping_address_id, status)
VALUES (1, 1, 'paid'), (2, 2, 'pending');

INSERT INTO order_items (order_id, product_id, quantity, unit_price)
VALUES (1, 1, 1, 120.00), (1, 2, 2, 28.50), (2, 3, 1, 45.00);

SELECT
    o.order_id,
    c.full_name AS customer_name,
    a.city,
    o.status,
    SUM(oi.quantity * oi.unit_price) AS order_total
FROM orders AS o
INNER JOIN customers AS c ON c.customer_id = o.customer_id
INNER JOIN customer_addresses AS a ON a.address_id = o.shipping_address_id
INNER JOIN order_items AS oi ON oi.order_id = o.order_id
GROUP BY o.order_id, c.full_name, a.city, o.status
ORDER BY o.order_id;
