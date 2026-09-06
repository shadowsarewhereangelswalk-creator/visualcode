import math
import sys
import tkinter as tk
from tkinter import colorchooser, ttk


def distancia(punto_a, punto_b):
    return math.hypot(punto_b[0] - punto_a[0], punto_b[1] - punto_a[1])


class Pizarra(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Pizarra con Canvas")
        self.geometry("820x560")
        self.minsize(640, 420)
        self.color = tk.StringVar(value="navy")
        self.grosor = tk.IntVar(value=4)
        self.ultimo_punto = None
        self.trazos = 0
        self.estado = tk.StringVar(value="Arrastra el mouse para dibujar")
        self.crear_interfaz()

    def crear_interfaz(self):
        barra = ttk.Frame(self, padding=12)
        barra.pack(fill="x")
        ttk.Button(barra, text="Color", command=self.elegir_color).pack(side="left")
        ttk.Label(barra, text="Grosor").pack(side="left", padx=(14, 4))
        ttk.Spinbox(barra, from_=1, to=20, textvariable=self.grosor, width=5).pack(side="left")
        ttk.Button(barra, text="Limpiar", command=self.limpiar).pack(side="left", padx=12)
        ttk.Label(barra, textvariable=self.estado).pack(side="right")

        self.canvas = tk.Canvas(self, background="white", cursor="crosshair")
        self.canvas.pack(fill="both", expand=True, padx=12, pady=(0, 12))
        self.canvas.bind("<Button-1>", self.iniciar_trazo)
        self.canvas.bind("<B1-Motion>", self.dibujar)
        self.canvas.bind("<ButtonRelease-1>", self.finalizar_trazo)

    def iniciar_trazo(self, evento):
        self.ultimo_punto = evento.x, evento.y

    def dibujar(self, evento):
        actual = evento.x, evento.y
        if self.ultimo_punto is not None and distancia(self.ultimo_punto, actual) > 0:
            self.canvas.create_line(
                *self.ultimo_punto,
                *actual,
                fill=self.color.get(),
                width=self.grosor.get(),
                capstyle="round",
                smooth=True,
            )
            self.trazos += 1
            self.estado.set(f"Segmentos dibujados: {self.trazos}")
        self.ultimo_punto = actual

    def finalizar_trazo(self, evento):
        self.ultimo_punto = None

    def elegir_color(self):
        color = colorchooser.askcolor(color=self.color.get(), parent=self)[1]
        if color:
            self.color.set(color)

    def limpiar(self):
        self.canvas.delete("all")
        self.trazos = 0
        self.estado.set("Lienzo limpio")


def comprobar():
    assert distancia((0, 0), (3, 4)) == 5
    assert round(distancia((2, 2), (5, 6))) == 5
    print("UNE9D12 OK")


if __name__ == "__main__":
    if "--check" in sys.argv:
        comprobar()
    else:
        Pizarra().mainloop()
