import sys
import tkinter as tk
from tkinter import messagebox, ttk

from database import RepositorioClientes
from modelos import Cliente


CAMPOS = ("nombre", "correo", "telefono", "servicio")


class CrudClientes(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("P5 — CRUD de escritorio")
        self.geometry("1120x680")
        self.minsize(900, 580)
        self.repositorio = RepositorioClientes()
        self.identificador = None
        self.variables = {campo: tk.StringVar() for campo in CAMPOS}
        self.activo = tk.BooleanVar(value=True)
        self.buscar = tk.StringVar()
        self.estado = tk.StringVar(value="Aplicación lista")
        self.crear_interfaz()
        self.after(150, self.cargar)

    def crear_interfaz(self):
        principal = ttk.Frame(self, padding=18)
        principal.pack(fill="both", expand=True)
        principal.columnconfigure(1, weight=1)
        principal.rowconfigure(1, weight=1)

        ttk.Label(principal, text="Gestión de clientes", font=("TkDefaultFont", 21, "bold")).grid(column=0, row=0, sticky="w")
        busqueda = ttk.Frame(principal)
        busqueda.grid(column=1, row=0, sticky="e")
        ttk.Label(busqueda, text="Buscar").pack(side="left")
        ttk.Entry(busqueda, textvariable=self.buscar, width=30).pack(side="left", padx=8)
        ttk.Button(busqueda, text="Aplicar", command=self.cargar).pack(side="left")

        formulario = ttk.LabelFrame(principal, text="Ficha del cliente", padding=16)
        formulario.grid(column=0, row=1, sticky="nsw", pady=(16, 0), padx=(0, 16))
        for fila, campo in enumerate(CAMPOS):
            ttk.Label(formulario, text=campo.title()).grid(column=0, row=fila * 2, sticky="w", pady=(0, 3))
            ttk.Entry(formulario, textvariable=self.variables[campo], width=32).grid(column=0, row=fila * 2 + 1, sticky="ew", pady=(0, 12))
        ttk.Checkbutton(formulario, text="Cliente activo", variable=self.activo).grid(column=0, row=8, sticky="w")

        acciones = ttk.Frame(formulario)
        acciones.grid(column=0, row=9, sticky="ew", pady=(18, 0))
        ttk.Button(acciones, text="Nuevo", command=self.nuevo).pack(side="left")
        ttk.Button(acciones, text="Guardar", command=self.guardar).pack(side="left", padx=6)
        ttk.Button(acciones, text="Eliminar", command=self.eliminar).pack(side="left")

        tabla_panel = ttk.Frame(principal)
        tabla_panel.grid(column=1, row=1, sticky="nsew", pady=(16, 0))
        tabla_panel.columnconfigure(0, weight=1)
        tabla_panel.rowconfigure(0, weight=1)
        columnas = ("id", "nombre", "correo", "telefono", "servicio", "activo")
        self.tabla = ttk.Treeview(tabla_panel, columns=columnas, show="headings")
        for columna, ancho in (
            ("id", 60),
            ("nombre", 170),
            ("correo", 210),
            ("telefono", 140),
            ("servicio", 160),
            ("activo", 70),
        ):
            self.tabla.heading(columna, text=columna.title())
            self.tabla.column(columna, width=ancho)
        barra = ttk.Scrollbar(tabla_panel, orient="vertical", command=self.tabla.yview)
        self.tabla.configure(yscrollcommand=barra.set)
        self.tabla.grid(column=0, row=0, sticky="nsew")
        barra.grid(column=1, row=0, sticky="ns")
        self.tabla.bind("<<TreeviewSelect>>", self.seleccionar)

        ttk.Label(principal, textvariable=self.estado).grid(column=0, row=2, columnspan=2, sticky="w", pady=(12, 0))
        self.bind("<Control-n>", lambda evento: self.nuevo())
        self.bind("<Control-s>", lambda evento: self.guardar())
        self.buscar.trace_add("write", lambda *args: self.after(250, self.cargar))

    def crear_cliente_actual(self):
        return Cliente.crear(
            self.variables["nombre"].get(),
            self.variables["correo"].get(),
            self.variables["telefono"].get(),
            self.variables["servicio"].get(),
            self.identificador,
            self.activo.get(),
        )

    def cargar(self):
        try:
            clientes = self.repositorio.listar(self.buscar.get())
            self.tabla.delete(*self.tabla.get_children())
            for cliente in clientes:
                self.tabla.insert(
                    "",
                    "end",
                    values=(
                        cliente.id,
                        cliente.nombre,
                        cliente.correo,
                        cliente.telefono,
                        cliente.servicio,
                        "Sí" if cliente.activo else "No",
                    ),
                )
            self.estado.set(f"Clientes encontrados: {len(clientes)}")
        except Exception as error:
            self.estado.set(f"No se pudo consultar: {error}")

    def seleccionar(self, evento=None):
        seleccion = self.tabla.selection()
        if not seleccion:
            return
        valores = self.tabla.item(seleccion[0], "values")
        self.identificador = int(valores[0])
        for campo, valor in zip(CAMPOS, valores[1:5]):
            self.variables[campo].set(valor)
        self.activo.set(valores[5] == "Sí")
        self.estado.set(f"Editando cliente {self.identificador}")

    def nuevo(self):
        self.identificador = None
        for variable in self.variables.values():
            variable.set("")
        self.activo.set(True)
        self.tabla.selection_remove(self.tabla.selection())
        self.estado.set("Nuevo cliente")

    def guardar(self):
        try:
            cliente = self.crear_cliente_actual()
            if cliente.id is None:
                identificador = self.repositorio.insertar(cliente)
                self.estado.set(f"Cliente {identificador} creado")
            else:
                filas = self.repositorio.actualizar(cliente)
                self.estado.set(f"Registros actualizados: {filas}")
            self.nuevo()
            self.cargar()
        except Exception as error:
            self.estado.set(f"No se pudo guardar: {error}")

    def eliminar(self):
        if self.identificador is None:
            self.estado.set("Selecciona un cliente")
            return
        if not messagebox.askyesno("Eliminar", "¿Eliminar este cliente?", parent=self):
            return
        try:
            filas = self.repositorio.eliminar(self.identificador)
            self.nuevo()
            self.cargar()
            self.estado.set(f"Registros eliminados: {filas}")
        except Exception as error:
            self.estado.set(f"No se pudo eliminar: {error}")


def comprobar():
    cliente = Cliente.crear(
        " ana torres ",
        "ANA@EJEMPLO.COM",
        "+58 412-555-0198",
        "automatización",
    )
    assert cliente.nombre == "Ana Torres"
    assert cliente.correo == "ana@ejemplo.com"
    assert cliente.id is None
    print("UNE9D30 OK")


if __name__ == "__main__":
    if "--check" in sys.argv:
        comprobar()
    else:
        CrudClientes().mainloop()
