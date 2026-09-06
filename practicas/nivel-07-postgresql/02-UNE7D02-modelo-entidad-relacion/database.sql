DROP SCHEMA IF EXISTS une7d02_er_model CASCADE;
CREATE SCHEMA une7d02_er_model;
SET search_path TO une7d02_er_model, public;

CREATE TABLE publishers (
    publisher_id bigint GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    publisher_name text NOT NULL UNIQUE,
    country_code char(2) NOT NULL
);

CREATE TABLE authors (
    author_id bigint GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    full_name text NOT NULL,
    country_code char(2) NOT NULL
);

CREATE TABLE books (
    book_id bigint GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    publisher_id bigint NOT NULL,
    isbn char(13) NOT NULL UNIQUE,
    title text NOT NULL,
    publication_year integer NOT NULL CHECK (publication_year BETWEEN 1450 AND 2100),
    price numeric(10, 2) NOT NULL CHECK (price >= 0),
    CONSTRAINT fk_books_publisher
        FOREIGN KEY (publisher_id)
        REFERENCES publishers(publisher_id)
        ON UPDATE CASCADE
        ON DELETE RESTRICT
);

CREATE TABLE book_authors (
    book_id bigint NOT NULL,
    author_id bigint NOT NULL,
    author_order smallint NOT NULL CHECK (author_order > 0),
    PRIMARY KEY (book_id, author_id),
    UNIQUE (book_id, author_order),
    CONSTRAINT fk_book_authors_book
        FOREIGN KEY (book_id)
        REFERENCES books(book_id)
        ON UPDATE CASCADE
        ON DELETE CASCADE,
    CONSTRAINT fk_book_authors_author
        FOREIGN KEY (author_id)
        REFERENCES authors(author_id)
        ON UPDATE CASCADE
        ON DELETE RESTRICT
);

INSERT INTO publishers (publisher_name, country_code)
VALUES
    ('Editorial Horizonte', 'VE'),
    ('Ediciones Código', 'ES');

INSERT INTO authors (full_name, country_code)
VALUES
    ('Elena Torres', 'VE'),
    ('Marco Ruiz', 'ES'),
    ('Ana Pérez', 'CO');

INSERT INTO books (publisher_id, isbn, title, publication_year, price)
VALUES
    (1, '9781234567890', 'Diseño de Datos', 2026, 36.50),
    (2, '9780987654321', 'PostgreSQL Aplicado', 2027, 42.00);

INSERT INTO book_authors (book_id, author_id, author_order)
VALUES
    (1, 1, 1),
    (1, 3, 2),
    (2, 2, 1);

SELECT
    b.book_id,
    b.title,
    p.publisher_name,
    string_agg(a.full_name, ', ' ORDER BY ba.author_order) AS authors,
    b.publication_year,
    b.price
FROM books AS b
INNER JOIN publishers AS p ON p.publisher_id = b.publisher_id
INNER JOIN book_authors AS ba ON ba.book_id = b.book_id
INNER JOIN authors AS a ON a.author_id = ba.author_id
GROUP BY b.book_id, b.title, p.publisher_name, b.publication_year, b.price
ORDER BY b.title;
