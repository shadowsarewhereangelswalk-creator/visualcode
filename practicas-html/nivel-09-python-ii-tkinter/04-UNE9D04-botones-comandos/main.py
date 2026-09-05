import sys
import tkinter as tk
from tkinter import ttk


def aplicar_operacion(valor, operacion):
    if operacion == "sumar":
        return valor + 1
    if operacion == "restar":
        return valor - 1
    if operacion == "doblar":
        return valor * 2
    if operacion == "reiniciar":
        return 0
    raise ValueError("Operación desconocida")


class Contador(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Botones y comandos")
        self.geometry("500x320")
        self.resizable(False, False)
        self.valor = tk.IntVar(value=0)
        self.mensaje = tk.StringVar(value="Selecciona una operación")
        self.crear_interfaz()

    def crear_interfaz(self):
        panel = ttk.Frame(self, padding=28)
        panel.pack(fill="both", expand=True)
        ttk.Label(panel, text="Contador interactivo", font=("TkDefaultFont", 18, "bold")).pack()
        ttk.Label(panel, textvariable=self.valor, font=("TkFixedFont", 42)).pack(pady=24)

        botones = ttk.Frame(panel)
        botones.pack()
        for texto, operacion in (
            ("−1", "restar"),
            ("+1", "sumar"),
            ("×2", "doblar"),
            ("Reiniciar", "reiniciar"),
        ):
            ttk.Button(
                botones,
                text=texto,
                command=lambda accion=operacion: self.ejecutar(accion),
            ).pack(side="left", padx=4)

        ttk.Label(panel, textvariable=self.mensaje).pack(pady=(22, 0))

    def ejecutar(self, operacion):
        nuevo_valor = aplicar_operacion(self.valor.get(), operacion)
        self.valor.set(nuevo_valor)
        self.mensaje.set(f"Operación aplicada: {operacion}")


def comprobar():
    assert aplicar_operacion(4, "sumar") == 5
    assert aplicar_operacion(4, "restar") == 3
    assert aplicar_operacion(4, "doblar") == 8
    assert aplicar_operacion(4, "reiniciar") == 0
    print("UNE9D04 OK")


if __name__ == "__main__":
    if "--check" in sys.argv:
        comprobar()
    else:
        Contador().mainloop()
