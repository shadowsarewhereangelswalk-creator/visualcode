import sys
import tkinter as tk
from tkinter import messagebox, ttk


def calcular(numero_a, numero_b, operacion):
    if operacion == "Sumar":
        return numero_a + numero_b
    if operacion == "Restar":
        return numero_a - numero_b
    if operacion == "Multiplicar":
        return numero_a * numero_b
    if operacion == "Dividir":
        if numero_b == 0:
            raise ZeroDivisionError("No se puede dividir entre cero")
        return numero_a / numero_b
    raise ValueError("Selecciona una operación válida")


class Calculadora(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Calculadora con botones")
        self.geometry("520x350")
        self.resizable(False, False)
        self.numero_a = tk.StringVar(value="12")
        self.numero_b = tk.StringVar(value="4")
        self.resultado = tk.StringVar(value="Resultado")
        self.crear_interfaz()

    def crear_interfaz(self):
        panel = ttk.Frame(self, padding=28)
        panel.pack(fill="both", expand=True)
        ttk.Label(panel, text="Calculadora", font=("TkDefaultFont", 18, "bold")).grid(column=0, row=0, columnspan=4, pady=(0, 22))
        ttk.Label(panel, text="Primer número").grid(column=0, row=1, sticky="w")
        ttk.Entry(panel, textvariable=self.numero_a, width=18).grid(column=1, row=1, columnspan=3, sticky="ew")
        ttk.Label(panel, text="Segundo número").grid(column=0, row=2, sticky="w", pady=10)
        ttk.Entry(panel, textvariable=self.numero_b, width=18).grid(column=1, row=2, columnspan=3, sticky="ew", pady=10)

        for columna, operacion in enumerate(("Sumar", "Restar", "Multiplicar", "Dividir")):
            ttk.Button(
                panel,
                text=operacion,
                command=lambda opcion=operacion: self.operar(opcion),
            ).grid(column=columna, row=3, padx=3, pady=12)

        ttk.Label(panel, textvariable=self.resultado, font=("TkDefaultFont", 14, "bold")).grid(column=0, row=4, columnspan=4, pady=14)
        ttk.Button(panel, text="Limpiar", command=self.limpiar).grid(column=0, row=5, columnspan=4)

    def operar(self, operacion):
        try:
            valor = calcular(float(self.numero_a.get()), float(self.numero_b.get()), operacion)
            self.resultado.set(f"Resultado: {valor:g}")
        except (ValueError, ZeroDivisionError) as error:
            messagebox.showerror("Error", str(error), parent=self)

    def limpiar(self):
        self.numero_a.set("")
        self.numero_b.set("")
        self.resultado.set("Resultado")


def comprobar():
    assert calcular(8, 2, "Sumar") == 10
    assert calcular(8, 2, "Dividir") == 4
    print("UNE9D05 OK")


if __name__ == "__main__":
    if "--check" in sys.argv:
        comprobar()
    else:
        Calculadora().mainloop()
