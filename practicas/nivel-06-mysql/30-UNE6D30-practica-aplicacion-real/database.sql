DROP DATABASE IF EXISTS une6d30_real_application;
CREATE DATABASE une6d30_real_application
CHARACTER SET utf8mb4
COLLATE utf8mb4_0900_ai_ci;

USE une6d30_real_application;

CREATE TABLE users (
    user_id BIGINT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    full_name VARCHAR(120) NOT NULL,
    email VARCHAR(160) NOT NULL UNIQUE,
    role_name ENUM('customer', 'administrator') NOT NULL DEFAULT 'customer',
    active BOOLEAN NOT NULL DEFAULT TRUE,
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
) ENGINE = InnoDB;

CREATE TABLE categories (
    category_id BIGINT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    category_name VARCHAR(100) NOT NULL UNIQUE
) ENGINE = InnoDB;

CREATE TABLE products (
    product_id BIGINT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    category_id BIGINT UNSIGNED NOT NULL,
    product_name VARCHAR(140) NOT NULL,
    price DECIMAL(10, 2) NOT NULL,
    stock INT UNSIGNED NOT NULL DEFAULT 0,
    active BOOLEAN NOT NULL DEFAULT TRUE,
    CONSTRAINT chk_real_product_price CHECK (price >= 0),
    CONSTRAINT fk_real_product_category
        FOREIGN KEY (category_id) REFERENCES categories(category_id)
        ON UPDATE CASCADE
        ON DELETE RESTRICT
) ENGINE = InnoDB;

CREATE TABLE orders (
    order_id BIGINT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    user_id BIGINT UNSIGNED NOT NULL,
    status ENUM('pending', 'paid', 'preparing', 'shipped', 'cancelled') NOT NULL DEFAULT 'pending',
    total DECIMAL(12, 2) NOT NULL DEFAULT 0,
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT chk_real_order_total CHECK (total >= 0),
    CONSTRAINT fk_real_order_user
        FOREIGN KEY (user_id) REFERENCES users(user_id)
        ON UPDATE CASCADE
        ON DELETE RESTRICT
) ENGINE = InnoDB;

CREATE TABLE order_items (
    order_item_id BIGINT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    order_id BIGINT UNSIGNED NOT NULL,
    product_id BIGINT UNSIGNED NOT NULL,
    quantity INT UNSIGNED NOT NULL,
    unit_price DECIMAL(10, 2) NOT NULL,
    CONSTRAINT uq_real_order_product UNIQUE (order_id, product_id),
    CONSTRAINT chk_real_item_quantity CHECK (quantity > 0),
    CONSTRAINT chk_real_item_price CHECK (unit_price >= 0),
    CONSTRAINT fk_real_item_order
        FOREIGN KEY (order_id) REFERENCES orders(order_id)
        ON UPDATE CASCADE
        ON DELETE CASCADE,
    CONSTRAINT fk_real_item_product
        FOREIGN KEY (product_id) REFERENCES products(product_id)
        ON UPDATE CASCADE
        ON DELETE RESTRICT
) ENGINE = InnoDB;

CREATE TABLE payments (
    payment_id BIGINT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    order_id BIGINT UNSIGNED NOT NULL UNIQUE,
    amount DECIMAL(12, 2) NOT NULL,
    payment_method ENUM('card', 'transfer', 'cash') NOT NULL,
    payment_status ENUM('pending', 'approved', 'rejected') NOT NULL DEFAULT 'pending',
    paid_at DATETIME NULL,
    CONSTRAINT chk_real_payment_amount CHECK (amount > 0),
    CONSTRAINT fk_real_payment_order
        FOREIGN KEY (order_id) REFERENCES orders(order_id)
        ON UPDATE CASCADE
        ON DELETE RESTRICT
) ENGINE = InnoDB;

CREATE TABLE inventory_movements (
    movement_id BIGINT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    product_id BIGINT UNSIGNED NOT NULL,
    movement_type ENUM('entry', 'sale', 'adjustment') NOT NULL,
    quantity_change INT NOT NULL,
    reference_code VARCHAR(40) NOT NULL,
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT fk_real_movement_product
        FOREIGN KEY (product_id) REFERENCES products(product_id)
        ON UPDATE CASCADE
        ON DELETE RESTRICT
) ENGINE = InnoDB;

CREATE TABLE order_status_audit (
    audit_id BIGINT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    order_id BIGINT UNSIGNED NOT NULL,
    previous_status VARCHAR(20) NOT NULL,
    new_status VARCHAR(20) NOT NULL,
    changed_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    changed_by VARCHAR(288) NOT NULL,
    CONSTRAINT fk_real_audit_order
        FOREIGN KEY (order_id) REFERENCES orders(order_id)
        ON UPDATE CASCADE
        ON DELETE CASCADE
) ENGINE = InnoDB;

