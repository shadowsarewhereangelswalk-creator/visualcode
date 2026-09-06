<?php

declare(strict_types=1);

$host = getenv('MYSQL_HOST') ?: '127.0.0.1';
$port = getenv('MYSQL_PORT') ?: '3306';
$user = getenv('MYSQL_USER') ?: 'root';
$password = getenv('MYSQL_PASSWORD') ?: '';

$dsn = sprintf(
    'mysql:host=%s;port=%s;dbname=une6d29_connectors;charset=utf8mb4',
    $host,
    $port
);

$connection = new PDO(
    $dsn,
    $user,
    $password,
    [
        PDO::ATTR_ERRMODE => PDO::ERRMODE_EXCEPTION,
        PDO::ATTR_DEFAULT_FETCH_MODE => PDO::FETCH_ASSOC
    ]
);

$statement = $connection->prepare(
    'SELECT contact_id, full_name, email, city, created_at
     FROM contacts
     ORDER BY contact_id'
);
$statement->execute();

echo json_encode(
    $statement->fetchAll(),
    JSON_PRETTY_PRINT | JSON_UNESCAPED_UNICODE | JSON_THROW_ON_ERROR
);
