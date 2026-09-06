DROP DATABASE IF EXISTS une6d22_library;
CREATE DATABASE une6d22_library CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci;
USE une6d22_library;

CREATE TABLE members (
  member_id INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
  full_name VARCHAR(120) NOT NULL,
  email VARCHAR(160) NOT NULL UNIQUE,
  active BOOLEAN NOT NULL DEFAULT TRUE
) ENGINE=InnoDB;

CREATE TABLE authors (
  author_id INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
  full_name VARCHAR(120) NOT NULL
) ENGINE=InnoDB;

CREATE TABLE books (
  book_id INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
  author_id INT UNSIGNED NOT NULL,
  isbn CHAR(13) NOT NULL UNIQUE,
  title VARCHAR(180) NOT NULL,
  available_copies SMALLINT UNSIGNED NOT NULL DEFAULT 1,
  CONSTRAINT fk_books_author
    FOREIGN KEY (author_id) REFERENCES authors(author_id)
    ON UPDATE CASCADE
    ON DELETE RESTRICT
) ENGINE=InnoDB;

CREATE TABLE loans (
  loan_id BIGINT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
  member_id INT UNSIGNED NOT NULL,
  book_id INT UNSIGNED NOT NULL,
  loaned_on DATE NOT NULL,
  due_on DATE NOT NULL,
  returned_on DATE,
  CONSTRAINT fk_loans_member
    FOREIGN KEY (member_id) REFERENCES members(member_id)
    ON UPDATE CASCADE
    ON DELETE RESTRICT,
  CONSTRAINT fk_loans_book
    FOREIGN KEY (book_id) REFERENCES books(book_id)
    ON UPDATE CASCADE
    ON DELETE RESTRICT,
  CHECK (due_on >= loaned_on),
  CHECK (returned_on IS NULL OR returned_on >= loaned_on)
) ENGINE=InnoDB;

INSERT INTO members (full_name, email) VALUES
('Ana Pérez', 'ana@example.com'),
('Luis Gómez', 'luis@example.com');

INSERT INTO authors (full_name) VALUES
('Elena Torres'),
('Marco Ruiz');

INSERT INTO books (author_id, isbn, title, available_copies) VALUES
(1, '9781234567890', 'SQL desde Cero', 3),
(2, '9780987654321', 'Diseño Relacional', 2);

INSERT INTO loans (member_id, book_id, loaned_on, due_on) VALUES
(1, 1, '2026-12-10', '2026-12-24'),
(2, 2, '2026-12-12', '2026-12-26');

SELECT
  l.loan_id,
  m.full_name AS member,
  b.title AS book,
  a.full_name AS author,
  l.loaned_on,
  l.due_on,
  l.returned_on
FROM loans AS l
INNER JOIN members AS m ON m.member_id = l.member_id
INNER JOIN books AS b ON b.book_id = l.book_id
INNER JOIN authors AS a ON a.author_id = b.author_id
ORDER BY l.due_on;
