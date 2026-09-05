import os
import sys
import tkinter as tk
from tkinter import ttk


def configuracion_desde_entorno():
    return {
        "host": os.getenv("MYSQL_HOST", "127.0.0.1"),
        "port": int(os.getenv("MYSQL_PORT", "3306")),
        "user": os.getenv("MYSQL_USER", "root"),
        "password": os.getenv("MYSQL_PASSWORD", ""),
        "database": os.getenv("MYSQL_DATABASE", "ai_career"),
    }


def probar_conexion(configuracion):
    import mysql.connector

    conexion = mysql.connector.connect(**configuracion)
    cursor = conexion.cursor()
    try:
        cursor.execute("SELECT DATABASE(), VERSION(), CURRENT_USER()")
        base_datos, version, usuario = cursor.fetchone()
        return {
            "base_datos": base_datos,
            "version": version,
            "usuario": usuario,
        }
    finally:
        cursor.close()
        conexion.close()


class ConexionTkinterMySQL(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("P4 — Conexión Tkinter a MySQL")
        self.geometry("640x500")
        self.resizable(False, False)
        valores = configuracion_desde_entorno()
        self.host = tk.StringVar(value=valores["host"])
        self.puerto = tk.StringVar(value=str(valores["port"]))
        self.usuario = tk.StringVar(value=valores["user"])
        self.clave = tk.StringVar(value=valores["password"])
        self.base_datos = tk.StringVar(value=valores["database"])
        self.estado = tk.StringVar(value="Completa los datos y prueba la conexión")
        self.crear_interfaz()

    def crear_interfaz(self):
        panel = ttk.Frame(self, padding=30)
        panel.pack(fill="both", expand=True)
        ttk.Label(panel, text="Conexión a MySQL", font=("TkDefaultFont", 19, "bold")).grid(column=0, row=0, columnspan=2, sticky="w", pady=(0, 22))

        campos = (
            ("Servidor", self.host, False),
            ("Puerto", self.puerto, False),
            ("Usuario", self.usuario, False),
            ("Contraseña", self.clave, True),
            ("Base de datos", self.base_datos, False),
        )
        for fila, (texto, variable, es_clave) in enumerate(campos, start=1):
            ttk.Label(panel, text=texto).grid(column=0, row=fila, sticky="w", pady=7)
            ttk.Entry(
                panel,
                textvariable=variable,
                show="•" if es_clave else "",
            ).grid(column=1, row=fila, sticky="ew", pady=7)

        ttk.Button(panel, text="Probar conexión", command=self.conectar).grid(column=1, row=6, sticky="e", pady=(20, 0))
        ttk.Label(panel, textvariable=self.estado, wraplength=540).grid(column=0, row=7, columnspan=2, sticky="w", pady=(22, 0))
        panel.columnconfigure(1, weight=1)

    def conectar(self):
        try:
            configuracion = {
                "host": self.host.get().strip(),
                "port": int(self.puerto.get()),
                "user": self.usuario.get().strip(),
                "password": self.clave.get(),
                "database": self.base_datos.get().strip(),
                "connection_timeout": 5,
            }
            resultado = probar_conexion(configuracion)
            self.estado.set(
                f'Conexión correcta · {resultado["base_datos"]} · MySQL {resultado["version"]} · {resultado["usuario"]}'
            )
        except Exception as error:
            self.estado.set(f"No se pudo conectar: {error}")


def comprobar():
    configuracion = configuracion_desde_entorno()
    assert configuracion["host"]
    assert isinstance(configuracion["port"], int)
    assert configuracion["database"] == os.getenv("MYSQL_DATABASE", "ai_career")
    print("UNE9D26 OK")


if __name__ == "__main__":
    if "--check" in sys.argv:
        comprobar()
    else:
        ConexionTkinterMySQL().mainloop()
