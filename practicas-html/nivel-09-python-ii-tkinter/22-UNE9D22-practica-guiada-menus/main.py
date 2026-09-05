import sys
import tkinter as tk
from decimal import Decimal
from tkinter import messagebox, simpledialog, ttk


CATEGORIAS = ("Software", "Marketing", "Operaciones")


def totalizar(gastos):
    return sum((Decimal(str(gasto["monto"])) for gasto in gastos), Decimal("0"))


class GestorGastos(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Gestor de gastos con menús")
        self.geometry("760x500")
        self.minsize(620, 420)
        self.gastos = []
        self.filtro = tk.StringVar(value="Todas")
        self.estado = tk.StringVar(value="Sin gastos registrados")
        self.crear_menu()
        self.crear_interfaz()

    def crear_menu(self):
        self.barra = tk.Menu(self)
        archivo = tk.Menu(self.barra, tearoff=False)
        archivo.add_command(label="Nuevo gasto", command=self.nuevo_gasto, accelerator="Ctrl+G")
        archivo.add_command(label="Vaciar lista", command=self.vaciar)
        archivo.add_separator()
        archivo.add_command(label="Salir", command=self.destroy)
        self.barra.add_cascade(label="Archivo", menu=archivo)

        self.menu_filtro = tk.Menu(self.barra, tearoff=False)
        for categoria in ("Todas", *CATEGORIAS):
            self.menu_filtro.add_radiobutton(
                label=categoria,
                value=categoria,
                variable=self.filtro,
                command=self.actualizar_tabla,
            )
        self.barra.add_cascade(label="Filtrar", menu=self.menu_filtro)
        self.config(menu=self.barra)

    def crear_interfaz(self):
        panel = ttk.Frame(self, padding=16)
        panel.pack(fill="both", expand=True)
        ttk.Label(panel, text="Gastos del proyecto", font=("TkDefaultFont", 18, "bold")).pack(anchor="w")
        ttk.Button(panel, text="Agregar gasto", command=self.nuevo_gasto).pack(anchor="e", pady=(0, 10))

        self.tabla = ttk.Treeview(panel, columns=("concepto", "categoria", "monto"), show="headings")
        for columna, titulo, ancho in (
            ("concepto", "Concepto", 300),
            ("categoria", "Categoría", 180),
            ("monto", "Monto", 120),
        ):
            self.tabla.heading(columna, text=titulo)
            self.tabla.column(columna, width=ancho)
        self.tabla.pack(fill="both", expand=True)
        ttk.Label(panel, textvariable=self.estado).pack(anchor="w", pady=(10, 0))
        self.bind("<Control-g>", lambda evento: self.nuevo_gasto())

    def nuevo_gasto(self):
        concepto = simpledialog.askstring("Nuevo gasto", "Concepto", parent=self)
        if not concepto:
            return
        categoria = simpledialog.askstring(
            "Nuevo gasto",
            f'Categoría: {", ".join(CATEGORIAS)}',
            parent=self,
            initialvalue=CATEGORIAS[0],
        )
        if categoria not in CATEGORIAS:
            messagebox.showerror("Categoría", "La categoría no es válida", parent=self)
            return
        monto = simpledialog.askfloat("Nuevo gasto", "Monto", parent=self, minvalue=0.01)
        if monto is None:
            return
        self.gastos.append({"concepto": concepto.strip(), "categoria": categoria, "monto": monto})
        self.actualizar_tabla()

    def actualizar_tabla(self):
        self.tabla.delete(*self.tabla.get_children())
        visibles = [
            gasto for gasto in self.gastos
            if self.filtro.get() == "Todas" or gasto["categoria"] == self.filtro.get()
        ]
        for gasto in visibles:
            self.tabla.insert("", "end", values=(gasto["concepto"], gasto["categoria"], f'{gasto["monto"]:.2f}'))
        self.estado.set(f"Registros: {len(visibles)} · Total: {totalizar(visibles):.2f}")

    def vaciar(self):
        if messagebox.askyesno("Vaciar", "¿Eliminar todos los gastos?", parent=self):
            self.gastos.clear()
            self.actualizar_tabla()


def comprobar():
    gastos = [{"monto": 25.5}, {"monto": 40}]
    assert totalizar(gastos) == Decimal("65.5")
    print("UNE9D22 OK")


if __name__ == "__main__":
    if "--check" in sys.argv:
        comprobar()
    else:
        GestorGastos().mainloop()
