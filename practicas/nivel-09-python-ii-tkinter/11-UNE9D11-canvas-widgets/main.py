import sys
import tkinter as tk
from tkinter import ttk


VENTAS = (("Enero", 18), ("Febrero", 26), ("Marzo", 34), ("Abril", 29), ("Mayo", 42))


def calcular_barras(datos, ancho, alto, margen=40):
    maximo = max(valor for _, valor in datos)
    espacio = (ancho - margen * 2) / len(datos)
    barras = []
    for indice, (etiqueta, valor) in enumerate(datos):
        x1 = margen + indice * espacio + 10
        x2 = margen + (indice + 1) * espacio - 10
        y2 = alto - margen
        y1 = y2 - (alto - margen * 2) * valor / maximo
        barras.append((etiqueta, valor, x1, y1, x2, y2))
    return barras


class Grafico(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Canvas widgets")
        self.geometry("760x500")
        self.minsize(620, 420)
        self.estado = tk.StringVar(value="Pasa el cursor sobre una barra")
        self.crear_interfaz()

    def crear_interfaz(self):
        panel = ttk.Frame(self, padding=20)
        panel.pack(fill="both", expand=True)
        ttk.Label(panel, text="Ventas mensuales", font=("TkDefaultFont", 18, "bold")).pack(anchor="w")
        self.canvas = tk.Canvas(panel, background="white", highlightthickness=1)
        self.canvas.pack(fill="both", expand=True, pady=14)
        ttk.Label(panel, textvariable=self.estado).pack(anchor="w")
        self.canvas.bind("<Configure>", self.dibujar)

    def dibujar(self, evento=None):
        self.canvas.delete("all")
        ancho = max(self.canvas.winfo_width(), 400)
        alto = max(self.canvas.winfo_height(), 260)
        self.canvas.create_line(40, alto - 40, ancho - 30, alto - 40, width=2)
        for indice, (etiqueta, valor, x1, y1, x2, y2) in enumerate(calcular_barras(VENTAS, ancho, alto)):
            etiqueta_barra = f"barra-{indice}"
            self.canvas.create_rectangle(x1, y1, x2, y2, fill="steelblue", outline="", tags=(etiqueta_barra,))
            self.canvas.create_text((x1 + x2) / 2, y1 - 12, text=str(valor))
            self.canvas.create_text((x1 + x2) / 2, y2 + 16, text=etiqueta)
            self.canvas.tag_bind(etiqueta_barra, "<Enter>", lambda evento, texto=etiqueta, dato=valor: self.estado.set(f"{texto}: {dato} ventas"))
            self.canvas.tag_bind(etiqueta_barra, "<Leave>", lambda evento: self.estado.set("Pasa el cursor sobre una barra"))


def comprobar():
    barras = calcular_barras(VENTAS, 700, 360)
    assert len(barras) == 5
    assert barras[-1][1] == 42
    assert all(barra[3] < barra[5] for barra in barras)
    print("UNE9D11 OK")


if __name__ == "__main__":
    if "--check" in sys.argv:
        comprobar()
    else:
        Grafico().mainloop()
