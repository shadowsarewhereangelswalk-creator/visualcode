import sys
import tkinter as tk
from tkinter import ttk


SERVICIOS = {
    "Diseño": 180,
    "Desarrollo": 420,
    "Automatización": 310,
    "Soporte": 90,
}


def calcular_total(seleccionados, urgente=False):
    subtotal = sum(SERVICIOS[nombre] for nombre in seleccionados)
    recargo = subtotal * 0.2 if urgente else 0
    return subtotal, recargo, subtotal + recargo


class SelectorServicios(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Checkboxes y variables de control")
        self.geometry("560x430")
        self.resizable(False, False)
        self.opciones = {nombre: tk.BooleanVar() for nombre in SERVICIOS}
        self.urgente = tk.BooleanVar()
        self.resultado = tk.StringVar(value="Total: 0.00")
        self.crear_interfaz()

    def crear_interfaz(self):
        panel = ttk.Frame(self, padding=28)
        panel.pack(fill="both", expand=True)
        ttk.Label(panel, text="Configura tu proyecto", font=("TkDefaultFont", 18, "bold")).pack(anchor="w")
        ttk.Label(panel, text="Selecciona uno o varios servicios").pack(anchor="w", pady=(6, 16))

        for nombre, precio in SERVICIOS.items():
            ttk.Checkbutton(
                panel,
                text=f"{nombre} · {precio:.2f}",
                variable=self.opciones[nombre],
                command=self.actualizar,
            ).pack(anchor="w", pady=4)

        ttk.Separator(panel).pack(fill="x", pady=14)
        ttk.Checkbutton(
            panel,
            text="Entrega urgente",
            variable=self.urgente,
            command=self.actualizar,
        ).pack(anchor="w")
        ttk.Label(panel, textvariable=self.resultado, font=("TkDefaultFont", 13, "bold")).pack(anchor="w", pady=(18, 0))

    def actualizar(self):
        seleccionados = [nombre for nombre, variable in self.opciones.items() if variable.get()]
        subtotal, recargo, total = calcular_total(seleccionados, self.urgente.get())
        self.resultado.set(f"Subtotal: {subtotal:.2f} · Recargo: {recargo:.2f} · Total: {total:.2f}")


def comprobar():
    assert calcular_total(["Diseño", "Soporte"]) == (270, 0, 270)
    assert calcular_total(["Desarrollo"], True) == (420, 84, 504)
    print("UNE9D09 OK")


if __name__ == "__main__":
    if "--check" in sys.argv:
        comprobar()
    else:
        SelectorServicios().mainloop()
