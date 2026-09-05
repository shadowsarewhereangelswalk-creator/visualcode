import os
import re
import sys
import tkinter as tk
from tkinter import messagebox, ttk


CAMPOS = ("nombre", "correo", "telefono", "servicio")


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
    if len(nombre) < 3 or not servicio:
        raise ValueError("Nombre y servicio son obligatorios")
    if re.fullmatch(r"[^@\s]+@[^@\s]+\.[A-Za-z]{2,}", correo) is None:
        raise ValueError("El correo no es válido")
    if len(re.sub(r"\D", "", telefono)) < 10:
        raise ValueError("El teléfono no es válido")
    return nombre, correo, telefono, servicio


class RepositorioClientes:
    def conectar(self):
        import mysql.connector

        return mysql.connector.connect(**configuracion_mysql())

    def listar(self):
        conexion = self.conectar()
        cursor = conexion.cursor(dictionary=True)
        try:
            cursor.execute("SELECT id, nombre, correo, telefono, servicio FROM clientes ORDER BY nombre")
            return cursor.fetchall()
        finally:
            cursor.close()
            conexion.close()

    def actualizar(self, identificador, cliente):
        conexion = self.conectar()
        cursor = conexion.cursor()
        try:
            cursor.execute(
                "UPDATE clientes SET nombre = %s, correo = %s, telefono = %s, servicio = %s WHERE id = %s",
                (*cliente, identificador),
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


class EditorClientes(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("CRUD — UPDATE y DELETE")
        self.geometry("960x640")
        self.minsize(780, 540)
        self.repositorio = RepositorioClientes()
        self.identificador = None
        self.variables = {campo: tk.StringVar() for campo in CAMPOS}
        self.estado = tk.StringVar(value="Selecciona un cliente")
        self.crear_interfaz()
        self.after(150, self.cargar)

    def crear_interfaz(self):
        principal = ttk.Frame(self, padding=18)
        principal.pack(fill="both", expand=True)
        formulario = ttk.LabelFrame(principal, text="Editar cliente", padding=16)
        formulario.pack(fill="x")
        for columna, campo in enumerate(CAMPOS):
            ttk.Label(formulario, text=campo.title()).grid(column=columna, row=0, sticky="w")
            ttk.Entry(formulario, textvariable=self.variables[campo]).grid(column=columna, row=1, sticky="ew", padx=(0, 8))
            formulario.columnconfigure(columna, weight=1)

        acciones = ttk.Frame(principal)
        acciones.pack(fill="x", pady=12)
        ttk.Button(acciones, text="Actualizar", command=self.actualizar).pack(side="left")
        ttk.Button(acciones, text="Eliminar", command=self.eliminar).pack(side="left", padx=8)
        ttk.Button(acciones, text="Recargar", command=self.cargar).pack(side="left")
        ttk.Label(acciones, textvariable=self.estado).pack(side="right")

        columnas = ("id", *CAMPOS)
        self.tabla = ttk.Treeview(principal, columns=columnas, show="headings")
        for columna in columnas:
            self.tabla.heading(columna, text=columna.title())
            self.tabla.column(columna, width=80 if columna == "id" else 180)
        self.tabla.pack(fill="both", expand=True)
        self.tabla.bind("<<TreeviewSelect>>", self.seleccionar)

    def cargar(self):
        try:
            filas = self.repositorio.listar()
            self.tabla.delete(*self.tabla.get_children())
            for fila in filas:
                self.tabla.insert("", "end", values=tuple(fila[columna] for columna in ("id", *CAMPOS)))
            self.estado.set(f"Clientes: {len(filas)}")
        except Exception as error:
            self.estado.set(f"No se pudo consultar: {error}")

    def seleccionar(self, evento=None):
        seleccion = self.tabla.selection()
        if not seleccion:
            return
        valores = self.tabla.item(seleccion[0], "values")
        self.identificador = int(valores[0])
        for campo, valor in zip(CAMPOS, valores[1:]):
            self.variables[campo].set(valor)
        self.estado.set(f"Editando cliente {self.identificador}")

    def actualizar(self):
        if self.identificador is None:
            self.estado.set("Selecciona un cliente")
            return
        try:
            cliente = validar_cliente(*(self.variables[campo].get() for campo in CAMPOS))
            filas = self.repositorio.actualizar(self.identificador, cliente)
            self.estado.set(f"Registros actualizados: {filas}")
            self.cargar()
        except Exception as error:
            self.estado.set(f"No se pudo actualizar: {error}")

    def eliminar(self):
        if self.identificador is None:
            self.estado.set("Selecciona un cliente")
            return
        if not messagebox.askyesno("Eliminar", "¿Eliminar el cliente seleccionado?", parent=self):
            return
        try:
            filas = self.repositorio.eliminar(self.identificador)
            self.identificador = None
            for variable in self.variables.values():
                variable.set("")
            self.estado.set(f"Registros eliminados: {filas}")
            self.cargar()
        except Exception as error:
            self.estado.set(f"No se pudo eliminar: {error}")


def comprobar():
    assert validar_cliente("Luis Pérez", "luis@ejemplo.com", "3055550124", "landing page")[3] == "Landing Page"
    print("UNE9D28 OK")


if __name__ == "__main__":
    if "--check" in sys.argv:
        comprobar()
    else:
        EditorClientes().mainloop()
