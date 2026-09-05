import sys
import tkinter as tk
from tkinter import ttk


TAREAS = (
    ("Diseñar interfaz", 80, 90),
    ("Programar eventos", 300, 180),
    ("Validar solución", 520, 100),
)


def limitar(valor, minimo, maximo):
    return max(minimo, min(valor, maximo))


class TableroArrastrable(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Práctica guiada de eventos")
        self.geometry("820x560")
        self.minsize(660, 460)
        self.arrastre = None
        self.estado = tk.StringVar(value="Arrastra las tarjetas con el mouse")
        self.crear_interfaz()

    def crear_interfaz(self):
        barra = ttk.Frame(self, padding=12)
        barra.pack(fill="x")
        ttk.Label(barra, text="Tablero de tareas", font=("TkDefaultFont", 18, "bold")).pack(side="left")
        ttk.Button(barra, text="Reiniciar", command=self.crear_tarjetas).pack(side="right")

        self.canvas = tk.Canvas(self, background="white")
        self.canvas.pack(fill="both", expand=True, padx=12)
        ttk.Label(self, textvariable=self.estado, padding=12).pack(fill="x")

        self.canvas.bind("<Button-1>", self.iniciar_arrastre)
        self.canvas.bind("<B1-Motion>", self.arrastrar)
        self.canvas.bind("<ButtonRelease-1>", self.finalizar_arrastre)
        self.canvas.bind("<Double-Button-1>", self.completar)
        self.after_idle(self.crear_tarjetas)

    def crear_tarjetas(self):
        self.canvas.delete("all")
        for indice, (texto, x, y) in enumerate(TAREAS):
            etiqueta = f"tarea-{indice}"
            self.canvas.create_rectangle(x, y, x + 170, y + 80, fill="lightsteelblue", outline="steelblue", width=2, tags=(etiqueta, "tarjeta"))
            self.canvas.create_text(x + 85, y + 40, text=texto, width=150, tags=(etiqueta, "tarjeta"))
        self.estado.set("Arrastra una tarjeta o haz doble clic para completarla")

    def iniciar_arrastre(self, evento):
        elementos = self.canvas.find_withtag("current")
        if not elementos:
            return
        etiquetas = self.canvas.gettags(elementos[0])
        etiqueta = next((valor for valor in etiquetas if valor.startswith("tarea-")), None)
        if etiqueta:
            self.arrastre = etiqueta, evento.x, evento.y
            self.canvas.tag_raise(etiqueta)
            self.estado.set(f"Moviendo {etiqueta}")

    def arrastrar(self, evento):
        if self.arrastre is None:
            return
        etiqueta, anterior_x, anterior_y = self.arrastre
        ancho = self.canvas.winfo_width()
        alto = self.canvas.winfo_height()
        x = limitar(evento.x, 10, ancho - 10)
        y = limitar(evento.y, 10, alto - 10)
        self.canvas.move(etiqueta, x - anterior_x, y - anterior_y)
        self.arrastre = etiqueta, x, y

    def finalizar_arrastre(self, evento):
        if self.arrastre is not None:
            self.estado.set(f"Ubicación final: {evento.x}, {evento.y}")
        self.arrastre = None

    def completar(self, evento):
        elementos = self.canvas.find_withtag("current")
        if elementos:
            etiquetas = self.canvas.gettags(elementos[0])
            etiqueta = next((valor for valor in etiquetas if valor.startswith("tarea-")), None)
            if etiqueta:
                for elemento in self.canvas.find_withtag(etiqueta):
                    if self.canvas.type(elemento) == "rectangle":
                        self.canvas.itemconfigure(elemento, fill="palegreen", outline="seagreen")
                self.estado.set(f"{etiqueta} completada")


def comprobar():
    assert limitar(5, 10, 100) == 10
    assert limitar(65, 10, 100) == 65
    assert limitar(120, 10, 100) == 100
    print("UNE9D24 OK")


if __name__ == "__main__":
    if "--check" in sys.argv:
        comprobar()
    else:
        TableroArrastrable().mainloop()
