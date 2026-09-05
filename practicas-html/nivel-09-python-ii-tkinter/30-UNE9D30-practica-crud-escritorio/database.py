import os

from modelos import Cliente


def configuracion_mysql():
    return {
        "host": os.getenv("MYSQL_HOST", "127.0.0.1"),
        "port": int(os.getenv("MYSQL_PORT", "3306")),
        "user": os.getenv("MYSQL_USER", "root"),
        "password": os.getenv("MYSQL_PASSWORD", ""),
        "database": os.getenv("MYSQL_DATABASE", "ai_career"),
    }


class RepositorioClientes:
    def conectar(self):
        import mysql.connector

        return mysql.connector.connect(**configuracion_mysql())

    def listar(self, filtro=""):
        conexion = self.conectar()
        cursor = conexion.cursor(dictionary=True)
        try:
            termino = f"%{filtro.strip()}%"
            cursor.execute(
                "SELECT id, nombre, correo, telefono, servicio, activo "
                "FROM clientes "
                "WHERE nombre LIKE %s OR correo LIKE %s OR servicio LIKE %s "
                "ORDER BY nombre",
                (termino, termino, termino),
            )
            return [
                Cliente(
                    fila["id"],
                    fila["nombre"],
                    fila["correo"],
                    fila["telefono"],
                    fila["servicio"],
                    bool(fila["activo"]),
                )
                for fila in cursor.fetchall()
            ]
        finally:
            cursor.close()
            conexion.close()

    def insertar(self, cliente):
        conexion = self.conectar()
        cursor = conexion.cursor()
        try:
            cursor.execute(
                "INSERT INTO clientes (nombre, correo, telefono, servicio, activo) "
                "VALUES (%s, %s, %s, %s, %s)",
                (
                    cliente.nombre,
                    cliente.correo,
                    cliente.telefono,
                    cliente.servicio,
                    cliente.activo,
                ),
            )
            conexion.commit()
            return cursor.lastrowid
        except Exception:
            conexion.rollback()
            raise
        finally:
            cursor.close()
            conexion.close()

    def actualizar(self, cliente):
        conexion = self.conectar()
        cursor = conexion.cursor()
        try:
            cursor.execute(
                "UPDATE clientes "
                "SET nombre = %s, correo = %s, telefono = %s, servicio = %s, activo = %s "
                "WHERE id = %s",
                (
                    cliente.nombre,
                    cliente.correo,
                    cliente.telefono,
                    cliente.servicio,
                    cliente.activo,
                    cliente.id,
                ),
            )
            conexion.commit()
            return cursor.rowcount
        except Exception:
            conexion.rollback()
            raise
        finally:
            cursor.close()
            conexion.close()

    def eliminar(self, identificador):
        conexion = self.conectar()
        cursor = conexion.cursor()
        try:
            cursor.execute("DELETE FROM clientes WHERE id = %s", (identificador,))
            conexion.commit()
            return cursor.rowcount
        except Exception:
            conexion.rollback()
            raise
        finally:
            cursor.close()
            conexion.close()
