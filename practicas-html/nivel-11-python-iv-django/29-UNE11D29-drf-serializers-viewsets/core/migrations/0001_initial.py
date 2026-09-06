import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True
    dependencies = []
    operations = [
        migrations.CreateModel(name="Cliente", fields=[("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")), ("nombre", models.CharField(max_length=100)), ("correo", models.EmailField(max_length=254, unique=True))]),
        migrations.CreateModel(name="Proyecto", fields=[("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")), ("nombre", models.CharField(max_length=120)), ("estado", models.CharField(choices=[("nuevo", "Nuevo"), ("activo", "Activo"), ("cerrado", "Cerrado")], default="nuevo", max_length=20)), ("presupuesto", models.DecimalField(decimal_places=2, max_digits=10)), ("cliente", models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name="proyectos", to="core.cliente"))]),
    ]

