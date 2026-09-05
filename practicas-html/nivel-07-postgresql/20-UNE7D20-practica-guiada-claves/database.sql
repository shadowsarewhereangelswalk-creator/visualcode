DROP SCHEMA IF EXISTS une7d20_library_keys CASCADE;
CREATE SCHEMA une7d20_library_keys;
SET search_path TO une7d20_library_keys, public;

CREATE TABLE authors (
    author_id bigint GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    full_name text NOT NULL
);

CREATE TABLE books (
    book_id bigint GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    author_id bigint NOT NULL,
    isbn char(13) NOT NULL UNIQUE,
    title text NOT NULL,
    available_copies integer NOT NULL DEFAULT 1 CHECK (available_copies >= 0),
    CONSTRAINT fk_library_book_author
        FOREIGN KEY (author_id)
        REFERENCES authors(author_id)
        ON UPDATE CASCADE
        ON DELETE RESTRICT
);

CREATE TABLE members (
    member_id bigint GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    member_code varchar(12) NOT NULL UNIQUE,
    full_name text NOT NULL,
    email text NOT NULL UNIQUE
);

CREATE TABLE loans (
    loan_id bigint GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    member_id bigint NOT NULL,
    book_id bigint NOT NULL,
    loaned_on date NOT NULL,
    due_on date NOT NULL,
    returned_on date,
    CHECK (due_on >= loaned_on),
    CHECK (returned_on IS NULL OR returned_on >= loaned_on),
    CONSTRAINT fk_library_loan_member
        FOREIGN KEY (member_id)
        REFERENCES members(member_id)
        ON UPDATE CASCADE
        ON DELETE RESTRICT,
    CONSTRAINT fk_library_loan_book
        FOREIGN KEY (book_id)
        REFERENCES books(book_id)
        ON UPDATE CASCADE
        ON DELETE RESTRICT
);

CREATE UNIQUE INDEX uq_active_book_loan
ON loans (member_id, book_id)
WHERE returned_on IS NULL;

INSERT INTO authors (full_name)
VALUES
    ('Elena Torres'),
    ('Marco Ruiz');

INSERT INTO books (author_id, isbn, title, available_copies)
VALUES
    (1, '9781234567890', 'PostgreSQL desde Cero', 3),
    (2, '9780987654321', 'Diseño Relacional', 2);

INSERT INTO members (member_code, full_name, email)
VALUES
    ('MEM-0001', 'Ana Torres', 'ana@example.com'),
    ('MEM-0002', 'Bruno Díaz', 'bruno@example.com');

INSERT INTO loans (member_id, book_id, loaned_on, due_on)
VALUES
    (1, 1, '2027-01-20', '2027-02-03'),
    (2, 2, '2027-01-20', '2027-02-03');

SELECT
    l.loan_id,
    m.member_code,
    m.full_name AS member_name,
    b.isbn,
    b.title,
    a.full_name AS author_name,
    l.loaned_on,
    l.due_on
FROM loans AS l
INNER JOIN members AS m
    ON m.member_id = l.member_id
INNER JOIN books AS b
    ON b.book_id = l.book_id
INNER JOIN authors AS a
    ON a.author_id = b.author_id
ORDER BY l.due_on, l.loan_id;
