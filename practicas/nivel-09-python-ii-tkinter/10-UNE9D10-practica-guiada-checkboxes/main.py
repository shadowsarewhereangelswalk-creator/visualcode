import sys
import tkinter as tk
from tkinter import ttk


CANALES = ("Correo", "WhatsApp", "Teléfono")
HORARIOS = ("Mañana", "Tarde", "Noche")


def crear_preferencia(nombre, canales, horario, acepta):
    nombre = " ".join(nombre.split()).title()
    if not nombre:
        raise ValueError("Escribe el nombre")
    if not canales:
        raise ValueError("Selecciona al menos un canal")
    if horario not in HORARIOS:
        raise ValueError("Selecciona un horario")
    if not acepta:
        raise ValueError("Debes aceptar el uso de los datos")
    return {
        "nombre": nombre,
        "canales": tuple(canales),
        "horario": horario,
        "acepta": acepta,
    }


class Preferencias(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Preferencias de contacto")
        self.geometry("600x460")
        self.resizable(False, False)
        self.nombre = tk.StringVar()
        self.canales = {canal: tk.BooleanVar() for canal in CANALES}
        self.horario = tk.StringVar(value=HORARIOS[0])
        self.acepta = tk.BooleanVar()
        self.resultado = tk.StringVar(value="Configura las preferencias")
        self.crear_interfaz()

    def crear_interfaz(self):
        panel = ttk.Frame(self, padding=28)
        panel.pack(fill="both", expand=True)
        ttk.Label(panel, text="Preferencias de contacto", font=("TkDefaultFont", 18, "bold")).grid(column=0, row=0, columnspan=2, sticky="w", pady=(0, 18))
        ttk.Label(panel, text="Nombre").grid(column=0, row=1, sticky="w")
        ttk.Entry(panel, textvariable=self.nombre, width=34).grid(column=1, row=1, sticky="ew")

        ttk.Label(panel, text="Canales").grid(column=0, row=2, sticky="nw", pady=(16, 0))
        caja_canales = ttk.Frame(panel)
        caja_canales.grid(column=1, row=2, sticky="w", pady=(12, 0))
        for canal in CANALES:
            ttk.Checkbutton(caja_canales, text=canal, variable=self.canales[canal]).pack(anchor="w")

        ttk.Label(panel, text="Horario").grid(column=0, row=3, sticky="nw", pady=(16, 0))
        caja_horarios = ttk.Frame(panel)
        caja_horarios.grid(column=1, row=3, sticky="w", pady=(12, 0))
        for horario in HORARIOS:
            ttk.Radiobutton(caja_horarios, text=horario, value=horario, variable=self.horario).pack(side="left", padx=(0, 8))

        ttk.Checkbutton(panel, text="Acepto el uso de mis datos", variable=self.acepta).grid(column=0, row=4, columnspan=2, sticky="w", pady=18)
        ttk.Button(panel, text="Guardar preferencias", command=self.guardar).grid(column=1, row=5, sticky="e")
        ttk.Label(panel, textvariable=self.resultado, wraplength=500).grid(column=0, row=6, columnspan=2, sticky="w", pady=(22, 0))
        panel.columnconfigure(1, weight=1)

    def guardar(self):
        try:
            seleccionados = [canal for canal, variable in self.canales.items() if variable.get()]
            preferencia = crear_preferencia(
                self.nombre.get(),
                seleccionados,
                self.horario.get(),
                self.acepta.get(),
            )
            canales = ", ".join(preferencia["canales"])
            self.resultado.set(f'{preferencia["nombre"]} · {canales} · {preferencia["horario"]}')
        except ValueError as error:
            self.resultado.set(str(error))


def comprobar():
    datos = crear_preferencia(" ana ", ["Correo", "WhatsApp"], "Tarde", True)
    assert datos["nombre"] == "Ana"
    assert len(datos["canales"]) == 2
    print("UNE9D10 OK")


if __name__ == "__main__":
    if "--check" in sys.argv:
        comprobar()
    else:
        Preferencias().mainloop()
