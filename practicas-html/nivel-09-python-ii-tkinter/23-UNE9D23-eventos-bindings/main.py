import re
import sys
import tkinter as tk
from tkinter import messagebox, ttk


def validar_formulario(nombre, correo):
    nombre = " ".join(nombre.split()).title()
    correo = correo.strip().lower()
    if not nombre:
        raise ValueError("El nombre es obligatorio")
    if re.fullmatch(r"[^@\s]+@[^@\s]+\.[A-Za-z]{2,}", correo) is None:
        raise ValueError("El correo no es válido")
    return nombre, correo


class FormularioEventos(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Gestión de eventos y bindings")
        self.geometry("620x430")
        self.resizable(False, False)
        self.nombre = tk.StringVar()
        self.correo = tk.StringVar()
        self.estado = tk.StringVar(value="Ctrl+Enter para guardar · Esc para limpiar")
        self.crear_interfaz()
        self.crear_bindings()

    def crear_interfaz(self):
        panel = ttk.Frame(self, padding=30)
        panel.pack(fill="both", expand=True)
        ttk.Label(panel, text="Registro rápido", font=("TkDefaultFont", 18, "bold")).grid(column=0, row=0, columnspan=2, sticky="w", pady=(0, 22))
        ttk.Label(panel, text="Nombre").grid(column=0, row=1, sticky="w", pady=8)
        self.entrada_nombre = ttk.Entry(panel, textvariable=self.nombre)
        self.entrada_nombre.grid(column=1, row=1, sticky="ew", pady=8)
        ttk.Label(panel, text="Correo").grid(column=0, row=2, sticky="w", pady=8)
        self.entrada_correo = ttk.Entry(panel, textvariable=self.correo)
        self.entrada_correo.grid(column=1, row=2, sticky="ew", pady=8)

        acciones = ttk.Frame(panel)
        acciones.grid(column=0, row=3, columnspan=2, sticky="e", pady=18)
        self.boton_limpiar = ttk.Button(acciones, text="Limpiar", command=self.limpiar)
        self.boton_limpiar.pack(side="left")
        self.boton_guardar = ttk.Button(acciones, text="Guardar", command=self.guardar)
        self.boton_guardar.pack(side="left", padx=(8, 0))
        ttk.Label(panel, textvariable=self.estado, wraplength=500).grid(column=0, row=4, columnspan=2, sticky="w")
        panel.columnconfigure(1, weight=1)
        self.entrada_nombre.focus_set()

    def crear_bindings(self):
        self.bind("<Control-Return>", lambda evento: self.guardar())
        self.bind("<Escape>", lambda evento: self.limpiar())
        self.bind("<F1>", lambda evento: messagebox.showinfo("Atajos", "Ctrl+Enter: guardar\nEsc: limpiar", parent=self))
        self.entrada_correo.bind("<FocusOut>", self.validar_correo_visual)
        for boton in (self.boton_limpiar, self.boton_guardar):
            boton.bind("<Enter>", lambda evento: self.estado.set(f'Acción: {evento.widget.cget("text")}'))
            boton.bind("<Leave>", lambda evento: self.estado.set("Ctrl+Enter para guardar · Esc para limpiar"))

    def validar_correo_visual(self, evento=None):
        correo = self.correo.get().strip()
        if correo and "@" not in correo:
            self.estado.set("El correo debe incluir @")

    def guardar(self):
        try:
            nombre, correo = validar_formulario(self.nombre.get(), self.correo.get())
            self.estado.set(f"Guardado: {nombre} · {correo}")
        except ValueError as error:
            self.estado.set(str(error))

    def limpiar(self):
        self.nombre.set("")
        self.correo.set("")
        self.estado.set("Formulario limpio")
        self.entrada_nombre.focus_set()


def comprobar():
    assert validar_formulario(" ana torres ", "ANA@EJEMPLO.COM") == ("Ana Torres", "ana@ejemplo.com")
    print("UNE9D23 OK")


if __name__ == "__main__":
    if "--check" in sys.argv:
        comprobar()
    else:
        FormularioEventos().mainloop()
