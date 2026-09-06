import sys
import tkinter as tk
from tkinter import ttk


INDICADORES = (
    ("Clientes", 128),
    ("Cotizaciones", 46),
    ("Aprobadas", 31),
)


def porcentaje(parte, total):
    return 0 if total == 0 else round(parte / total * 100, 1)


class Tablero(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Tablero con layouts personalizados")
        self.geometry("940x600")
        self.minsize(720, 500)
        self.tamaño = tk.StringVar()
        self.crear_interfaz()
        self.bind("<Configure>", self.actualizar_tamaño)

    def crear_interfaz(self):
        encabezado = ttk.Frame(self, padding=16)
        encabezado.pack(fill="x")
        ttk.Label(encabezado, text="Panel de ventas", font=("TkDefaultFont", 20, "bold")).pack(side="left")
        ttk.Label(encabezado, textvariable=self.tamaño).pack(side="right")

        cuerpo = ttk.Frame(self)
        cuerpo.pack(fill="both", expand=True)
        lateral = ttk.Frame(cuerpo, padding=14)
        lateral.pack(side="left", fill="y")
        for opcion in ("Resumen", "Clientes", "Cotizaciones", "Reportes"):
            ttk.Button(lateral, text=opcion, width=18).pack(fill="x", pady=4)

        contenido = ttk.Frame(cuerpo, padding=18)
        contenido.pack(side="left", fill="both", expand=True)
        contenido.columnconfigure((0, 1, 2), weight=1)
        contenido.rowconfigure(1, weight=1)

        for columna, (titulo, valor) in enumerate(INDICADORES):
            tarjeta = ttk.LabelFrame(contenido, text=titulo, padding=18)
            tarjeta.grid(column=columna, row=0, sticky="nsew", padx=6)
            ttk.Label(tarjeta, text=str(valor), font=("TkDefaultFont", 24, "bold")).pack()

        detalle = ttk.LabelFrame(contenido, text="Conversión", padding=18)
        detalle.grid(column=0, row=1, columnspan=3, sticky="nsew", padx=6, pady=(16, 0))
        conversion = porcentaje(INDICADORES[2][1], INDICADORES[1][1])
        ttk.Label(detalle, text=f"{conversion}%", font=("TkDefaultFont", 36, "bold")).place(relx=0.5, rely=0.45, anchor="center")
        ttk.Label(detalle, text="Cotizaciones aprobadas").place(relx=0.5, rely=0.62, anchor="center")

    def actualizar_tamaño(self, evento):
        if evento.widget is self:
            self.tamaño.set(f"{evento.width} × {evento.height}")


def comprobar():
    assert porcentaje(31, 46) == 67.4
    assert porcentaje(0, 0) == 0
    print("UNE9D19 OK")


if __name__ == "__main__":
    if "--check" in sys.argv:
        comprobar()
    else:
        Tablero().mainloop()
