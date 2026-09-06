import sys
import tkinter as tk
from tkinter import ttk


TAREAS = (
    "Crear la ventana principal",
    "Configurar título y tamaño",
    "Agregar widgets",
    "Procesar eventos",
    "Cerrar la aplicación",
)


def calcular_progreso(completadas):
    return round(completadas / len(TAREAS) * 100)


class Seguimiento(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Práctica guiada de ventana")
        self.geometry("600x380")
        self.minsize(520, 340)
        self.indice = 0
        self.progreso = tk.DoubleVar(value=0)
        self.tarea = tk.StringVar(value=TAREAS[0])
        self.estado = tk.StringVar(value="Inicia la práctica")
        self.crear_interfaz()

    def crear_interfaz(self):
        panel = ttk.Frame(self, padding=28)
        panel.pack(fill="both", expand=True)
        ttk.Label(panel, text="Ruta de construcción", font=("TkDefaultFont", 18, "bold")).pack(anchor="w")
        ttk.Label(panel, textvariable=self.tarea, font=("TkDefaultFont", 13)).pack(anchor="w", pady=(24, 8))
        ttk.Progressbar(panel, variable=self.progreso, maximum=100).pack(fill="x")
        ttk.Label(panel, textvariable=self.estado).pack(anchor="w", pady=(8, 24))

        acciones = ttk.Frame(panel)
        acciones.pack(fill="x")
        ttk.Button(acciones, text="Completar paso", command=self.avanzar).pack(side="left")
        ttk.Button(acciones, text="Reiniciar", command=self.reiniciar).pack(side="left", padx=8)
        ttk.Button(acciones, text="Cerrar", command=self.destroy).pack(side="right")

    def avanzar(self):
        if self.indice < len(TAREAS):
            self.indice += 1
        self.progreso.set(calcular_progreso(self.indice))
        if self.indice == len(TAREAS):
            self.tarea.set("Práctica completada")
            self.estado.set("La ventana respondió correctamente a todos los eventos")
        else:
            self.tarea.set(TAREAS[self.indice])
            self.estado.set(f"Paso {self.indice} de {len(TAREAS)} completado")

    def reiniciar(self):
        self.indice = 0
        self.progreso.set(0)
        self.tarea.set(TAREAS[0])
        self.estado.set("Inicia la práctica")


def comprobar():
    assert calcular_progreso(0) == 0
    assert calcular_progreso(5) == 100
    print("UNE9D03 OK")


if __name__ == "__main__":
    if "--check" in sys.argv:
        comprobar()
    else:
        Seguimiento().mainloop()
