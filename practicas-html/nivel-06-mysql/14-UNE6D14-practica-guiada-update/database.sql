DROP DATABASE IF EXISTS une6d14_inventory;
CREATE DATABASE une6d14_inventory CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci;
USE une6d14_inventory;

CREATE TABLE inventory (
  product_id INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
  sku VARCHAR(20) NOT NULL UNIQUE,
  name VARCHAR(120) NOT NULL,
  stock INT UNSIGNED NOT NULL,
  minimum_stock INT UNSIGNED NOT NULL DEFAULT 5,
  price DECIMAL(10,2) NOT NULL,
  status ENUM('Activo','Pausado','Agotado') NOT NULL DEFAULT 'Activo',
  updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
) ENGINE=InnoDB;

INSERT INTO inventory (sku, name, stock, minimum_stock, price, status) VALUES
('PRD-001', 'Teclado', 14, 5, 68.00, 'Activo'),
('PRD-002', 'Ratón', 3, 6, 32.00, 'Activo'),
('PRD-003', 'Monitor', 0, 2, 190.00, 'Activo'),
('PRD-004', 'Cámara web', 9, 4, 74.00, 'Pausado');

UPDATE inventory
SET stock = stock + 10
WHERE sku = 'PRD-002';

UPDATE inventory
SET price = ROUND(price * 0.90, 2)
WHERE status = 'Activo'
  AND stock > minimum_stock;

UPDATE inventory
SET status = 'Agotado'
WHERE stock = 0
  AND status <> 'Agotado';

UPDATE inventory
SET status = 'Activo'
WHERE sku = 'PRD-004'
  AND stock > 0;

SELECT
  product_id,
  sku,
  name,
  stock,
  minimum_stock,
  price,
  status,
  CASE
    WHEN stock = 0 THEN 'Sin existencias'
    WHEN stock <= minimum_stock THEN 'Reponer pronto'
    ELSE 'Inventario suficiente'
  END AS inventory_health
FROM inventory
ORDER BY product_id;
