import sys
import tkinter as tk
from pathlib import Path
from tkinter import filedialog, messagebox, ttk
from tkinter.scrolledtext import ScrolledText


def resumen_archivo(ruta, contenido):
    lineas = contenido.count("\n") + (1 if contenido else 0)
    return f"{Path(ruta).name} · {len(contenido)} caracteres · {lineas} líneas"


class GestorArchivos(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Diálogos de mensajes y archivos")
        self.geometry("780x520")
        self.minsize(620, 420)
        self.ruta = None
        self.estado = tk.StringVar(value="Ningún archivo seleccionado")
        self.crear_interfaz()

    def crear_interfaz(self):
        barra = ttk.Frame(self, padding=12)
        barra.pack(fill="x")
        ttk.Button(barra, text="Abrir", command=self.abrir).pack(side="left")
        ttk.Button(barra, text="Guardar como", command=self.guardar).pack(side="left", padx=8)
        ttk.Button(barra, text="Información", command=self.informar).pack(side="left")
        ttk.Label(barra, textvariable=self.estado).pack(side="right")

        self.editor = ScrolledText(self, wrap="word", undo=True, font=("TkDefaultFont", 12))
        self.editor.pack(fill="both", expand=True, padx=12, pady=(0, 12))

    def abrir(self):
        ruta = filedialog.askopenfilename(
            parent=self,
            title="Abrir archivo",
            filetypes=(("Archivos de texto", "*.txt"), ("Todos", "*.*")),
        )
        if not ruta:
            return
        self.ruta = Path(ruta)
        try:
            contenido = self.ruta.read_text(encoding="utf-8")
        except (OSError, UnicodeDecodeError) as error:
            messagebox.showerror("No se pudo abrir", str(error), parent=self)
            return
        self.editor.delete("1.0", "end")
        self.editor.insert("1.0", contenido)
        self.estado.set(resumen_archivo(self.ruta, contenido))

    def guardar(self):
        ruta = filedialog.asksaveasfilename(
            parent=self,
            title="Guardar archivo",
            defaultextension=".txt",
            filetypes=(("Archivos de texto", "*.txt"),),
        )
        if not ruta:
            return
        contenido = self.editor.get("1.0", "end-1c")
        try:
            Path(ruta).write_text(contenido, encoding="utf-8")
        except OSError as error:
            messagebox.showerror("No se pudo guardar", str(error), parent=self)
            return
        self.ruta = Path(ruta)
        self.estado.set(resumen_archivo(self.ruta, contenido))
        messagebox.showinfo("Guardado", "El archivo se guardó correctamente", parent=self)

    def informar(self):
        contenido = self.editor.get("1.0", "end-1c")
        texto = resumen_archivo(self.ruta or "sin_nombre.txt", contenido)
        messagebox.showinfo("Documento actual", texto, parent=self)


def comprobar():
    assert resumen_archivo("/tmp/notas.txt", "uno\ndos") == "notas.txt · 7 caracteres · 2 líneas"
    print("UNE9D16 OK")


if __name__ == "__main__":
    if "--check" in sys.argv:
        comprobar()
    else:
        GestorArchivos().mainloop()
