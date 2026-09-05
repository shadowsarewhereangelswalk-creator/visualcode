import sys
import tkinter as tk
from tkinter import ttk


def posicion_relativa(ancho, alto, relx, rely):
    return round(ancho * relx), round(alto * rely)


class GaleriaLayouts(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Layouts con pack, grid y place")
        self.geometry("760x500")
        self.minsize(620, 420)
        self.crear_interfaz()

    def crear_interfaz(self):
        cuaderno = ttk.Notebook(self)
        cuaderno.pack(fill="both", expand=True, padx=16, pady=16)

        pestaña_pack = ttk.Frame(cuaderno, padding=20)
        pestaña_grid = ttk.Frame(cuaderno, padding=20)
        pestaña_place = ttk.Frame(cuaderno)
        cuaderno.add(pestaña_pack, text="pack")
        cuaderno.add(pestaña_grid, text="grid")
        cuaderno.add(pestaña_place, text="place")

        ttk.Label(pestaña_pack, text="Encabezado", font=("TkDefaultFont", 16, "bold")).pack(fill="x", pady=(0, 14))
        ttk.Button(pestaña_pack, text="Acción izquierda").pack(side="left")
        ttk.Button(pestaña_pack, text="Acción derecha").pack(side="right")
        ttk.Label(pestaña_pack, text="Contenido flexible", anchor="center").pack(fill="both", expand=True)

        for fila in range(3):
            pestaña_grid.rowconfigure(fila, weight=1)
            for columna in range(3):
                pestaña_grid.columnconfigure(columna, weight=1)
                ttk.Button(
                    pestaña_grid,
                    text=f"Fila {fila + 1} · Columna {columna + 1}",
                ).grid(column=columna, row=fila, sticky="nsew", padx=4, pady=4)

        ttk.Label(
            pestaña_place,
            text="Elemento centrado",
            font=("TkDefaultFont", 18, "bold"),
        ).place(relx=0.5, rely=0.45, anchor="center")
        ttk.Button(pestaña_place, text="Esquina inferior").place(relx=0.98, rely=0.96, anchor="se")


def comprobar():
    assert posicion_relativa(800, 600, 0.5, 0.25) == (400, 150)
    print("UNE9D18 OK")


if __name__ == "__main__":
    if "--check" in sys.argv:
        comprobar()
    else:
        GaleriaLayouts().mainloop()
