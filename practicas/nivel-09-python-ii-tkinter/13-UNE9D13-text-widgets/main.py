import re
import sys
import tkinter as tk
from tkinter import ttk
from tkinter.scrolledtext import ScrolledText


def estadisticas(texto):
    palabras = re.findall(r"\b[\wáéíóúüñÁÉÍÓÚÜÑ]+\b", texto)
    lineas = texto.count("\n") + (1 if texto else 0)
    return len(palabras), len(texto), lineas


class Editor(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Text widgets")
        self.geometry("760x520")
        self.minsize(600, 420)
        self.estado = tk.StringVar(value="0 palabras · 0 caracteres · 0 líneas")
        self.crear_interfaz()

    def crear_interfaz(self):
        encabezado = ttk.Frame(self, padding=(18, 14))
        encabezado.pack(fill="x")
        ttk.Label(encabezado, text="Editor de notas", font=("TkDefaultFont", 18, "bold")).pack(side="left")
        ttk.Button(encabezado, text="Limpiar", command=self.limpiar).pack(side="right")

        self.editor = ScrolledText(self, wrap="word", undo=True, font=("TkDefaultFont", 12))
        self.editor.pack(fill="both", expand=True, padx=18, pady=(0, 10))
        self.editor.insert("1.0", "Ideas para la aplicación CRUD\n\n1. Diseñar la interfaz\n2. Conectar la base de datos\n3. Validar las operaciones")
        self.editor.bind("<<Modified>>", self.actualizar_estado)

        ttk.Label(self, textvariable=self.estado, padding=(18, 8)).pack(fill="x")
        self.actualizar_estado()

    def actualizar_estado(self, evento=None):
        texto = self.editor.get("1.0", "end-1c")
        palabras, caracteres, lineas = estadisticas(texto)
        self.estado.set(f"{palabras} palabras · {caracteres} caracteres · {lineas} líneas")
        self.editor.edit_modified(False)

    def limpiar(self):
        self.editor.delete("1.0", "end")
        self.actualizar_estado()


def comprobar():
    assert estadisticas("Hola mundo\nSegunda línea") == (4, 24, 2)
    print("UNE9D13 OK")


if __name__ == "__main__":
    if "--check" in sys.argv:
        comprobar()
    else:
        Editor().mainloop()
