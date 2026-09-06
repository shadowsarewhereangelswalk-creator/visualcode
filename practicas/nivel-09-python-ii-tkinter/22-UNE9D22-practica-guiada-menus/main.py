import tkinter as tk
from tkinter import messagebox

raiz = tk.Tk()
raiz.title("UNE9D22 — Menús y barras de opciones")
raiz.geometry("520x300")

estado = tk.StringVar(value="Usa el menú para ejecutar una acción")


def nuevo():
    estado.set("Nuevo registro preparado")


def guardar():
    estado.set("Registro guardado")


def acerca_de():
    messagebox.showinfo("Acerca de", "Práctica UNE9D22")


barra = tk.Menu(raiz)
archivo = tk.Menu(barra, tearoff=False)
archivo.add_command(label="Nuevo", command=nuevo)
archivo.add_command(label="Guardar", command=guardar)
archivo.add_separator()
archivo.add_command(label="Salir", command=raiz.destroy)
barra.add_cascade(label="Archivo", menu=archivo)
ayuda = tk.Menu(barra, tearoff=False)
ayuda.add_command(label="Acerca de", command=acerca_de)
barra.add_cascade(label="Ayuda", menu=ayuda)
raiz.config(menu=barra)

tk.Label(raiz, text="Ejercicio guiado de menús", font=("Arial", 18, "bold")).pack(pady=40)
tk.Label(raiz, textvariable=estado).pack()
raiz.mainloop()
