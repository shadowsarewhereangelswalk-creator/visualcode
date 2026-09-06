import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True
    dependencies = []
    operations = [
        migrations.CreateModel(name="Servicio", fields=[("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")), ("nombre", models.CharField(max_length=100)), ("slug", models.SlugField(unique=True)), ("descripcion", models.TextField()), ("precio_desde", models.DecimalField(decimal_places=2, max_digits=10)), ("activo", models.BooleanField(default=True))]),
        migrations.CreateModel(name="Solicitud", fields=[("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")), ("nombre", models.CharField(max_length=80)), ("correo", models.EmailField(max_length=254)), ("mensaje", models.TextField()), ("estado", models.CharField(choices=[("nueva", "Nueva"), ("contactada", "Contactada"), ("cerrada", "Cerrada")], default="nueva", max_length=20)), ("creada_en", models.DateTimeField(auto_now_add=True)), ("servicio", models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name="solicitudes", to="core.servicio"))]),
    ]

