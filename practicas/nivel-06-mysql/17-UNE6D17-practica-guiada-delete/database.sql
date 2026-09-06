DROP DATABASE IF EXISTS une6d17_cleanup;
CREATE DATABASE une6d17_cleanup CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci;
USE une6d17_cleanup;

CREATE TABLE shopping_carts (
  cart_id INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
  customer_email VARCHAR(160) NOT NULL,
  status ENUM('Activo','Convertido','Abandonado') NOT NULL,
  updated_at DATETIME NOT NULL
) ENGINE=InnoDB;

CREATE TABLE cart_items (
  cart_item_id BIGINT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
  cart_id INT UNSIGNED NOT NULL,
  product_name VARCHAR(120) NOT NULL,
  quantity INT UNSIGNED NOT NULL,
  CONSTRAINT fk_cart_items_cart
    FOREIGN KEY (cart_id) REFERENCES shopping_carts(cart_id)
    ON UPDATE CASCADE
    ON DELETE CASCADE
) ENGINE=InnoDB;

CREATE TABLE cart_cleanup_log (
  log_id BIGINT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
  cart_id INT UNSIGNED NOT NULL,
  customer_email VARCHAR(160) NOT NULL,
  deleted_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB;

INSERT INTO shopping_carts (customer_email, status, updated_at) VALUES
('ana@example.com', 'Activo', '2026-12-15 10:00:00'),
('luis@example.com', 'Abandonado', '2026-08-01 08:00:00'),
('marta@example.com', 'Abandonado', '2026-09-10 12:00:00'),
('carlos@example.com', 'Convertido', '2026-12-12 16:00:00');

INSERT INTO cart_items (cart_id, product_name, quantity) VALUES
(1, 'Curso MySQL', 1),
(2, 'Plantilla Web', 1),
(2, 'Guía SQL', 2),
(3, 'Kit UI', 1),
(4, 'Curso JavaScript', 1);

SELECT cart_id, customer_email, updated_at
FROM shopping_carts
WHERE status = 'Abandonado'
  AND updated_at < '2026-10-01';

START TRANSACTION;

INSERT INTO cart_cleanup_log (cart_id, customer_email)
SELECT cart_id, customer_email
FROM shopping_carts
WHERE status = 'Abandonado'
  AND updated_at < '2026-10-01';

DELETE FROM shopping_carts
WHERE status = 'Abandonado'
  AND updated_at < '2026-10-01';

COMMIT;

SELECT * FROM shopping_carts ORDER BY cart_id;
SELECT * FROM cart_items ORDER BY cart_item_id;
SELECT * FROM cart_cleanup_log ORDER BY log_id;
