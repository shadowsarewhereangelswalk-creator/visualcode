import re
import sys
import tkinter as tk
from dataclasses import dataclass, replace
from tkinter import ttk


@dataclass(frozen=True)
class Cliente:
    id: int
    nombre: str
    correo: str
    servicio: str


def validar_datos(nombre, correo, servicio):
    nombre = " ".join(nombre.split()).title()
    correo = correo.strip().lower()
    servicio = servicio.strip().title()
    if len(nombre) < 3:
        raise ValueError("Nombre inválido")
    if re.fullmatch(r"[^@\s]+@[^@\s]+\.[A-Za-z]{2,}", correo) is None:
        raise ValueError("Correo inválido")
    if len(servicio) < 3:
        raise ValueError("Servicio inválido")
    return nombre, correo, servicio


class RepositorioMemoria:
    def __init__(self):
        self.registros = {}
        self.siguiente_id = 1

    def crear(self, nombre, correo, servicio):
        datos = validar_datos(nombre, correo, servicio)
        if any(cliente.correo == datos[1] for cliente in self.registros.values()):
            raise ValueError("El correo ya existe")
        cliente = Cliente(self.siguiente_id, *datos)
        self.registros[cliente.id] = cliente
        self.siguiente_id += 1
        return cliente

    def listar(self, filtro=""):
        termino = filtro.strip().casefold()
        clientes = self.registros.values()
        if termino:
            clientes = [
                cliente for cliente in clientes
                if termino in cliente.nombre.casefold()
                or termino in cliente.correo.casefold()
                or termino in cliente.servicio.casefold()
            ]
        return sorted(clientes, key=lambda cliente: cliente.nombre)

    def actualizar(self, identificador, nombre, correo, servicio):
        if identificador not in self.registros:
            raise LookupError("Cliente no encontrado")
        datos = validar_datos(nombre, correo, servicio)
        if any(
            cliente.correo == datos[1] and cliente.id != identificador
            for cliente in self.registros.values()
        ):
            raise ValueError("El correo ya existe")
        cliente = replace(self.registros[identificador], nombre=datos[0], correo=datos[1], servicio=datos[2])
        self.registros[identificador] = cliente
        return cliente

    def eliminar(self, identificador):
        if identificador not in self.registros:
            raise LookupError("Cliente no encontrado")
        return self.registros.pop(identificador)


class EvaluacionCrud(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Evaluación integral del Nivel 9")
        self.geometry("900x590")
        self.minsize(720, 500)
        self.repositorio = RepositorioMemoria()
        self.identificador = None
        self.nombre = tk.StringVar()
        self.correo = tk.StringVar()
        self.servicio = tk.StringVar()
        self.buscar = tk.StringVar()
        self.estado = tk.StringVar(value="CRUD listo")
        self.crear_interfaz()
        self.cargar_ejemplos()

    def crear_interfaz(self):
        principal = ttk.Frame(self, padding=18)
        principal.pack(fill="both", expand=True)
        ttk.Label(principal, text="Evaluación CRUD", font=("TkDefaultFont", 20, "bold")).grid(column=0, row=0, sticky="w")
        busqueda = ttk.Entry(principal, textvariable=self.buscar, width=28)
        busqueda.grid(column=1, row=0, sticky="e")

        formulario = ttk.LabelFrame(principal, text="Cliente", padding=14)
        formulario.grid(column=0, row=1, sticky="nsw", pady=16, padx=(0, 16))
        for fila, (texto, variable) in enumerate(
            (("Nombre", self.nombre), ("Correo", self.correo), ("Servicio", self.servicio))
        ):
            ttk.Label(formulario, text=texto).grid(column=0, row=fila * 2, sticky="w")
            ttk.Entry(formulario, textvariable=variable, width=30).grid(column=0, row=fila * 2 + 1, pady=(3, 12))
        acciones = ttk.Frame(formulario)
        acciones.grid(column=0, row=6, sticky="ew", pady=(8, 0))
        ttk.Button(acciones, text="Nuevo", command=self.nuevo).pack(side="left")
        ttk.Button(acciones, text="Guardar", command=self.guardar).pack(side="left", padx=6)
        ttk.Button(acciones, text="Eliminar", command=self.eliminar).pack(side="left")

        self.tabla = ttk.Treeview(principal, columns=("id", "nombre", "correo", "servicio"), show="headings")
        for columna, ancho in (("id", 60), ("nombre", 170), ("correo", 210), ("servicio", 160)):
            self.tabla.heading(columna, text=columna.title())
            self.tabla.column(columna, width=ancho)
        self.tabla.grid(column=1, row=1, sticky="nsew", pady=16)
        self.tabla.bind("<<TreeviewSelect>>", self.seleccionar)

        ttk.Label(principal, textvariable=self.estado).grid(column=0, row=2, columnspan=2, sticky="w")
        principal.columnconfigure(1, weight=1)
        principal.rowconfigure(1, weight=1)
        self.buscar.trace_add("write", lambda *args: self.actualizar_tabla())

    def cargar_ejemplos(self):
        self.repositorio.crear("Ana Torres", "ana@ejemplo.com", "Automatización")
        self.repositorio.crear("Luis Pérez", "luis@ejemplo.com", "Landing page")
        self.actualizar_tabla()

    def actualizar_tabla(self):
        clientes = self.repositorio.listar(self.buscar.get())
        self.tabla.delete(*self.tabla.get_children())
        for cliente in clientes:
            self.tabla.insert("", "end", values=(cliente.id, cliente.nombre, cliente.correo, cliente.servicio))
        self.estado.set(f"Clientes: {len(clientes)}")

    def seleccionar(self, evento=None):
        seleccion = self.tabla.selection()
        if not seleccion:
            return
        valores = self.tabla.item(seleccion[0], "values")
        self.identificador = int(valores[0])
        self.nombre.set(valores[1])
        self.correo.set(valores[2])
        self.servicio.set(valores[3])

    def nuevo(self):
        self.identificador = None
        self.nombre.set("")
        self.correo.set("")
        self.servicio.set("")

    def guardar(self):
        try:
            if self.identificador is None:
                self.repositorio.crear(self.nombre.get(), self.correo.get(), self.servicio.get())
            else:
                self.repositorio.actualizar(self.identificador, self.nombre.get(), self.correo.get(), self.servicio.get())
            self.nuevo()
            self.actualizar_tabla()
        except (ValueError, LookupError) as error:
            self.estado.set(str(error))

    def eliminar(self):
        if self.identificador is None:
            self.estado.set("Selecciona un cliente")
            return
        try:
            self.repositorio.eliminar(self.identificador)
            self.nuevo()
            self.actualizar_tabla()
        except LookupError as error:
            self.estado.set(str(error))


def ejecutar_pruebas():
    repositorio = RepositorioMemoria()
    ana = repositorio.crear(" ana torres ", "ANA@EJEMPLO.COM", "automatización")
    assert ana.nombre == "Ana Torres"
    assert ana.correo == "ana@ejemplo.com"
    assert len(repositorio.listar()) == 1
    actualizado = repositorio.actualizar(ana.id, "Ana Torres", "ana@ejemplo.com", "Desarrollo")
    assert actualizado.servicio == "Desarrollo"
    assert repositorio.listar("desa") == [actualizado]
    eliminado = repositorio.eliminar(ana.id)
    assert eliminado == actualizado
    assert repositorio.listar() == []
    print("UNE9D31 OK")


if __name__ == "__main__":
    if "--check" in sys.argv:
        ejecutar_pruebas()
    else:
        EvaluacionCrud().mainloop()
