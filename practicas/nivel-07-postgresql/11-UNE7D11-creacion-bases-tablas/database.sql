DROP SCHEMA IF EXISTS une7d11_app CASCADE;
CREATE SCHEMA une7d11_app;
SET search_path TO une7d11_app, public;

CREATE TABLE service_categories (
    category_id bigint GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    category_name text NOT NULL UNIQUE
);

CREATE TABLE services (
    service_id bigint GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    category_id bigint NOT NULL,
    service_name text NOT NULL,
    price numeric(10, 2) NOT NULL CHECK (price >= 0),
    active boolean NOT NULL DEFAULT true,
    created_at timestamptz NOT NULL DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT fk_service_category
        FOREIGN KEY (category_id)
        REFERENCES service_categories(category_id)
        ON UPDATE CASCADE
        ON DELETE RESTRICT
);

INSERT INTO service_categories (category_name)
VALUES ('Desarrollo'), ('Automatización');

INSERT INTO services (category_id, service_name, price)
VALUES (1, 'Sitio web profesional', 850.00), (2, 'Flujo automatizado', 450.00);

SELECT s.service_id, s.service_name, c.category_name, s.price, s.active, s.created_at
FROM services AS s
INNER JOIN service_categories AS c ON c.category_id = s.category_id
ORDER BY s.service_id;
