import tkinter as tk

raiz = tk.Tk()
raiz.title("UNE9D23 — Eventos y bindings")
raiz.geometry("560x340")

mensaje = tk.StringVar(value="Interactúa con el área")
area = tk.Frame(raiz, width=420, height=180, bg="white", highlightthickness=1, highlightbackground="#999")
area.pack(pady=35)
area.pack_propagate(False)
tk.Label(area, textvariable=mensaje, bg="white").place(relx=0.5, rely=0.5, anchor="center")


def informar(texto):
    mensaje.set(texto)


area.bind("<Button-1>", lambda evento: informar(f"Clic en {evento.x}, {evento.y}"))
area.bind("<Enter>", lambda evento: informar("Puntero dentro del área"))
area.bind("<Leave>", lambda evento: informar("Puntero fuera del área"))
raiz.bind("<Key>", lambda evento: informar(f"Tecla: {evento.keysym}"))
area.focus_set()
raiz.mainloop()
