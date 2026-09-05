import os
import sys
import tkinter as tk
from tkinter import ttk


def crear_configuracion(host, puerto, usuario, clave, base_datos):
    if not host.strip() or not usuario.strip() or not base_datos.strip():
        raise ValueError("Servidor, usuario y base de datos son obligatorios")
    puerto = int(puerto)
    if not 1 <= puerto <= 65535:
        raise ValueError("El puerto no es válido")
    return {
        "host": host.strip(),
        "port": puerto,
        "user": usuario.strip(),
        "password": clave,
        "database": base_datos.strip(),
        "connection_timeout": 5,
    }


class ConexionMySQL:
    def __init__(self, configuracion):
        self.configuracion = configuracion
        self.conexion = None

    def __enter__(self):
        import mysql.connector

        self.conexion = mysql.connector.connect(**self.configuracion)
        return self.conexion

    def __exit__(self, tipo, valor, traceback):
        if self.conexion is not None and self.conexion.is_connected():
            self.conexion.close()


def diagnosticar(configuracion):
    with ConexionMySQL(configuracion) as conexion:
        cursor = conexion.cursor()
        try:
            cursor.execute(
                "SELECT DATABASE(), VERSION(), CURRENT_USER(), @@character_set_database"
            )
            base_datos, version, usuario, juego_caracteres = cursor.fetchone()
            cursor.execute(
                "SELECT COUNT(*) FROM information_schema.tables WHERE table_schema = %s",
                (base_datos,),
            )
            tablas = cursor.fetchone()[0]
            return (
                ("Base de datos", base_datos),
                ("Versión", version),
                ("Usuario", usuario),
                ("Juego de caracteres", juego_caracteres),
                ("Tablas", tablas),
            )
        finally:
            cursor.close()


class DiagnosticoConexion(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Diagnóstico de conexión MySQL")
        self.geometry("720x560")
        self.resizable(False, False)
        self.variables = {
            "host": tk.StringVar(value=os.getenv("MYSQL_HOST", "127.0.0.1")),
            "puerto": tk.StringVar(value=os.getenv("MYSQL_PORT", "3306")),
            "usuario": tk.StringVar(value=os.getenv("MYSQL_USER", "root")),
            "clave": tk.StringVar(value=os.getenv("MYSQL_PASSWORD", "")),
            "base_datos": tk.StringVar(value=os.getenv("MYSQL_DATABASE", "ai_career")),
        }
        self.estado = tk.StringVar(value="Ejecuta el diagnóstico")
        self.crear_interfaz()

    def crear_interfaz(self):
        panel = ttk.Frame(self, padding=24)
        panel.pack(fill="both", expand=True)
        ttk.Label(panel, text="Diagnóstico MySQL", font=("TkDefaultFont", 19, "bold")).grid(column=0, row=0, columnspan=2, sticky="w", pady=(0, 18))
        for fila, (campo, variable) in enumerate(self.variables.items(), start=1):
            ttk.Label(panel, text=campo.replace("_", " ").title()).grid(column=0, row=fila, sticky="w", pady=6)
            ttk.Entry(panel, textvariable=variable, show="•" if campo == "clave" else "").grid(column=1, row=fila, sticky="ew", pady=6)

        ttk.Button(panel, text="Probar y diagnosticar", command=self.probar).grid(column=1, row=6, sticky="e", pady=(16, 12))
        self.tabla = ttk.Treeview(panel, columns=("propiedad", "valor"), show="headings", height=7)
        self.tabla.heading("propiedad", text="Propiedad")
        self.tabla.heading("valor", text="Valor")
        self.tabla.column("propiedad", width=180)
        self.tabla.column("valor", width=400)
        self.tabla.grid(column=0, row=7, columnspan=2, sticky="nsew")
        ttk.Label(panel, textvariable=self.estado, wraplength=620).grid(column=0, row=8, columnspan=2, sticky="w", pady=(12, 0))
        panel.columnconfigure(1, weight=1)

    def probar(self):
        try:
            configuracion = crear_configuracion(*(self.variables[campo].get() for campo in ("host", "puerto", "usuario", "clave", "base_datos")))
            datos = diagnosticar(configuracion)
            self.tabla.delete(*self.tabla.get_children())
            for fila in datos:
                self.tabla.insert("", "end", values=fila)
            self.estado.set("Conexión verificada y cerrada correctamente")
        except Exception as error:
            self.estado.set(f"Diagnóstico fallido: {error}")


def comprobar():
    configuracion = crear_configuracion("127.0.0.1", "3306", "root", "", "ai_career")
    assert configuracion["port"] == 3306
    assert configuracion["database"] == "ai_career"
    print("UNE9D29 OK")


if __name__ == "__main__":
    if "--check" in sys.argv:
        comprobar()
    else:
        DiagnosticoConexion().mainloop()
