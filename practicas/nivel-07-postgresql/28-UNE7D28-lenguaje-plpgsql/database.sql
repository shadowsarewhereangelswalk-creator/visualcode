DROP SCHEMA IF EXISTS une7d28_plpgsql CASCADE;
CREATE SCHEMA une7d28_plpgsql;
SET search_path TO une7d28_plpgsql, public;

CREATE TABLE quote_requests (
    request_id bigint GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    customer_name text NOT NULL,
    customer_type text NOT NULL
        CHECK (customer_type IN ('regular', 'premium', 'partner')),
    subtotal numeric(12, 2) NOT NULL CHECK (subtotal >= 0),
    created_at timestamptz NOT NULL DEFAULT CURRENT_TIMESTAMP
);

CREATE OR REPLACE FUNCTION calculate_quote(
    requested_subtotal numeric,
    requested_customer_type text
)
RETURNS TABLE (
    discount numeric,
    tax numeric,
    total numeric
)
LANGUAGE plpgsql
AS $function$
DECLARE
    discount_rate numeric := 0;
    discount_amount numeric;
    taxable_amount numeric;
BEGIN
    IF requested_subtotal < 0 THEN
        RAISE EXCEPTION 'El subtotal no puede ser negativo';
    END IF;

    IF requested_customer_type = 'premium' THEN
        discount_rate := 0.10;
    ELSIF requested_customer_type = 'partner' THEN
        discount_rate := 0.15;
    ELSIF requested_customer_type <> 'regular' THEN
        RAISE EXCEPTION 'El tipo de cliente no es válido';
    END IF;

    discount_amount := round(requested_subtotal * discount_rate, 2);
    taxable_amount := requested_subtotal - discount_amount;

    RETURN QUERY
    SELECT
        discount_amount,
        round(taxable_amount * 0.16, 2),
        round(taxable_amount * 1.16, 2);
END;
$function$;

INSERT INTO quote_requests (customer_name, customer_type, subtotal)
VALUES
    ('Ana Torres', 'premium', 850.00),
    ('Bruno Díaz', 'regular', 450.00),
    ('Carla Méndez', 'partner', 1200.00);

SELECT
    qr.request_id,
    qr.customer_name,
    qr.customer_type,
    qr.subtotal,
    calculation.discount,
    calculation.tax,
    calculation.total
FROM quote_requests AS qr
CROSS JOIN LATERAL calculate_quote(
    qr.subtotal,
    qr.customer_type
) AS calculation
ORDER BY qr.request_id;
