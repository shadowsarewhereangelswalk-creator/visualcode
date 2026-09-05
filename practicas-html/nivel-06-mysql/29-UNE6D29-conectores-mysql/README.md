# UNE6D29 — Fundamentos de conectores MySQL: ODBC, .NET, JDBC y PHP

Clase 29 del Nivel 6 — MySQL.

- **Objetivo:** Comprender y aplicar fundamentos de conectores mysql: odbc, .net, jdbc y php dentro del objetivo del Nivel 6.
- **Conceptos:** Fundamentos de conectores MySQL: ODBC, .NET, JDBC y PHP
- **Herramientas:** MySQL, MySQL Workbench, SQL
- **Proyecto del nivel:** Base de datos para aplicación real
- **Ejercicio:** Realizar un ejemplo guiado de fundamentos de conectores mysql: odbc, .net, jdbc y php.
- **Entregable:** Resolver una práctica corta y responder preguntas de comprobación.
- **Archivos:** `database.sql`, `php-pdo.php`, `java-jdbc/App.java`, `dotnet/Program.cs`, `odbc-python/app.py` y `odbc-python/requirements.txt`

Abre `database.sql` en MySQL Workbench y ejecuta todo el script. El archivo recrea únicamente la base `une6d29_connectors` e incluye estructura, datos y consultas de comprobación terminadas.

## Ejemplos de conexión

Antes de ejecutar cualquier ejemplo, abre `database.sql` en MySQL Workbench y ejecuta todo el script.

Los cuatro ejemplos leen estas variables de entorno:

- `MYSQL_HOST`
- `MYSQL_PORT`
- `MYSQL_USER`
- `MYSQL_PASSWORD`

Para ODBC, crea un DSN que apunte a la base `une6d29_connectors` y define `MYSQL_ODBC_DSN` con su nombre.

### PHP con PDO

Requiere PHP con la extensión `pdo_mysql`.

```bash
php php-pdo.php
```

### Java con JDBC

Requiere Java 17 o superior y MySQL Connector/J en el classpath.

```bash
javac -cp "mysql-connector-j.jar" java-jdbc/App.java
java -cp "java-jdbc:mysql-connector-j.jar" App
```

En Windows sustituye `:` por `;` en el classpath.

### .NET

Crea un proyecto de consola, agrega MySQL Connector/NET y usa el archivo incluido como `Program.cs`.

```bash
dotnet new console -n ConnectorNet
cd ConnectorNet
dotnet add package MySql.Data
dotnet run
```

### ODBC con Python

Requiere el controlador MySQL Connector/ODBC y un DSN configurado.

```bash
python -m pip install -r odbc-python/requirements.txt
python odbc-python/app.py
```
