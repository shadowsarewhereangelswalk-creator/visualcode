from decimal import Decimal

from django.core.management.base import BaseCommand

from core.models import Cliente, Pedido


class Command(BaseCommand):
    def handle(self, *args, **options):
        cliente, _ = Cliente.objects.update_or_create(correo="ada@example.com", defaults={"nombre": "Ada Lovelace"})
        Pedido.objects.get_or_create(cliente=cliente, total=Decimal("320.00"), estado="nuevo")
        Pedido.objects.filter(cliente=cliente, estado="nuevo").update(estado="procesando")
        self.stdout.write(self.style.SUCCESS(f"{cliente.nombre}: {cliente.pedidos.count()} pedido"))

