DROP DATABASE IF EXISTS une6d10_purchases;
CREATE DATABASE une6d10_purchases CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci;
USE une6d10_purchases;

CREATE TABLE suppliers (
  supplier_id INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
  name VARCHAR(120) NOT NULL,
  email VARCHAR(160) NOT NULL UNIQUE
) ENGINE=InnoDB;

CREATE TABLE supplies (
  supply_id INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
  name VARCHAR(120) NOT NULL,
  unit_cost DECIMAL(10,2) NOT NULL CHECK (unit_cost >= 0)
) ENGINE=InnoDB;

CREATE TABLE purchases (
  purchase_id BIGINT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
  supplier_id INT UNSIGNED NOT NULL,
  purchase_date DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
  status ENUM('Registrada','Recibida','Cancelada') NOT NULL DEFAULT 'Registrada',
  CONSTRAINT fk_purchases_supplier
    FOREIGN KEY (supplier_id) REFERENCES suppliers(supplier_id)
    ON UPDATE CASCADE
    ON DELETE RESTRICT
) ENGINE=InnoDB;

CREATE TABLE purchase_items (
  purchase_id BIGINT UNSIGNED NOT NULL,
  supply_id INT UNSIGNED NOT NULL,
  quantity INT UNSIGNED NOT NULL CHECK (quantity > 0),
  unit_cost DECIMAL(10,2) NOT NULL CHECK (unit_cost >= 0),
  PRIMARY KEY (purchase_id, supply_id),
  CONSTRAINT fk_purchase_items_purchase
    FOREIGN KEY (purchase_id) REFERENCES purchases(purchase_id)
    ON UPDATE CASCADE
    ON DELETE CASCADE,
  CONSTRAINT fk_purchase_items_supply
    FOREIGN KEY (supply_id) REFERENCES supplies(supply_id)
    ON UPDATE CASCADE
    ON DELETE RESTRICT
) ENGINE=InnoDB;

INSERT INTO suppliers (name, email) VALUES
('Distribuciones Norte', 'ventas@norte.example'),
('Suministros Centro', 'contacto@centro.example');

INSERT INTO supplies (name, unit_cost) VALUES
('Caja mediana', 2.80),
('Cinta de embalaje', 1.45),
('Etiqueta térmica', 0.12);

INSERT INTO purchases (supplier_id) VALUES (1);
SET @purchase_id = LAST_INSERT_ID();

INSERT INTO purchase_items (purchase_id, supply_id, quantity, unit_cost) VALUES
(@purchase_id, 1, 100, 2.80),
(@purchase_id, 2, 60, 1.45),
(@purchase_id, 3, 500, 0.12);

SELECT
  p.purchase_id,
  s.name AS supplier,
  p.purchase_date,
  p.status,
  SUM(pi.quantity * pi.unit_cost) AS purchase_total
FROM purchases AS p
INNER JOIN suppliers AS s ON s.supplier_id = p.supplier_id
INNER JOIN purchase_items AS pi ON pi.purchase_id = p.purchase_id
GROUP BY p.purchase_id, s.name, p.purchase_date, p.status;
