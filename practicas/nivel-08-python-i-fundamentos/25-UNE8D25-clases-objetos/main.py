class Cliente:
    def __init__(self, codigo, nombre, correo):
        self.codigo = codigo.upper()
        self.nombre = nombre.strip().title()
        self.correo = correo.strip().lower()
        self.servicios = []

    def contratar(self, servicio):
        if servicio not in self.servicios:
            self.servicios.append(servicio)

    def resumen(self):
        servicios = ", ".join(self.servicios) or "Sin servicios"
        return f"{self.codigo} · {self.nombre} · {self.correo} · {servicios}"


class CRM:
    def __init__(self):
        self.clientes = {}

    def registrar(self, cliente):
        if cliente.codigo in self.clientes:
            raise ValueError("El código ya está registrado")
        self.clientes[cliente.codigo] = cliente

    def buscar(self, codigo):
        cliente = self.clientes.get(codigo.upper())
        if cliente is None:
            raise LookupError("Cliente no encontrado")
        return cliente

    def contratar(self, codigo, servicio):
        self.buscar(codigo).contratar(servicio)

    def listar(self):
        return sorted(self.clientes.values(), key=lambda cliente: cliente.nombre)


def main():
    crm = CRM()
    crm.registrar(Cliente("cli-002", "Luis Pérez", "LUIS@EJEMPLO.COM"))
    crm.registrar(Cliente("cli-001", "Ana Torres", "ana@ejemplo.com"))
    crm.contratar("cli-001", "Landing page")
    crm.contratar("cli-001", "Automatización")
    crm.contratar("cli-002", "Asistente virtual")

    for cliente in crm.listar():
        print(cliente.resumen())


if __name__ == "__main__":
    main()
