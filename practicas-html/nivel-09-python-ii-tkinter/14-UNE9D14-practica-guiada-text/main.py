import sys
import tkinter as tk
from tkinter import ttk
from tkinter.scrolledtext import ScrolledText


def contar_coincidencias(texto, termino):
    if not termino:
        return 0
    return texto.casefold().count(termino.casefold())


def reemplazar_todo(texto, termino, reemplazo):
    if not termino:
        return texto
    resultado = []
    inicio = 0
    texto_min = texto.casefold()
    termino_min = termino.casefold()
    while True:
        posicion = texto_min.find(termino_min, inicio)
        if posicion == -1:
            resultado.append(texto[inicio:])
            break
        resultado.append(texto[inicio:posicion])
        resultado.append(reemplazo)
        inicio = posicion + len(termino)
    return "".join(resultado)


class BuscadorTexto(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Búsqueda y reemplazo")
        self.geometry("820x560")
        self.minsize(660, 440)
        self.buscar = tk.StringVar()
        self.reemplazo = tk.StringVar()
        self.estado = tk.StringVar(value="Escribe un término para buscar")
        self.crear_interfaz()

    def crear_interfaz(self):
        barra = ttk.Frame(self, padding=14)
        barra.pack(fill="x")
        ttk.Label(barra, text="Buscar").grid(column=0, row=0, sticky="w")
        ttk.Entry(barra, textvariable=self.buscar, width=22).grid(column=1, row=0, padx=6)
        ttk.Label(barra, text="Reemplazar").grid(column=2, row=0, sticky="w")
        ttk.Entry(barra, textvariable=self.reemplazo, width=22).grid(column=3, row=0, padx=6)
        ttk.Button(barra, text="Buscar", command=self.resaltar).grid(column=4, row=0, padx=4)
        ttk.Button(barra, text="Reemplazar todo", command=self.reemplazar).grid(column=5, row=0)

        self.editor = ScrolledText(self, wrap="word", undo=True, font=("TkDefaultFont", 12))
        self.editor.pack(fill="both", expand=True, padx=14)
        self.editor.insert("1.0", "Tkinter permite crear interfaces de escritorio. Esta práctica usa el widget Text para buscar, resaltar y reemplazar texto.")
        self.editor.tag_configure("coincidencia", background="gold")

        ttk.Label(self, textvariable=self.estado, padding=14).pack(fill="x")

    def resaltar(self):
        self.editor.tag_remove("coincidencia", "1.0", "end")
        termino = self.buscar.get()
        texto = self.editor.get("1.0", "end-1c")
        cantidad = contar_coincidencias(texto, termino)
        if termino:
            inicio = "1.0"
            while True:
                inicio = self.editor.search(termino, inicio, stopindex="end", nocase=True)
                if not inicio:
                    break
                fin = f"{inicio}+{len(termino)}c"
                self.editor.tag_add("coincidencia", inicio, fin)
                inicio = fin
        self.estado.set(f"Coincidencias: {cantidad}")

    def reemplazar(self):
        texto = self.editor.get("1.0", "end-1c")
        actualizado = reemplazar_todo(texto, self.buscar.get(), self.reemplazo.get())
        self.editor.delete("1.0", "end")
        self.editor.insert("1.0", actualizado)
        self.resaltar()


def comprobar():
    texto = "Python y python"
    assert contar_coincidencias(texto, "PYTHON") == 2
    assert reemplazar_todo(texto, "python", "Tkinter") == "Tkinter y Tkinter"
    print("UNE9D14 OK")


if __name__ == "__main__":
    if "--check" in sys.argv:
        comprobar()
    else:
        BuscadorTexto().mainloop()
