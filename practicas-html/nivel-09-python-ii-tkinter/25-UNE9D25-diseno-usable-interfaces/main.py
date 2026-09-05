import re
import sys
import tkinter as tk
from tkinter import ttk


SERVICIOS = ("Consulta", "Desarrollo", "Soporte")


def validar_solicitud(nombre, correo, servicio, mensaje):
    errores = {}
    nombre = " ".join(nombre.split()).title()
    correo = correo.strip().lower()
    mensaje = mensaje.strip()
    if len(nombre) < 3:
        errores["nombre"] = "Escribe tu nombre completo"
    if re.fullmatch(r"[^@\s]+@[^@\s]+\.[A-Za-z]{2,}", correo) is None:
        errores["correo"] = "Escribe un correo válido"
    if servicio not in SERVICIOS:
        errores["servicio"] = "Selecciona un servicio"
    if len(mensaje) < 10:
        errores["mensaje"] = "Describe tu solicitud con al menos 10 caracteres"
    if errores:
        raise ValueError(errores)
    return nombre, correo, servicio, mensaje


class SolicitudUsable(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Diseño usable de interfaces")
        self.geometry("700x560")
        self.minsize(620, 520)
        self.nombre = tk.StringVar()
        self.correo = tk.StringVar()
        self.servicio = tk.StringVar(value=SERVICIOS[0])
        self.estado = tk.StringVar(value="Todos los campos son obligatorios")
        self.alto_contraste = tk.BooleanVar()
        self.crear_interfaz()

    def crear_interfaz(self):
        self.panel = ttk.Frame(self, padding=28)
        self.panel.pack(fill="both", expand=True)
        ttk.Label(self.panel, text="Solicitud de servicio", font=("TkDefaultFont", 20, "bold")).grid(column=0, row=0, columnspan=2, sticky="w")
        ttk.Label(self.panel, text="Completa los datos. Usa Tab para navegar.").grid(column=0, row=1, columnspan=2, sticky="w", pady=(4, 20))

        ttk.Label(self.panel, text="Nombre completo", underline=0).grid(column=0, row=2, sticky="w", pady=7)
        self.entrada_nombre = ttk.Entry(self.panel, textvariable=self.nombre)
        self.entrada_nombre.grid(column=1, row=2, sticky="ew", pady=7)

        ttk.Label(self.panel, text="Correo electrónico", underline=0).grid(column=0, row=3, sticky="w", pady=7)
        self.entrada_correo = ttk.Entry(self.panel, textvariable=self.correo)
        self.entrada_correo.grid(column=1, row=3, sticky="ew", pady=7)

        ttk.Label(self.panel, text="Servicio", underline=0).grid(column=0, row=4, sticky="w", pady=7)
        self.selector_servicio = ttk.Combobox(self.panel, textvariable=self.servicio, values=SERVICIOS, state="readonly")
        self.selector_servicio.grid(column=1, row=4, sticky="ew", pady=7)

        ttk.Label(self.panel, text="Mensaje", underline=0).grid(column=0, row=5, sticky="nw", pady=7)
        self.mensaje = tk.Text(self.panel, height=8, wrap="word")
        self.mensaje.grid(column=1, row=5, sticky="nsew", pady=7)

        ttk.Checkbutton(
            self.panel,
            text="Alto contraste",
            variable=self.alto_contraste,
            command=self.aplicar_contraste,
        ).grid(column=0, row=6, sticky="w", pady=(14, 0))
        ttk.Button(self.panel, text="Enviar solicitud", command=self.enviar).grid(column=1, row=6, sticky="e", pady=(14, 0))
        self.etiqueta_estado = ttk.Label(self.panel, textvariable=self.estado, wraplength=580)
        self.etiqueta_estado.grid(column=0, row=7, columnspan=2, sticky="w", pady=(18, 0))

        self.panel.columnconfigure(1, weight=1)
        self.panel.rowconfigure(5, weight=1)
        self.entrada_nombre.focus_set()
        self.bind("<Alt-n>", lambda evento: self.entrada_nombre.focus_set())
        self.bind("<Alt-c>", lambda evento: self.entrada_correo.focus_set())
        self.bind("<Alt-s>", lambda evento: self.selector_servicio.focus_set())
        self.bind("<Alt-m>", lambda evento: self.mensaje.focus_set())
        self.bind("<Control-Return>", lambda evento: self.enviar())

    def aplicar_contraste(self):
        fondo = "black" if self.alto_contraste.get() else "white"
        texto = "yellow" if self.alto_contraste.get() else "black"
        self.mensaje.configure(background=fondo, foreground=texto, insertbackground=texto)

    def enviar(self):
        try:
            solicitud = validar_solicitud(
                self.nombre.get(),
                self.correo.get(),
                self.servicio.get(),
                self.mensaje.get("1.0", "end-1c"),
            )
            self.estado.set(f"Solicitud enviada para {solicitud[0]} · {solicitud[2]}")
        except ValueError as error:
            errores = error.args[0]
            orden = (
                ("nombre", self.entrada_nombre),
                ("correo", self.entrada_correo),
                ("servicio", self.selector_servicio),
                ("mensaje", self.mensaje),
            )
            for campo, widget in orden:
                if campo in errores:
                    self.estado.set(errores[campo])
                    widget.focus_set()
                    break


def comprobar():
    solicitud = validar_solicitud(
        "Ana Torres",
        "ana@ejemplo.com",
        "Desarrollo",
        "Necesito una aplicación de escritorio",
    )
    assert solicitud[0] == "Ana Torres"
    assert solicitud[2] == "Desarrollo"
    print("UNE9D25 OK")


if __name__ == "__main__":
    if "--check" in sys.argv:
        comprobar()
    else:
        SolicitudUsable().mainloop()
