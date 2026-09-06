DROP DATABASE IF EXISTS une6d26_consolidated_view;
CREATE DATABASE une6d26_consolidated_view
CHARACTER SET utf8mb4
COLLATE utf8mb4_0900_ai_ci;

USE une6d26_consolidated_view;

CREATE TABLE customers (
    customer_id BIGINT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    full_name VARCHAR(120) NOT NULL,
    email VARCHAR(160) NOT NULL UNIQUE
) ENGINE = InnoDB;

CREATE TABLE products (
    product_id BIGINT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    product_name VARCHAR(140) NOT NULL,
    current_price DECIMAL(10, 2) NOT NULL,
    CONSTRAINT chk_product_price CHECK (current_price >= 0)
) ENGINE = InnoDB;

CREATE TABLE orders (
    order_id BIGINT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    customer_id BIGINT UNSIGNED NOT NULL,
    status ENUM('pending', 'paid', 'shipped', 'cancelled') NOT NULL DEFAULT 'pending',
    ordered_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT fk_orders_customer
        FOREIGN KEY (customer_id) REFERENCES customers(customer_id)
        ON UPDATE CASCADE
        ON DELETE RESTRICT
) ENGINE = InnoDB;

CREATE TABLE order_items (
    order_item_id BIGINT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    order_id BIGINT UNSIGNED NOT NULL,
    product_id BIGINT UNSIGNED NOT NULL,
    quantity SMALLINT UNSIGNED NOT NULL,
    unit_price DECIMAL(10, 2) NOT NULL,
    CONSTRAINT uq_order_product UNIQUE (order_id, product_id),
    CONSTRAINT chk_order_item_quantity CHECK (quantity > 0),
    CONSTRAINT chk_order_item_price CHECK (unit_price >= 0),
    CONSTRAINT fk_order_items_order
        FOREIGN KEY (order_id) REFERENCES orders(order_id)
        ON UPDATE CASCADE
        ON DELETE CASCADE,
    CONSTRAINT fk_order_items_product
        FOREIGN KEY (product_id) REFERENCES products(product_id)
        ON UPDATE CASCADE
        ON DELETE RESTRICT
) ENGINE = InnoDB;

INSERT INTO customers (full_name, email)
VALUES
    ('Ana Torres', 'ana@example.com'),
    ('Bruno Díaz', 'bruno@example.com');

INSERT INTO products (product_name, current_price)
VALUES
    ('Teclado mecánico', 89.90),
    ('Mouse ergonómico', 45.50),
    ('Monitor 27 pulgadas', 289.00);

INSERT INTO orders (customer_id, status, ordered_at)
VALUES
    (1, 'paid', '2026-08-15 10:20:00'),
    (2, 'shipped', '2026-08-16 14:45:00'),
    (1, 'pending', '2026-08-18 09:10:00');

INSERT INTO order_items (order_id, product_id, quantity, unit_price)
VALUES
    (1, 1, 1, 89.90),
    (1, 2, 2, 45.50),
    (2, 3, 1, 289.00),
    (2, 2, 1, 45.50),
    (3, 3, 2, 289.00);

CREATE OR REPLACE VIEW v_order_summary AS
SELECT
    o.order_id,
    o.ordered_at,
    o.status,
    c.customer_id,
    c.full_name AS customer_name,
    c.email,
    COUNT(DISTINCT oi.product_id) AS different_products,
    SUM(oi.quantity) AS total_units,
    ROUND(SUM(oi.quantity * oi.unit_price), 2) AS subtotal,
    ROUND(SUM(oi.quantity * oi.unit_price) * 0.19, 2) AS tax,
    ROUND(SUM(oi.quantity * oi.unit_price) * 1.19, 2) AS total
FROM orders AS o
INNER JOIN customers AS c
    ON c.customer_id = o.customer_id
INNER JOIN order_items AS oi
    ON oi.order_id = o.order_id
GROUP BY
    o.order_id,
    o.ordered_at,
    o.status,
    c.customer_id,
    c.full_name,
    c.email;

SELECT
    order_id,
    ordered_at,
    status,
    customer_name,
    different_products,
    total_units,
    subtotal,
    tax,
    total
FROM v_order_summary
ORDER BY ordered_at, order_id;

SELECT
    customer_name,
    COUNT(*) AS order_count,
    ROUND(SUM(total), 2) AS customer_total
FROM v_order_summary
GROUP BY customer_id, customer_name
ORDER BY customer_total DESC;
