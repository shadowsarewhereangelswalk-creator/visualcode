import os
import re
import sys
import tkinter as tk
from tkinter import ttk


def configuracion_mysql():
    return {
        "host": os.getenv("MYSQL_HOST", "127.0.0.1"),
        "port": int(os.getenv("MYSQL_PORT", "3306")),
        "user": os.getenv("MYSQL_USER", "root"),
        "password": os.getenv("MYSQL_PASSWORD", ""),
        "database": os.getenv("MYSQL_DATABASE", "ai_career"),
    }


def validar_cliente(nombre, correo, telefono, servicio):
    nombre = " ".join(nombre.split()).title()
    correo = correo.strip().lower()
    telefono = telefono.strip()
    servicio = servicio.strip().title()
    if len(nombre) < 3:
        raise ValueError("Escribe un nombre válido")
    if re.fullmatch(r"[^@\s]+@[^@\s]+\.[A-Za-z]{2,}", correo) is None:
        raise ValueError("Escribe un correo válido")
    if len(re.sub(r"\D", "", telefono)) < 10:
        raise ValueError("Escribe un teléfono válido")
    if not servicio:
        raise ValueError("Escribe el servicio")
    return nombre, correo, telefono, servicio


class RepositorioClientes:
    def conectar(self):
        import mysql.connector

        return mysql.connector.connect(**configuracion_mysql())

    def insertar(self, cliente):
        conexion = self.conectar()
        cursor = conexion.cursor()
        try:
            cursor.execute(
                "INSERT INTO clientes (nombre, correo, telefono, servicio) VALUES (%s, %s, %s, %s)",
                cliente,
            )
            conexion.commit()
            return cursor.lastrowid
        except Exception:
            conexion.rollback()
            raise
        finally:
            cursor.close()
            conexion.close()

    def listar(self):
        conexion = self.conectar()
        cursor = conexion.cursor(dictionary=True)
        try:
            cursor.execute(
                "SELECT id, nombre, correo, telefono, servicio, activo FROM clientes ORDER BY nombre"
            )
            return cursor.fetchall()
        finally:
            cursor.close()
            conexion.close()


class ClientesApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("CRUD — INSERT y SELECT")
        self.geometry("960x620")
        self.minsize(780, 520)
        self.repositorio = RepositorioClientes()
        self.variables = {
            "nombre": tk.StringVar(),
            "correo": tk.StringVar(),
            "telefono": tk.StringVar(),
            "servicio": tk.StringVar(),
        }
        self.estado = tk.StringVar(value="Conecta MySQL y carga los clientes")
        self.crear_interfaz()

    def crear_interfaz(self):
        principal = ttk.Frame(self, padding=18)
        principal.pack(fill="both", expand=True)
        formulario = ttk.LabelFrame(principal, text="Nuevo cliente", padding=16)
        formulario.pack(fill="x")

        for columna, campo in enumerate(("nombre", "correo", "telefono", "servicio")):
            ttk.Label(formulario, text=campo.title()).grid(column=columna, row=0, sticky="w")
            ttk.Entry(formulario, textvariable=self.variables[campo]).grid(column=columna, row=1, sticky="ew", padx=(0, 8))
            formulario.columnconfigure(columna, weight=1)
        ttk.Button(formulario, text="Guardar", command=self.guardar).grid(column=4, row=1)

        acciones = ttk.Frame(principal)
        acciones.pack(fill="x", pady=12)
        ttk.Button(acciones, text="Actualizar lista", command=self.cargar).pack(side="left")
        ttk.Label(acciones, textvariable=self.estado).pack(side="right")

        columnas = ("id", "nombre", "correo", "telefono", "servicio", "activo")
        self.tabla = ttk.Treeview(principal, columns=columnas, show="headings")
        for columna in columnas:
            self.tabla.heading(columna, text=columna.title())
            self.tabla.column(columna, width=80 if columna in {"id", "activo"} else 160)
        self.tabla.pack(fill="both", expand=True)
        self.after(150, self.cargar)

    def guardar(self):
        try:
            cliente = validar_cliente(*(self.variables[campo].get() for campo in ("nombre", "correo", "telefono", "servicio")))
            identificador = self.repositorio.insertar(cliente)
            for variable in self.variables.values():
                variable.set("")
            self.estado.set(f"Cliente {identificador} guardado")
            self.cargar()
        except Exception as error:
            self.estado.set(f"No se pudo guardar: {error}")

    def cargar(self):
        try:
            clientes = self.repositorio.listar()
            self.tabla.delete(*self.tabla.get_children())
            for cliente in clientes:
                self.tabla.insert("", "end", values=tuple(cliente[columna] for columna in ("id", "nombre", "correo", "telefono", "servicio", "activo")))
            self.estado.set(f"Clientes cargados: {len(clientes)}")
        except Exception as error:
            self.estado.set(f"No se pudo consultar: {error}")


def comprobar():
    cliente = validar_cliente(" ana torres ", "ANA@EJEMPLO.COM", "+58 412-555-0198", "automatización")
    assert cliente == ("Ana Torres", "ana@ejemplo.com", "+58 412-555-0198", "Automatización")
    print("UNE9D27 OK")


if __name__ == "__main__":
    if "--check" in sys.argv:
        comprobar()
    else:
        ClientesApp().mainloop()
