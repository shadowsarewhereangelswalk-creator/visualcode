DROP SCHEMA IF EXISTS une7d30_migration CASCADE;
CREATE SCHEMA une7d30_migration;
SET search_path TO une7d30_migration, public;

CREATE TABLE legacy_customers (
    customer_id integer PRIMARY KEY,
    full_name varchar(120) NOT NULL,
    email varchar(160) NOT NULL,
    active smallint NOT NULL,
    created_at timestamp NOT NULL
);

CREATE TABLE legacy_products (
    product_id integer PRIMARY KEY,
    category_name varchar(100) NOT NULL,
    product_name varchar(140) NOT NULL,
    price numeric(10, 2) NOT NULL,
    stock integer NOT NULL
);

CREATE TABLE legacy_orders (
    order_id integer PRIMARY KEY,
    customer_id integer NOT NULL,
    status varchar(20) NOT NULL,
    ordered_at timestamp NOT NULL
);

CREATE TABLE legacy_order_items (
    order_id integer NOT NULL,
    product_id integer NOT NULL,
    quantity integer NOT NULL,
    unit_price numeric(10, 2) NOT NULL,
    PRIMARY KEY (order_id, product_id)
);

INSERT INTO legacy_customers
VALUES
    (101, 'Ana Torres', 'ANA@EXAMPLE.COM', 1, '2026-10-01 09:00:00'),
    (102, 'Bruno Díaz', 'bruno@example.com', 1, '2026-11-15 14:30:00');

INSERT INTO legacy_products
VALUES
    (501, 'Formación', 'Curso PostgreSQL', 120.00, 20),
    (502, 'Recursos', 'Guía SQL', 24.00, 35),
    (503, 'Recursos', 'Plantilla de migración', 45.00, 18);

INSERT INTO legacy_orders
VALUES
    (1001, 101, 'PAID', '2026-12-01 10:15:00'),
    (1002, 102, 'PENDING', '2026-12-02 16:40:00');

INSERT INTO legacy_order_items
VALUES
    (1001, 501, 1, 120.00),
    (1001, 502, 2, 24.00),
    (1002, 503, 1, 45.00);

CREATE TABLE customers (
    customer_id bigint GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    full_name text NOT NULL,
    email text NOT NULL UNIQUE,
    active boolean NOT NULL DEFAULT true,
    metadata jsonb NOT NULL DEFAULT '{}'::jsonb,
    created_at timestamptz NOT NULL
);

CREATE TABLE categories (
    category_id bigint GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    category_name text NOT NULL UNIQUE
);

CREATE TABLE products (
    product_id bigint GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    category_id bigint NOT NULL,
    product_name text NOT NULL,
    price numeric(10, 2) NOT NULL CHECK (price >= 0),
    stock integer NOT NULL DEFAULT 0 CHECK (stock >= 0),
    CONSTRAINT fk_migration_product_category
        FOREIGN KEY (category_id)
        REFERENCES categories(category_id)
        ON UPDATE CASCADE
        ON DELETE RESTRICT
);

CREATE TABLE orders (
    order_id bigint GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    customer_id bigint NOT NULL,
    status text NOT NULL
        CHECK (status IN ('pending', 'paid', 'cancelled')),
    ordered_at timestamptz NOT NULL,
    CONSTRAINT fk_migration_order_customer
        FOREIGN KEY (customer_id)
        REFERENCES customers(customer_id)
        ON UPDATE CASCADE
        ON DELETE RESTRICT
);

CREATE TABLE order_items (
    order_id bigint NOT NULL,
    product_id bigint NOT NULL,
    quantity integer NOT NULL CHECK (quantity > 0),
    unit_price numeric(10, 2) NOT NULL CHECK (unit_price >= 0),
    PRIMARY KEY (order_id, product_id),
    CONSTRAINT fk_migration_item_order
        FOREIGN KEY (order_id)
        REFERENCES orders(order_id)
        ON UPDATE CASCADE
        ON DELETE CASCADE,
    CONSTRAINT fk_migration_item_product
        FOREIGN KEY (product_id)
        REFERENCES products(product_id)
        ON UPDATE CASCADE
        ON DELETE RESTRICT
);

INSERT INTO customers (
    customer_id,
    full_name,
    email,
    active,
    metadata,
    created_at
)
OVERRIDING SYSTEM VALUE
SELECT
    customer_id,
    btrim(full_name),
    lower(btrim(email)),
    active = 1,
    jsonb_build_object('source', 'legacy_mysql'),
    created_at AT TIME ZONE 'America/Caracas'
FROM legacy_customers;

INSERT INTO categories (category_name)
SELECT DISTINCT btrim(category_name)
FROM legacy_products
ORDER BY btrim(category_name);

INSERT INTO products (
    product_id,
    category_id,
    product_name,
    price,
    stock
)
OVERRIDING SYSTEM VALUE
SELECT
    lp.product_id,
    c.category_id,
    btrim(lp.product_name),
    lp.price,
    lp.stock
FROM legacy_products AS lp
INNER JOIN categories AS c
    ON c.category_name = btrim(lp.category_name);

INSERT INTO orders (
    order_id,
    customer_id,
    status,
    ordered_at
)
OVERRIDING SYSTEM VALUE
SELECT
    order_id,
    customer_id,
    lower(status),
    ordered_at AT TIME ZONE 'America/Caracas'
FROM legacy_orders;

INSERT INTO order_items (
    order_id,
    product_id,
    quantity,
    unit_price
)
SELECT
    order_id,
    product_id,
    quantity,
    unit_price
FROM legacy_order_items;

SELECT setval(
    pg_get_serial_sequence('customers', 'customer_id'),
    (SELECT MAX(customer_id) FROM customers),
    true
);

SELECT setval(
    pg_get_serial_sequence('products', 'product_id'),
    (SELECT MAX(product_id) FROM products),
    true
);

SELECT setval(
    pg_get_serial_sequence('orders', 'order_id'),
    (SELECT MAX(order_id) FROM orders),
    true
);

CREATE VIEW migrated_order_summary AS
SELECT
    o.order_id,
    o.ordered_at,
    o.status,
    c.full_name AS customer_name,
    COUNT(oi.product_id) AS different_products,
    SUM(oi.quantity) AS total_units,
    SUM(oi.quantity * oi.unit_price) AS order_total
FROM orders AS o
INNER JOIN customers AS c
    ON c.customer_id = o.customer_id
INNER JOIN order_items AS oi
    ON oi.order_id = o.order_id
GROUP BY
    o.order_id,
    o.ordered_at,
    o.status,
    c.full_name;

SELECT
    'customers' AS entity_name,
    (SELECT COUNT(*) FROM legacy_customers) AS source_rows,
    (SELECT COUNT(*) FROM customers) AS migrated_rows
UNION ALL
SELECT
    'products',
    (SELECT COUNT(*) FROM legacy_products),
    (SELECT COUNT(*) FROM products)
UNION ALL
SELECT
    'orders',
    (SELECT COUNT(*) FROM legacy_orders),
    (SELECT COUNT(*) FROM orders)
UNION ALL
SELECT
    'order_items',
    (SELECT COUNT(*) FROM legacy_order_items),
    (SELECT COUNT(*) FROM order_items)
ORDER BY entity_name;

SELECT *
FROM migrated_order_summary
ORDER BY order_id;
