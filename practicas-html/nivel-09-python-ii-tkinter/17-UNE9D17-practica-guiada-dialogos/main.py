import csv
import io
import sys
import tkinter as tk
from pathlib import Path
from tkinter import filedialog, messagebox, ttk


COLUMNAS = ("codigo", "nombre", "correo")


def leer_csv(contenido):
    lector = csv.DictReader(io.StringIO(contenido))
    if tuple(lector.fieldnames or ()) != COLUMNAS:
        raise ValueError("El CSV debe contener codigo,nombre,correo")
    return [
        (
            fila["codigo"].strip().upper(),
            " ".join(fila["nombre"].split()).title(),
            fila["correo"].strip().lower(),
        )
        for fila in lector
        if any(fila.values())
    ]


def crear_csv(registros):
    salida = io.StringIO()
    escritor = csv.writer(salida, lineterminator="\n")
    escritor.writerow(COLUMNAS)
    escritor.writerows(registros)
    return salida.getvalue()


class ImportadorContactos(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Importar y exportar contactos")
        self.geometry("780x500")
        self.minsize(620, 400)
        self.estado = tk.StringVar(value="Carga un archivo CSV")
        self.crear_interfaz()

    def crear_interfaz(self):
        barra = ttk.Frame(self, padding=14)
        barra.pack(fill="x")
        ttk.Button(barra, text="Importar CSV", command=self.importar).pack(side="left")
        ttk.Button(barra, text="Exportar CSV", command=self.exportar).pack(side="left", padx=8)
        ttk.Button(barra, text="Eliminar selección", command=self.eliminar).pack(side="left")
        ttk.Label(barra, textvariable=self.estado).pack(side="right")

        self.tabla = ttk.Treeview(self, columns=COLUMNAS, show="headings")
        for columna, titulo, ancho in (
            ("codigo", "Código", 120),
            ("nombre", "Nombre", 220),
            ("correo", "Correo", 280),
        ):
            self.tabla.heading(columna, text=titulo)
            self.tabla.column(columna, width=ancho)
        self.tabla.pack(fill="both", expand=True, padx=14, pady=(0, 14))

    def importar(self):
        ruta = filedialog.askopenfilename(
            parent=self,
            filetypes=(("CSV", "*.csv"),),
        )
        if not ruta:
            return
        try:
            registros = leer_csv(Path(ruta).read_text(encoding="utf-8-sig"))
        except (OSError, UnicodeDecodeError, ValueError) as error:
            messagebox.showerror("Importación", str(error), parent=self)
            return
        self.tabla.delete(*self.tabla.get_children())
        for registro in registros:
            self.tabla.insert("", "end", values=registro)
        self.estado.set(f"Importados: {len(registros)}")

    def exportar(self):
        registros = [self.tabla.item(item, "values") for item in self.tabla.get_children()]
        if not registros:
            messagebox.showwarning("Exportación", "No hay contactos para exportar", parent=self)
            return
        ruta = filedialog.asksaveasfilename(
            parent=self,
            defaultextension=".csv",
            filetypes=(("CSV", "*.csv"),),
        )
        if ruta:
            Path(ruta).write_text(crear_csv(registros), encoding="utf-8")
            self.estado.set(f"Exportados: {len(registros)}")

    def eliminar(self):
        seleccion = self.tabla.selection()
        for item in seleccion:
            self.tabla.delete(item)
        self.estado.set(f"Eliminados: {len(seleccion)}")


def comprobar():
    contenido = "codigo,nombre,correo\ncli-001,ana torres,ANA@EJEMPLO.COM\n"
    registros = leer_csv(contenido)
    assert registros == [("CLI-001", "Ana Torres", "ana@ejemplo.com")]
    assert crear_csv(registros).startswith("codigo,nombre,correo\n")
    print("UNE9D17 OK")


if __name__ == "__main__":
    if "--check" in sys.argv:
        comprobar()
    else:
        ImportadorContactos().mainloop()
