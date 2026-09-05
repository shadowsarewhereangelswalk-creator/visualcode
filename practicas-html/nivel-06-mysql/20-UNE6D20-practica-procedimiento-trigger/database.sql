DROP DATABASE IF EXISTS une6d20_automation;
CREATE DATABASE une6d20_automation CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci;
USE une6d20_automation;

CREATE TABLE products (
  product_id INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
  sku VARCHAR(20) NOT NULL UNIQUE,
  name VARCHAR(120) NOT NULL,
  stock INT NOT NULL DEFAULT 0 CHECK (stock >= 0),
  updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
) ENGINE=InnoDB;

CREATE TABLE stock_movements (
  movement_id BIGINT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
  product_id INT UNSIGNED NOT NULL,
  quantity_change INT NOT NULL,
  reason VARCHAR(180) NOT NULL,
  created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  CONSTRAINT fk_movements_product
    FOREIGN KEY (product_id) REFERENCES products(product_id)
    ON UPDATE CASCADE
    ON DELETE RESTRICT
) ENGINE=InnoDB;

CREATE TABLE stock_audit (
  audit_id BIGINT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
  product_id INT UNSIGNED NOT NULL,
  old_stock INT NOT NULL,
  new_stock INT NOT NULL,
  changed_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB;

INSERT INTO products (sku, name, stock) VALUES
('DB-001', 'Curso MySQL', 20),
('DB-002', 'Guía SQL', 35);

DELIMITER $$

CREATE TRIGGER trg_products_stock_audit
AFTER UPDATE ON products
FOR EACH ROW
BEGIN
  IF OLD.stock <> NEW.stock THEN
    INSERT INTO stock_audit (product_id, old_stock, new_stock)
    VALUES (NEW.product_id, OLD.stock, NEW.stock);
  END IF;
END$$

CREATE PROCEDURE register_stock_movement (
  IN p_product_id INT UNSIGNED,
  IN p_quantity_change INT,
  IN p_reason VARCHAR(180)
)
BEGIN
  DECLARE v_current_stock INT DEFAULT NULL;
  DECLARE EXIT HANDLER FOR SQLEXCEPTION
  BEGIN
    ROLLBACK;
    RESIGNAL;
  END;

  START TRANSACTION;

  SELECT stock
  INTO v_current_stock
  FROM products
  WHERE product_id = p_product_id
  FOR UPDATE;

  IF v_current_stock IS NULL THEN
    SIGNAL SQLSTATE '45000'
      SET MESSAGE_TEXT = 'El producto no existe';
  END IF;

  IF v_current_stock + p_quantity_change < 0 THEN
    SIGNAL SQLSTATE '45000'
      SET MESSAGE_TEXT = 'El movimiento dejaría un stock negativo';
  END IF;

  INSERT INTO stock_movements (product_id, quantity_change, reason)
  VALUES (p_product_id, p_quantity_change, p_reason);

  UPDATE products
  SET stock = stock + p_quantity_change
  WHERE product_id = p_product_id;

  COMMIT;
END$$

DELIMITER ;

CALL register_stock_movement(1, 8, 'Reposición de inventario');
CALL register_stock_movement(1, -3, 'Venta confirmada');

SELECT * FROM products ORDER BY product_id;
SELECT * FROM stock_movements ORDER BY movement_id;
SELECT * FROM stock_audit ORDER BY audit_id;
