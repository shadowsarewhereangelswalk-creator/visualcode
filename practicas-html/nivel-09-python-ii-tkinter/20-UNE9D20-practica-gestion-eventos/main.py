import sys
import tkinter as tk
from datetime import datetime
from tkinter import ttk


def describir_evento(tipo, detalle):
    return f"{tipo}: {detalle}".strip()


class LaboratorioEventos(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("P3 — Gestión de eventos")
        self.geometry("820x560")
        self.minsize(660, 460)
        self.contador = 0
        self.estado = tk.StringVar(value="Interactúa con la interfaz")
        self.crear_interfaz()
        self.configurar_eventos()

    def crear_interfaz(self):
        principal = ttk.Frame(self, padding=18)
        principal.pack(fill="both", expand=True)
        ttk.Label(principal, text="Laboratorio de eventos", font=("TkDefaultFont", 19, "bold")).pack(anchor="w")

        controles = ttk.Frame(principal)
        controles.pack(fill="x", pady=14)
        self.entrada = ttk.Entry(controles)
        self.entrada.pack(side="left", fill="x", expand=True)
        self.boton = ttk.Button(controles, text="Registrar", command=lambda: self.registrar("command", self.entrada.get()))
        self.boton.pack(side="left", padx=(8, 0))

        self.zona = tk.Canvas(principal, background="white", height=180, cursor="crosshair")
        self.zona.pack(fill="x")
        self.zona.create_text(380, 90, text="Haz clic o mueve el mouse aquí", tags=("mensaje",))

        self.historial = tk.Listbox(principal)
        self.historial.pack(fill="both", expand=True, pady=(14, 8))
        ttk.Label(principal, textvariable=self.estado).pack(anchor="w")

    def configurar_eventos(self):
        self.bind("<Control-l>", lambda evento: self.limpiar())
        self.entrada.bind("<Return>", lambda evento: self.registrar("teclado", self.entrada.get()))
        self.entrada.bind("<FocusIn>", lambda evento: self.registrar("foco", "Entrada activada"))
        self.zona.bind("<Button-1>", lambda evento: self.registrar("clic", f"x={evento.x}, y={evento.y}"))
        self.zona.bind("<Motion>", self.mostrar_posicion)

    def mostrar_posicion(self, evento):
        self.estado.set(f"Posición del mouse: {evento.x}, {evento.y}")

    def registrar(self, tipo, detalle):
        detalle = detalle.strip()
        if not detalle:
            detalle = "Sin detalle"
        self.contador += 1
        hora = datetime.now().strftime("%H:%M:%S")
        self.historial.insert("end", f"{self.contador:02d} · {hora} · {describir_evento(tipo, detalle)}")
        self.historial.see("end")
        self.estado.set(f"Eventos registrados: {self.contador}")

    def limpiar(self):
        self.historial.delete(0, "end")
        self.contador = 0
        self.estado.set("Historial limpio")


def comprobar():
    assert describir_evento("clic", "x=20, y=40") == "clic: x=20, y=40"
    print("UNE9D20 OK")


if __name__ == "__main__":
    if "--check" in sys.argv:
        comprobar()
    else:
        LaboratorioEventos().mainloop()