INSERT INTO users (full_name, email, role_name)
VALUES
    ('Ana Torres', 'ana@example.com', 'customer'),
    ('Bruno Díaz', 'bruno@example.com', 'customer'),
    ('Carla Méndez', 'carla@example.com', 'administrator');

INSERT INTO categories (category_name)
VALUES ('Tecnología'), ('Hogar');

INSERT INTO products (category_id, product_name, price, stock)
VALUES
    (1, 'Teclado mecánico', 89.90, 15),
    (1, 'Mouse ergonómico', 45.50, 30),
    (2, 'Lámpara de escritorio', 39.90, 20);

DELIMITER $$

CREATE TRIGGER trg_real_order_status_audit
AFTER UPDATE ON orders
FOR EACH ROW
BEGIN
    IF NOT (OLD.status <=> NEW.status) THEN
        INSERT INTO order_status_audit (
            order_id,
            previous_status,
            new_status,
            changed_by
        )
        VALUES (
            NEW.order_id,
            OLD.status,
            NEW.status,
            CURRENT_USER()
        );
    END IF;
END$$

CREATE PROCEDURE create_single_product_order (
    IN p_user_id BIGINT UNSIGNED,
    IN p_product_id BIGINT UNSIGNED,
    IN p_quantity INT UNSIGNED,
    OUT p_order_id BIGINT UNSIGNED
)
BEGIN
    DECLARE v_price DECIMAL(10, 2) DEFAULT NULL;
    DECLARE v_stock INT UNSIGNED DEFAULT NULL;
    DECLARE v_total DECIMAL(12, 2) DEFAULT NULL;

    DECLARE EXIT HANDLER FOR SQLEXCEPTION
    BEGIN
        ROLLBACK;
        RESIGNAL;
    END;

    IF p_quantity IS NULL OR p_quantity = 0 THEN
        SIGNAL SQLSTATE '45000'
            SET MESSAGE_TEXT = 'La cantidad debe ser mayor que cero';
    END IF;

    START TRANSACTION;

    SELECT price, stock
    INTO v_price, v_stock
    FROM products
    WHERE product_id = p_product_id
      AND active = TRUE
    FOR UPDATE;

    IF v_price IS NULL THEN
        SIGNAL SQLSTATE '45000'
            SET MESSAGE_TEXT = 'El producto no existe o está inactivo';
    END IF;

    IF v_stock < p_quantity THEN
        SIGNAL SQLSTATE '45000'
            SET MESSAGE_TEXT = 'No hay existencias suficientes';
    END IF;

    SET v_total = v_price * p_quantity;

    INSERT INTO orders (user_id, total)
    VALUES (p_user_id, v_total);

    SET p_order_id = LAST_INSERT_ID();

    INSERT INTO order_items (
        order_id,
        product_id,
        quantity,
        unit_price
    )
    VALUES (
        p_order_id,
        p_product_id,
        p_quantity,
        v_price
    );

    UPDATE products
    SET stock = stock - p_quantity
    WHERE product_id = p_product_id;

    INSERT INTO inventory_movements (
        product_id,
        movement_type,
        quantity_change,
        reference_code
    )
    VALUES (
        p_product_id,
        'sale',
        -CAST(p_quantity AS SIGNED),
        CONCAT('ORDER-', p_order_id)
    );

    INSERT INTO payments (
        order_id,
        amount,
        payment_method,
        payment_status
    )
    VALUES (
        p_order_id,
        v_total,
        'card',
        'pending'
    );

    COMMIT;
END$$

DELIMITER ;

CALL create_single_product_order(1, 1, 2, @new_order_id);

UPDATE payments
SET payment_status = 'approved',
    paid_at = CURRENT_TIMESTAMP
WHERE order_id = @new_order_id;

UPDATE orders
SET status = 'paid'
WHERE order_id = @new_order_id;

CREATE OR REPLACE VIEW v_order_details AS
SELECT
    o.order_id,
    o.created_at,
    o.status,
    u.full_name AS customer_name,
    u.email,
    p.product_name,
    oi.quantity,
    oi.unit_price,
    oi.quantity * oi.unit_price AS line_total,
    o.total,
    pay.payment_method,
    pay.payment_status,
    pay.paid_at
FROM orders AS o
INNER JOIN users AS u
    ON u.user_id = o.user_id
INNER JOIN order_items AS oi
    ON oi.order_id = o.order_id
INNER JOIN products AS p
    ON p.product_id = oi.product_id
LEFT JOIN payments AS pay
    ON pay.order_id = o.order_id;

SELECT *
FROM v_order_details
ORDER BY order_id, product_name;

SELECT
    product_id,
    product_name,
    stock
FROM products
ORDER BY product_id;

SELECT
    audit_id,
    order_id,
    previous_status,
    new_status,
    changed_at,
    changed_by
FROM order_status_audit
ORDER BY audit_id;
