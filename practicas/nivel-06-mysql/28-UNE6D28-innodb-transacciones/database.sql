DROP DATABASE IF EXISTS une6d28_transactions;
CREATE DATABASE une6d28_transactions
CHARACTER SET utf8mb4
COLLATE utf8mb4_0900_ai_ci;

USE une6d28_transactions;

CREATE TABLE bank_accounts (
    account_id BIGINT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    holder_name VARCHAR(120) NOT NULL,
    balance DECIMAL(12, 2) NOT NULL DEFAULT 0,
    updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    CONSTRAINT chk_account_balance CHECK (balance >= 0)
) ENGINE = InnoDB;

CREATE TABLE transfers (
    transfer_id BIGINT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    source_account_id BIGINT UNSIGNED NOT NULL,
    destination_account_id BIGINT UNSIGNED NOT NULL,
    amount DECIMAL(12, 2) NOT NULL,
    transferred_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT chk_transfer_amount CHECK (amount > 0),
    CONSTRAINT chk_different_accounts CHECK (source_account_id <> destination_account_id),
    CONSTRAINT fk_transfer_source
        FOREIGN KEY (source_account_id) REFERENCES bank_accounts(account_id)
        ON UPDATE CASCADE
        ON DELETE RESTRICT,
    CONSTRAINT fk_transfer_destination
        FOREIGN KEY (destination_account_id) REFERENCES bank_accounts(account_id)
        ON UPDATE CASCADE
        ON DELETE RESTRICT
) ENGINE = InnoDB;

INSERT INTO bank_accounts (holder_name, balance)
VALUES
    ('Ana Torres', 1500.00),
    ('Bruno Díaz', 800.00);

DELIMITER $$

CREATE PROCEDURE transfer_funds (
    IN p_source_account_id BIGINT UNSIGNED,
    IN p_destination_account_id BIGINT UNSIGNED,
    IN p_amount DECIMAL(12, 2)
)
BEGIN
    DECLARE v_source_balance DECIMAL(12, 2) DEFAULT NULL;
    DECLARE v_destination_balance DECIMAL(12, 2) DEFAULT NULL;

    DECLARE EXIT HANDLER FOR SQLEXCEPTION
    BEGIN
        ROLLBACK;
        RESIGNAL;
    END;

    IF p_amount IS NULL OR p_amount <= 0 THEN
        SIGNAL SQLSTATE '45000'
            SET MESSAGE_TEXT = 'El monto debe ser mayor que cero';
    END IF;

    IF p_source_account_id = p_destination_account_id THEN
        SIGNAL SQLSTATE '45000'
            SET MESSAGE_TEXT = 'Las cuentas deben ser diferentes';
    END IF;

    START TRANSACTION;

    SELECT balance
    INTO v_source_balance
    FROM bank_accounts
    WHERE account_id = p_source_account_id
    FOR UPDATE;

    SELECT balance
    INTO v_destination_balance
    FROM bank_accounts
    WHERE account_id = p_destination_account_id
    FOR UPDATE;

    IF v_source_balance IS NULL OR v_destination_balance IS NULL THEN
        SIGNAL SQLSTATE '45000'
            SET MESSAGE_TEXT = 'Una de las cuentas no existe';
    END IF;

    IF v_source_balance < p_amount THEN
        SIGNAL SQLSTATE '45000'
            SET MESSAGE_TEXT = 'Saldo insuficiente';
    END IF;

    UPDATE bank_accounts
    SET balance = balance - p_amount
    WHERE account_id = p_source_account_id;

    UPDATE bank_accounts
    SET balance = balance + p_amount
    WHERE account_id = p_destination_account_id;

    SAVEPOINT balances_transferred;

    UPDATE bank_accounts
    SET balance = balance - 15.00
    WHERE account_id = p_source_account_id;

    ROLLBACK TO SAVEPOINT balances_transferred;
    RELEASE SAVEPOINT balances_transferred;

    INSERT INTO transfers (
        source_account_id,
        destination_account_id,
        amount
    )
    VALUES (
        p_source_account_id,
        p_destination_account_id,
        p_amount
    );

    COMMIT;
END$$

DELIMITER ;

SET TRANSACTION ISOLATION LEVEL READ COMMITTED;
CALL transfer_funds(1, 2, 250.00);

SELECT
    account_id,
    holder_name,
    balance,
    updated_at
FROM bank_accounts
ORDER BY account_id;

SELECT
    transfer_id,
    source_account_id,
    destination_account_id,
    amount,
    transferred_at
FROM transfers
ORDER BY transfer_id;
