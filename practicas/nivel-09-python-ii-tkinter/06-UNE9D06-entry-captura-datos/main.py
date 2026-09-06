import re
import sys
import tkinter as tk
from tkinter import ttk


def validar_contacto(nombre, correo, telefono):
    nombre = " ".join(nombre.split()).title()
    correo = correo.strip().lower()
    telefono = re.sub(r"\D", "", telefono)
    if len(nombre) < 3:
        raise ValueError("Escribe un nombre válido")
    if re.fullmatch(r"[^@\s]+@[^@\s]+\.[A-Za-z]{2,}", correo) is None:
        raise ValueError("Escribe un correo válido")
    if not 10 <= len(telefono) <= 15:
        raise ValueError("Escribe un teléfono válido")
    return nombre, correo, telefono


class Formulario(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Captura de datos con Entry")
        self.geometry("560x390")
        self.resizable(False, False)
        self.nombre = tk.StringVar()
        self.correo = tk.StringVar()
        self.telefono = tk.StringVar()
        self.estado = tk.StringVar(value="Completa todos los campos")
        self.crear_interfaz()

    def crear_interfaz(self):
        panel = ttk.Frame(self, padding=30)
        panel.pack(fill="both", expand=True)
        ttk.Label(panel, text="Registro de contacto", font=("TkDefaultFont", 18, "bold")).grid(column=0, row=0, columnspan=2, sticky="w", pady=(0, 22))

        campos = (
            ("Nombre", self.nombre),
            ("Correo", self.correo),
            ("Teléfono", self.telefono),
        )
        primer_campo = None
        for fila, (texto, variable) in enumerate(campos, start=1):
            ttk.Label(panel, text=texto).grid(column=0, row=fila, sticky="w", pady=7)
            entrada = ttk.Entry(panel, textvariable=variable, width=38)
            entrada.grid(column=1, row=fila, sticky="ew", pady=7)
            if primer_campo is None:
                primer_campo = entrada

        ttk.Button(panel, text="Guardar", command=self.guardar).grid(column=1, row=4, sticky="e", pady=(18, 0))
        ttk.Label(panel, textvariable=self.estado, wraplength=440).grid(column=0, row=5, columnspan=2, sticky="w", pady=(24, 0))
        panel.columnconfigure(1, weight=1)
        primer_campo.focus_set()
        self.bind("<Return>", lambda evento: self.guardar())

    def guardar(self):
        try:
            nombre, correo, telefono = validar_contacto(
                self.nombre.get(),
                self.correo.get(),
                self.telefono.get(),
            )
            self.estado.set(f"Guardado: {nombre} · {correo} · {telefono}")
        except ValueError as error:
            self.estado.set(str(error))


def comprobar():
    assert validar_contacto(" ana torres ", "ANA@EJEMPLO.COM", "+58 412-555-0198") == (
        "Ana Torres",
        "ana@ejemplo.com",
        "584125550198",
    )
    print("UNE9D06 OK")


if __name__ == "__main__":
    if "--check" in sys.argv:
        comprobar()
    else:
        Formulario().mainloop()
