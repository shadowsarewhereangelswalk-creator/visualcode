import sys
import tkinter as tk
from decimal import Decimal, InvalidOperation, ROUND_HALF_UP
from tkinter import ttk


def calcular_cotizacion(servicio, precio, horas, descuento):
    servicio = " ".join(servicio.split()).title()
    try:
        precio = Decimal(precio)
        horas = Decimal(horas)
        descuento = Decimal(descuento) / Decimal("100")
    except InvalidOperation as error:
        raise ValueError("Precio, horas y descuento deben ser numéricos") from error
    if not servicio:
        raise ValueError("Escribe el servicio")
    if precio <= 0 or horas <= 0:
        raise ValueError("Precio y horas deben ser positivos")
    if not Decimal("0") <= descuento <= Decimal("1"):
        raise ValueError("El descuento debe estar entre 0 y 100")
    subtotal = precio * horas
    total = subtotal * (Decimal("1") - descuento)
    return servicio, subtotal.quantize(Decimal("0.01")), total.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)


class Cotizador(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Cotizador con Entry")
        self.geometry("600x420")
        self.resizable(False, False)
        self.servicio = tk.StringVar(value="Automatización")
        self.precio = tk.StringVar(value="45")
        self.horas = tk.StringVar(value="12")
        self.descuento = tk.StringVar(value="10")
        self.resultado = tk.StringVar(value="Completa los datos y calcula")
        self.crear_interfaz()

    def crear_interfaz(self):
        panel = ttk.Frame(self, padding=30)
        panel.pack(fill="both", expand=True)
        ttk.Label(panel, text="Cotizador de servicios", font=("TkDefaultFont", 18, "bold")).grid(column=0, row=0, columnspan=2, sticky="w", pady=(0, 20))

        for fila, (etiqueta, variable) in enumerate(
            (
                ("Servicio", self.servicio),
                ("Precio por hora", self.precio),
                ("Horas", self.horas),
                ("Descuento %", self.descuento),
            ),
            start=1,
        ):
            ttk.Label(panel, text=etiqueta).grid(column=0, row=fila, sticky="w", pady=6)
            ttk.Entry(panel, textvariable=variable).grid(column=1, row=fila, sticky="ew", pady=6)

        ttk.Button(panel, text="Calcular", command=self.calcular).grid(column=1, row=5, sticky="e", pady=(18, 0))
        ttk.Label(panel, textvariable=self.resultado, wraplength=500).grid(column=0, row=6, columnspan=2, sticky="w", pady=(24, 0))
        panel.columnconfigure(1, weight=1)

    def calcular(self):
        try:
            servicio, subtotal, total = calcular_cotizacion(
                self.servicio.get(),
                self.precio.get(),
                self.horas.get(),
                self.descuento.get(),
            )
            self.resultado.set(f"{servicio} · subtotal {subtotal:.2f} · total {total:.2f}")
        except ValueError as error:
            self.resultado.set(str(error))


def comprobar():
    servicio, subtotal, total = calcular_cotizacion("automatización", "50", "10", "10")
    assert servicio == "Automatización"
    assert subtotal == Decimal("500.00")
    assert total == Decimal("450.00")
    print("UNE9D07 OK")


if __name__ == "__main__":
    if "--check" in sys.argv:
        comprobar()
    else:
        Cotizador().mainloop()
