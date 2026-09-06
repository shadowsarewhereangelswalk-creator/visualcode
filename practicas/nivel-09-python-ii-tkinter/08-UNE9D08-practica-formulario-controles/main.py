import re
import sys
import tkinter as tk
from tkinter import ttk


SERVICIOS = ("Landing page", "Automatización", "Asistente virtual")
PRECIOS = {"Landing page": 450, "Automatización": 780, "Asistente virtual": 950}


def crear_registro(nombre, correo, servicio, prioridad, boletin):
    nombre = " ".join(nombre.split()).title()
    correo = correo.strip().lower()
    if len(nombre) < 3:
        raise ValueError("El nombre es obligatorio")
    if re.fullmatch(r"[^@\s]+@[^@\s]+\.[A-Za-z]{2,}", correo) is None:
        raise ValueError("El correo no es válido")
    if servicio not in SERVICIOS:
        raise ValueError("Selecciona un servicio")
    return nombre, correo, servicio, prioridad, "Sí" if boletin else "No", PRECIOS[servicio]


class FormularioClientes(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("P1 — Formulario de escritorio")
        self.geometry("820x560")
        self.minsize(720, 500)
        self.nombre = tk.StringVar()
        self.correo = tk.StringVar()
        self.servicio = tk.StringVar(value=SERVICIOS[0])
        self.prioridad = tk.StringVar(value="Normal")
        self.boletin = tk.BooleanVar(value=True)
        self.estado = tk.StringVar(value="Completa el formulario")
        self.crear_interfaz()

    def crear_interfaz(self):
        principal = ttk.Frame(self, padding=24)
        principal.pack(fill="both", expand=True)
        ttk.Label(principal, text="Registro de clientes", font=("TkDefaultFont", 20, "bold")).grid(column=0, row=0, columnspan=4, sticky="w", pady=(0, 18))

        ttk.Label(principal, text="Nombre").grid(column=0, row=1, sticky="w")
        ttk.Entry(principal, textvariable=self.nombre).grid(column=1, row=1, sticky="ew", padx=(8, 20))
        ttk.Label(principal, text="Correo").grid(column=2, row=1, sticky="w")
        ttk.Entry(principal, textvariable=self.correo).grid(column=3, row=1, sticky="ew", padx=(8, 0))

        ttk.Label(principal, text="Servicio").grid(column=0, row=2, sticky="w", pady=12)
        ttk.Combobox(principal, textvariable=self.servicio, values=SERVICIOS, state="readonly").grid(column=1, row=2, sticky="ew", padx=(8, 20), pady=12)
        ttk.Label(principal, text="Prioridad").grid(column=2, row=2, sticky="w", pady=12)
        prioridades = ttk.Frame(principal)
        prioridades.grid(column=3, row=2, sticky="w", padx=(8, 0), pady=12)
        for texto in ("Normal", "Alta"):
            ttk.Radiobutton(prioridades, text=texto, value=texto, variable=self.prioridad).pack(side="left", padx=(0, 8))

        ttk.Checkbutton(principal, text="Recibir novedades", variable=self.boletin).grid(column=0, row=3, columnspan=2, sticky="w")
        acciones = ttk.Frame(principal)
        acciones.grid(column=2, row=3, columnspan=2, sticky="e")
        ttk.Button(acciones, text="Limpiar", command=self.limpiar).pack(side="left")
        ttk.Button(acciones, text="Registrar", command=self.registrar).pack(side="left", padx=(8, 0))

        self.tabla = ttk.Treeview(
            principal,
            columns=("nombre", "correo", "servicio", "prioridad", "boletin", "precio"),
            show="headings",
            height=12,
        )
        for columna, titulo, ancho in (
            ("nombre", "Nombre", 130),
            ("correo", "Correo", 170),
            ("servicio", "Servicio", 140),
            ("prioridad", "Prioridad", 80),
            ("boletin", "Boletín", 70),
            ("precio", "Precio", 80),
        ):
            self.tabla.heading(columna, text=titulo)
            self.tabla.column(columna, width=ancho)
        self.tabla.grid(column=0, row=4, columnspan=4, sticky="nsew", pady=(20, 10))
        ttk.Label(principal, textvariable=self.estado).grid(column=0, row=5, columnspan=4, sticky="w")

        for columna in (1, 3):
            principal.columnconfigure(columna, weight=1)
        principal.rowconfigure(4, weight=1)
        self.bind("<Return>", lambda evento: self.registrar())

    def registrar(self):
        try:
            registro = crear_registro(
                self.nombre.get(),
                self.correo.get(),
                self.servicio.get(),
                self.prioridad.get(),
                self.boletin.get(),
            )
            self.tabla.insert("", "end", values=registro)
            self.estado.set(f"Cliente registrado: {registro[0]}")
            self.limpiar(conservar_estado=True)
        except ValueError as error:
            self.estado.set(str(error))

    def limpiar(self, conservar_estado=False):
        self.nombre.set("")
        self.correo.set("")
        self.servicio.set(SERVICIOS[0])
        self.prioridad.set("Normal")
        self.boletin.set(True)
        if not conservar_estado:
            self.estado.set("Formulario limpio")


def comprobar():
    registro = crear_registro("Ana Torres", "ANA@EJEMPLO.COM", "Automatización", "Alta", True)
    assert registro[-1] == 780
    assert registro[1] == "ana@ejemplo.com"
    print("UNE9D08 OK")


if __name__ == "__main__":
    if "--check" in sys.argv:
        comprobar()
    else:
        FormularioClientes().mainloop()
