from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True
    dependencies = []
    operations = [
        migrations.CreateModel(name="Reserva", fields=[("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")), ("nombre", models.CharField(max_length=80)), ("correo", models.EmailField(max_length=254)), ("servicio", models.CharField(choices=[("mentoria", "Mentoría"), ("portafolio", "Portafolio"), ("entrevista", "Entrevista")], max_length=30)), ("fecha", models.DateField()), ("mensaje", models.TextField(blank=True)), ("creada_en", models.DateTimeField(auto_now_add=True))]),
    ]

