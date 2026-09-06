from django.core.management.base import BaseCommand

from core.models import Curso


class Command(BaseCommand):
    def handle(self, *args, **options):
        Curso.objects.update_or_create(nombre="Django", defaults={"nivel": "Intermedio", "activo": True})
        Curso.objects.update_or_create(nombre="Python", defaults={"nivel": "Inicial", "activo": True})
        activos = Curso.objects.filter(activo=True).order_by("nombre")
        for curso in activos:
            self.stdout.write(f"{curso.pk}: {curso.nombre} · {curso.nivel}")
        self.stdout.write(self.style.SUCCESS(f"Total: {activos.count()}"))

