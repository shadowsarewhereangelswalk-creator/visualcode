import re
import sys
import tkinter as tk
from pathlib import Path
from tkinter import filedialog, messagebox, simpledialog, ttk
from tkinter.scrolledtext import ScrolledText


def estadisticas(texto):
    palabras = re.findall(r"\b\w+\b", texto, flags=re.UNICODE)
    return len(palabras), len(texto)


class EditorProyectos(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("P2 — Editor de proyectos")
        self.geometry("900x620")
        self.minsize(700, 500)
        self.ruta = None
        self.estado = tk.StringVar(value="Documento nuevo")
        self.crear_menu()
        self.crear_interfaz()
        self.protocol("WM_DELETE_WINDOW", self.salir)

    def crear_menu(self):
        barra = tk.Menu(self)
        archivo = tk.Menu(barra, tearoff=False)
        archivo.add_command(label="Nuevo", command=self.nuevo, accelerator="Ctrl+N")
        archivo.add_command(label="Abrir", command=self.abrir, accelerator="Ctrl+O")
        archivo.add_command(label="Guardar", command=self.guardar, accelerator="Ctrl+S")
        archivo.add_command(label="Guardar como", command=self.guardar_como)
        archivo.add_separator()
        archivo.add_command(label="Salir", command=self.salir)
        barra.add_cascade(label="Archivo", menu=archivo)

        edicion = tk.Menu(barra, tearoff=False)
        edicion.add_command(label="Título del proyecto", command=self.insertar_titulo)
        edicion.add_command(label="Deshacer", command=lambda: self.editor.event_generate("<<Undo>>"))
        edicion.add_command(label="Rehacer", command=lambda: self.editor.event_generate("<<Redo>>"))
        barra.add_cascade(label="Edición", menu=edicion)

        ayuda = tk.Menu(barra, tearoff=False)
        ayuda.add_command(label="Acerca de", command=lambda: messagebox.showinfo("Acerca de", "Editor de proyectos · Nivel 9", parent=self))
        barra.add_cascade(label="Ayuda", menu=ayuda)
        self.config(menu=barra)

    def crear_interfaz(self):
        principal = ttk.Frame(self, padding=12)
        principal.grid(sticky="nsew")
        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)
        principal.rowconfigure(1, weight=1)
        principal.columnconfigure(0, weight=1)

        herramientas = ttk.Frame(principal)
        herramientas.grid(column=0, row=0, sticky="ew", pady=(0, 10))
        ttk.Button(herramientas, text="Nuevo", command=self.nuevo).pack(side="left")
        ttk.Button(herramientas, text="Abrir", command=self.abrir).pack(side="left", padx=6)
        ttk.Button(herramientas, text="Guardar", command=self.guardar).pack(side="left")
        ttk.Label(herramientas, textvariable=self.estado).pack(side="right")

        self.editor = ScrolledText(principal, wrap="word", undo=True, font=("TkDefaultFont", 12))
        self.editor.grid(column=0, row=1, sticky="nsew")
        self.editor.bind("<<Modified>>", self.marcar_cambios)

        self.bind("<Control-n>", lambda evento: self.nuevo())
        self.bind("<Control-o>", lambda evento: self.abrir())
        self.bind("<Control-s>", lambda evento: self.guardar())

    def marcar_cambios(self, evento=None):
        if self.editor.edit_modified():
            palabras, caracteres = estadisticas(self.editor.get("1.0", "end-1c"))
            self.estado.set(f"Sin guardar · {palabras} palabras · {caracteres} caracteres")
            self.editor.edit_modified(False)

    def nuevo(self):
        if messagebox.askyesno("Nuevo", "¿Crear un documento nuevo?", parent=self):
            self.editor.delete("1.0", "end")
            self.ruta = None
            self.estado.set("Documento nuevo")

    def abrir(self):
        ruta = filedialog.askopenfilename(
            parent=self,
            filetypes=(("Texto", "*.txt"), ("Todos", "*.*")),
        )
        if ruta:
            self.ruta = Path(ruta)
            self.editor.delete("1.0", "end")
            self.editor.insert("1.0", self.ruta.read_text(encoding="utf-8"))
            self.estado.set(self.ruta.name)

    def guardar(self):
        if self.ruta is None:
            return self.guardar_como()
        self.ruta.write_text(self.editor.get("1.0", "end-1c"), encoding="utf-8")
        self.estado.set(f"Guardado · {self.ruta.name}")
        return True

    def guardar_como(self):
        ruta = filedialog.asksaveasfilename(
            parent=self,
            defaultextension=".txt",
            filetypes=(("Texto", "*.txt"),),
        )
        if not ruta:
            return False
        self.ruta = Path(ruta)
        return self.guardar()

    def insertar_titulo(self):
        titulo = simpledialog.askstring("Título", "Nombre del proyecto", parent=self)
        if titulo:
            self.editor.insert("1.0", f"{titulo.strip().title()}\n{'=' * len(titulo.strip())}\n\n")

    def salir(self):
        if messagebox.askokcancel("Salir", "¿Cerrar el editor?", parent=self):
            self.destroy()


def comprobar():
    assert estadisticas("Proyecto Tkinter completo") == (3, 25)
    print("UNE9D15 OK")


if __name__ == "__main__":
    if "--check" in sys.argv:
        comprobar()
    else:
        EditorProyectos().mainloop()
