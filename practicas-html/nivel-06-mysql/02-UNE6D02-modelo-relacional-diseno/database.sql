DROP DATABASE IF EXISTS une6d02_relational;
CREATE DATABASE une6d02_relational CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci;
USE une6d02_relational;

CREATE TABLE authors (
  author_id INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
  full_name VARCHAR(120) NOT NULL,
  country VARCHAR(80) NOT NULL
) ENGINE=InnoDB;

CREATE TABLE books (
  book_id INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
  author_id INT UNSIGNED NOT NULL,
  title VARCHAR(180) NOT NULL,
  publication_year YEAR NOT NULL,
  price DECIMAL(10,2) NOT NULL CHECK (price >= 0),
  CONSTRAINT fk_books_authors
    FOREIGN KEY (author_id) REFERENCES authors(author_id)
    ON UPDATE CASCADE
    ON DELETE RESTRICT
) ENGINE=InnoDB;

INSERT INTO authors (full_name, country) VALUES
('Elena Torres', 'Venezuela'),
('Marco Ruiz', 'España');

INSERT INTO books (author_id, title, publication_year, price) VALUES
(1, 'Diseño de Datos', 2024, 32.50),
(1, 'SQL desde Cero', 2025, 28.00),
(2, 'Modelos Relacionales', 2023, 41.75);

SELECT
  b.book_id,
  b.title,
  b.publication_year,
  b.price,
  a.full_name AS author,
  a.country
FROM books AS b
INNER JOIN authors AS a ON a.author_id = b.author_id
ORDER BY a.full_name, b.title;
