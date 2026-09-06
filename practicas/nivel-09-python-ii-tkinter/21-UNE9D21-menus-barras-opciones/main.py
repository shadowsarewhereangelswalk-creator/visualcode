import sys
import tkinter as tk
from tkinter import messagebox, ttk
from tkinter.scrolledtext import ScrolledText


TAMAÑOS = (10, 12, 14, 16, 18)


def limitar_tamaño(valor):
    valor = int(valor)
    return min(max(valor, min(TAMAÑOS)), max(TAMAÑOS))


class EditorMenu(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Menús y barras de opciones")
        self.geometry("800x540")
        self.minsize(640, 420)
        self.tamaño = tk.IntVar(value=12)
        self.ajuste_linea = tk.BooleanVar(value=True)
        self.tema = tk.StringVar(value="Claro")
        self.crear_menu()
        self.crear_interfaz()

    def crear_menu(self):
        barra = tk.Menu(self)
        archivo = tk.Menu(barra, tearoff=False)
        archivo.add_command(label="Nuevo", command=self.nuevo)
        archivo.add_separator()
        archivo.add_command(label="Cerrar", command=self.destroy)
        barra.add_cascade(label="Archivo", menu=archivo)

        vista = tk.Menu(barra, tearoff=False)
        vista.add_checkbutton(label="Ajuste de línea", variable=self.ajuste_linea, command=self.aplicar_formato)
        tema = tk.Menu(vista, tearoff=False)
        for opcion in ("Claro", "Oscuro"):
            tema.add_radiobutton(label=opcion, value=opcion, variable=self.tema, command=self.aplicar_formato)
        vista.add_cascade(label="Tema", menu=tema)
        barra.add_cascade(label="Vista", menu=vista)

        ayuda = tk.Menu(barra, tearoff=False)
        ayuda.add_command(label="Atajos", command=lambda: messagebox.showinfo("Atajos", "Ctrl+N: nuevo\nCtrl++: aumentar\nCtrl+-: reducir", parent=self))
        barra.add_cascade(label="Ayuda", menu=ayuda)
        self.config(menu=barra)

    def crear_interfaz(self):
        herramientas = ttk.Frame(self, padding=10)
        herramientas.pack(fill="x")
        ttk.Button(herramientas, text="Nuevo", command=self.nuevo).pack(side="left")
        ttk.Button(herramientas, text="A−", command=lambda: self.cambiar_tamaño(-2)).pack(side="left", padx=(8, 2))
        ttk.Button(herramientas, text="A+", command=lambda: self.cambiar_tamaño(2)).pack(side="left")
        ttk.Label(herramientas, text="Tamaño").pack(side="left", padx=(16, 4))
        ttk.Combobox(herramientas, textvariable=self.tamaño, values=TAMAÑOS, width=5, state="readonly").pack(side="left")

        self.editor = ScrolledText(self, undo=True, wrap="word", font=("TkDefaultFont", 12))
        self.editor.pack(fill="both", expand=True, padx=10, pady=(0, 10))
        self.editor.insert("1.0", "Menús, barras de herramientas y opciones de visualización.")

        self.tamaño.trace_add("write", lambda *args: self.aplicar_formato())
        self.bind("<Control-n>", lambda evento: self.nuevo())
        self.bind("<Control-plus>", lambda evento: self.cambiar_tamaño(2))
        self.bind("<Control-minus>", lambda evento: self.cambiar_tamaño(-2))

    def cambiar_tamaño(self, cambio):
        self.tamaño.set(limitar_tamaño(self.tamaño.get() + cambio))

    def aplicar_formato(self):
        tema_oscuro = self.tema.get() == "Oscuro"
        fondo = "gray15" if tema_oscuro else "white"
        texto = "white" if tema_oscuro else "black"
        self.editor.configure(
            font=("TkDefaultFont", self.tamaño.get()),
            wrap="word" if self.ajuste_linea.get() else "none",
            background=fondo,
            foreground=texto,
            insertbackground=texto,
        )

    def nuevo(self):
        self.editor.delete("1.0", "end")


def comprobar():
    assert limitar_tamaño(4) == 10
    assert limitar_tamaño(15) == 15
    assert limitar_tamaño(30) == 18
    print("UNE9D21 OK")


if __name__ == "__main__":
    if "--check" in sys.argv:
        comprobar()
    else:
        EditorMenu().mainloop()
