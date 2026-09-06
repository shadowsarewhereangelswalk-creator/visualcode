import argparse
import json
import re
from dataclasses import asdict, dataclass
from decimal import Decimal, ROUND_HALF_UP
from pathlib import Path


@dataclass
class Cliente:
    codigo: str
    nombre: str
    correo: str


class RepositorioClientes:
    def __init__(self, ruta):
        self.ruta = Path(ruta)
        self.clientes = self.cargar()

    def cargar(self):
        if not self.ruta.exists():
            return []
        datos = json.loads(self.ruta.read_text(encoding="utf-8"))
        return [Cliente(**registro) for registro in datos]

    def guardar(self):
        self.ruta.parent.mkdir(parents=True, exist_ok=True)
        contenido = [asdict(cliente) for cliente in self.clientes]
        self.ruta.write_text(
            json.dumps(contenido, ensure_ascii=False, indent=2) + "\n",
            encoding="utf-8",
        )

    def buscar(self, codigo):
        codigo = codigo.upper()
        return next((cliente for cliente in self.clientes if cliente.codigo == codigo), None)

    def agregar(self, cliente):
        if self.buscar(cliente.codigo):
            raise ValueError("El código ya existe")
        if not re.fullmatch(r"[^@\s]+@[^@\s]+\.[A-Za-z]{2,}", cliente.correo):
            raise ValueError("El correo no es válido")
        cliente.codigo = cliente.codigo.upper()
        cliente.nombre = " ".join(cliente.nombre.split()).title()
        cliente.correo = cliente.correo.lower()
        self.clientes.append(cliente)
        self.guardar()

    def listar(self):
        return sorted(self.clientes, key=lambda cliente: cliente.nombre)


def calcular_cotizacion(cliente, servicio, precio, cantidad=1, impuesto=0.16):
    precio = Decimal(str(precio))
    cantidad = Decimal(str(cantidad))
    impuesto = Decimal(str(impuesto))
    if precio <= 0 or cantidad <= 0:
        raise ValueError("El precio y la cantidad deben ser positivos")
    subtotal = precio * cantidad
    total = subtotal * (Decimal("1") + impuesto)
    moneda = Decimal("0.01")
    return {
        "cliente": cliente.nombre,
        "servicio": servicio.strip().title(),
        "subtotal": subtotal.quantize(moneda, rounding=ROUND_HALF_UP),
        "total": total.quantize(moneda, rounding=ROUND_HALF_UP),
    }


def crear_parser():
    parser = argparse.ArgumentParser(prog="clientes", description="Sistema de clientes y cotizaciones")
    parser.add_argument(
        "--archivo",
        type=Path,
        default=Path(__file__).with_name("clientes.json"),
    )
    comandos = parser.add_subparsers(dest="comando")

    agregar = comandos.add_parser("agregar")
    agregar.add_argument("codigo")
    agregar.add_argument("nombre")
    agregar.add_argument("correo")

    comandos.add_parser("listar")

    cotizar = comandos.add_parser("cotizar")
    cotizar.add_argument("codigo")
    cotizar.add_argument("servicio")
    cotizar.add_argument("precio", type=Decimal)
    cotizar.add_argument("--cantidad", type=int, default=1)

    comandos.add_parser("demo")
    return parser


def mostrar_clientes(repositorio):
    for cliente in repositorio.listar():
        print(f"{cliente.codigo} · {cliente.nombre} · {cliente.correo}")


def ejecutar(args):
    repositorio = RepositorioClientes(args.archivo)

    if args.comando == "agregar":
        repositorio.agregar(Cliente(args.codigo, args.nombre, args.correo))
        print("Cliente guardado")
        return

    if args.comando == "listar":
        mostrar_clientes(repositorio)
        return

    if args.comando == "cotizar":
        cliente = repositorio.buscar(args.codigo)
        if cliente is None:
            raise LookupError("Cliente no encontrado")
        cotizacion = calcular_cotizacion(
            cliente,
            args.servicio,
            args.precio,
            args.cantidad,
        )
        print(f'Cliente: {cotizacion["cliente"]}')
        print(f'Servicio: {cotizacion["servicio"]}')
        print(f'Subtotal: {cotizacion["subtotal"]:.2f}')
        print(f'Total: {cotizacion["total"]:.2f}')
        return

    ejemplos = [
        Cliente("CLI-001", "Ana Torres", "ana@ejemplo.com"),
        Cliente("CLI-002", "Luis Pérez", "luis@ejemplo.com"),
    ]
    for cliente in ejemplos:
        if repositorio.buscar(cliente.codigo) is None:
            repositorio.agregar(cliente)
    mostrar_clientes(repositorio)
    cotizacion = calcular_cotizacion(repositorio.buscar("CLI-001"), "Automatización", 640, 2)
    print(f'Cotización: {cotizacion["servicio"]} · total {cotizacion["total"]:.2f}')


def main():
    parser = crear_parser()
    try:
        ejecutar(parser.parse_args())
    except (ValueError, LookupError, json.JSONDecodeError) as error:
        parser.error(str(error))


if __name__ == "__main__":
    main()
