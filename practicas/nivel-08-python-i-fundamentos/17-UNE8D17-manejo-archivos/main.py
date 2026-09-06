from pathlib import Path
from tempfile import TemporaryDirectory


def guardar_clientes(ruta, clientes):
    lineas = [
        "|".join((cliente["codigo"], cliente["nombre"], cliente["correo"]))
        for cliente in clientes
    ]
    ruta.write_text("\n".join(lineas) + "\n", encoding="utf-8")


def leer_clientes(ruta):
    clientes = []
    for linea in ruta.read_text(encoding="utf-8").splitlines():
        codigo, nombre, correo = linea.split("|")
        clientes.append({"codigo": codigo, "nombre": nombre, "correo": correo})
    return clientes


def guardar_reporte(ruta, clientes):
    encabezado = "CÓDIGO,NOMBRE,CORREO"
    filas = [
        f'{cliente["codigo"]},{cliente["nombre"]},{cliente["correo"]}'
        for cliente in clientes
    ]
    ruta.write_text("\n".join([encabezado, *filas]) + "\n", encoding="utf-8")


def main():
    clientes = [
        {"codigo": "CLI-001", "nombre": "Ana Torres", "correo": "ana@ejemplo.com"},
        {"codigo": "CLI-002", "nombre": "Luis Pérez", "correo": "luis@ejemplo.com"},
        {"codigo": "CLI-003", "nombre": "Marta Díaz", "correo": "marta@ejemplo.com"},
    ]

    with TemporaryDirectory() as carpeta:
        carpeta = Path(carpeta)
        archivo_clientes = carpeta / "clientes.txt"
        archivo_reporte = carpeta / "reporte.csv"
        guardar_clientes(archivo_clientes, clientes)
        recuperados = leer_clientes(archivo_clientes)
        guardar_reporte(archivo_reporte, recuperados)

        print(archivo_clientes.read_text(encoding="utf-8").strip())
        print(archivo_reporte.read_text(encoding="utf-8").strip())


if __name__ == "__main__":
    main()
