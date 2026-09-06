import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True
    dependencies = []
    operations = [
        migrations.CreateModel(name="Cliente", fields=[("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")), ("nombre", models.CharField(max_length=100)), ("correo", models.EmailField(max_length=254, unique=True))]),
        migrations.CreateModel(name="Pedido", fields=[("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")), ("total", models.DecimalField(decimal_places=2, max_digits=10)), ("estado", models.CharField(default="nuevo", max_length=20)), ("cliente", models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name="pedidos", to="core.cliente"))]),
    ]

