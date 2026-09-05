DROP DATABASE IF EXISTS une6d19_blog;
CREATE DATABASE une6d19_blog CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci;
USE une6d19_blog;

CREATE TABLE blog_users (
  user_id INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
  username VARCHAR(60) NOT NULL UNIQUE,
  display_name VARCHAR(120) NOT NULL
) ENGINE=InnoDB;

CREATE TABLE posts (
  post_id BIGINT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
  author_id INT UNSIGNED NOT NULL,
  title VARCHAR(180) NOT NULL,
  body TEXT NOT NULL,
  published_at DATETIME,
  CONSTRAINT fk_posts_author
    FOREIGN KEY (author_id) REFERENCES blog_users(user_id)
    ON UPDATE CASCADE
    ON DELETE RESTRICT
) ENGINE=InnoDB;

CREATE TABLE comments (
  comment_id BIGINT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
  post_id BIGINT UNSIGNED NOT NULL,
  author_id INT UNSIGNED NOT NULL,
  body VARCHAR(500) NOT NULL,
  created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  CONSTRAINT fk_comments_post
    FOREIGN KEY (post_id) REFERENCES posts(post_id)
    ON UPDATE CASCADE
    ON DELETE CASCADE,
  CONSTRAINT fk_comments_author
    FOREIGN KEY (author_id) REFERENCES blog_users(user_id)
    ON UPDATE CASCADE
    ON DELETE RESTRICT
) ENGINE=InnoDB;

INSERT INTO blog_users (username, display_name) VALUES
('ana.dev', 'Ana Pérez'),
('luis.sql', 'Luis Gómez'),
('marta.data', 'Marta Díaz');

INSERT INTO posts (author_id, title, body, published_at)
VALUES (1, 'Claves primarias', 'Una clave primaria identifica cada registro.', NOW());

SET @post_id = LAST_INSERT_ID();

INSERT INTO comments (post_id, author_id, body) VALUES
(@post_id, 2, 'El ejemplo de autoincremento quedó claro.'),
(@post_id, 3, 'También es útil combinar la clave con índices únicos.');

SELECT
  p.post_id,
  p.title,
  a.display_name AS author,
  COUNT(c.comment_id) AS comment_count
FROM posts AS p
INNER JOIN blog_users AS a ON a.user_id = p.author_id
LEFT JOIN comments AS c ON c.post_id = p.post_id
GROUP BY p.post_id, p.title, a.display_name;
