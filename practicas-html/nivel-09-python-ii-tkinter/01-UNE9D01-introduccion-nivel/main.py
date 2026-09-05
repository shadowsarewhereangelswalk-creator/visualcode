import sys
import tkinter as tk
from tkinter import ttk


PRACTICAS = (
    ("P1", 8, "Formulario con controles básicos"),
    ("P2", 15, "Aplicación con menús, diálogos y layouts"),
    ("P3", 20, "Gestión de eventos"),
    ("P4", 26, "Conexión de Tkinter a MySQL"),
    ("P5", 30, "Aplicación CRUD de escritorio"),
)


class Aplicacion(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Nivel 9 — Python II: Tkinter")
        self.geometry("760x460")
        self.minsize(640, 380)
        self.crear_interfaz()

    def crear_interfaz(self):
        contenedor = ttk.Frame(self, padding=24)
        contenedor.pack(fill="both", expand=True)

        ttk.Label(
            contenedor,
            text="Nivel 9 — Python II: Tkinter",
            font=("TkDefaultFont", 20, "bold"),
        ).pack(anchor="w")
        ttk.Label(
            contenedor,
            text="Proyecto del mes: CRUD de escritorio con Python, Tkinter y MySQL",
        ).pack(anchor="w", pady=(6, 20))

        tabla = ttk.Treeview(
            contenedor,
            columns=("dia", "entrega"),
            show="headings",
            height=8,
        )
        tabla.heading("dia", text="Día")
        tabla.heading("entrega", text="Entrega")
        tabla.column("dia", width=90, anchor="center")
        tabla.column("entrega", width=520)
        for codigo, dia, entrega in PRACTICAS:
            tabla.insert("", "end", values=(f"{codigo} · {dia}", entrega))
        tabla.pack(fill="both", expand=True)

        ttk.Button(contenedor, text="Cerrar", command=self.destroy).pack(anchor="e", pady=(18, 0))


def comprobar():
    assert len(PRACTICAS) == 5
    assert PRACTICAS[-1][1] == 30
    print("UNE9D01 OK")


if __name__ == "__main__":
    if "--check" in sys.argv:
        comprobar()
    else:
        Aplicacion().mainloop()
