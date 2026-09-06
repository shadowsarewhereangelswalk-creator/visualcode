import sys
import tkinter as tk
from datetime import datetime
from tkinter import ttk


def formatear_hora(momento):
    return momento.strftime("%H:%M:%S")


class Reloj(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Ventana principal y ciclo de eventos")
        self.geometry("520x300")
        self.resizable(False, False)
        self.hora = tk.StringVar()
        self.estado = tk.StringVar(value="Ciclo de eventos activo")
        self.temporizador = None
        self.crear_interfaz()
        self.actualizar_reloj()
        self.protocol("WM_DELETE_WINDOW", self.cerrar)

    def crear_interfaz(self):
        panel = ttk.Frame(self, padding=30)
        panel.pack(fill="both", expand=True)
        ttk.Label(panel, text="Reloj de escritorio", font=("TkDefaultFont", 18, "bold")).pack()
        ttk.Label(panel, textvariable=self.hora, font=("TkFixedFont", 34)).pack(pady=28)
        ttk.Label(panel, textvariable=self.estado).pack()
        ttk.Button(panel, text="Finalizar", command=self.cerrar).pack(pady=(24, 0))

    def actualizar_reloj(self):
        self.hora.set(formatear_hora(datetime.now()))
        self.temporizador = self.after(1000, self.actualizar_reloj)

    def cerrar(self):
        if self.temporizador is not None:
            self.after_cancel(self.temporizador)
        self.destroy()


def comprobar():
    assert formatear_hora(datetime(2027, 3, 2, 9, 5, 7)) == "09:05:07"
    print("UNE9D02 OK")


if __name__ == "__main__":
    if "--check" in sys.argv:
        comprobar()
    else:
        Reloj().mainloop()
