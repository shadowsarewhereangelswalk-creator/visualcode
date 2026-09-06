from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True
    dependencies = []
    operations = [
        migrations.CreateModel(name="Oferta", fields=[("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")), ("cargo", models.CharField(max_length=100)), ("empresa", models.CharField(max_length=100)), ("modalidad", models.CharField(choices=[("remoto", "Remoto"), ("hibrido", "Híbrido"), ("presencial", "Presencial")], max_length=20)), ("salario", models.PositiveIntegerField()), ("activa", models.BooleanField(default=True))]),
    ]

