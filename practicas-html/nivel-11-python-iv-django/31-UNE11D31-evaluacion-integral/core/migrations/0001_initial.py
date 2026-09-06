from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True
    dependencies = []
    operations = [
        migrations.CreateModel(name="Incidencia", fields=[("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")), ("titulo", models.CharField(max_length=120)), ("prioridad", models.CharField(choices=[("baja", "Baja"), ("media", "Media"), ("alta", "Alta")], default="media", max_length=10)), ("resuelta", models.BooleanField(default=False))]),
    ]

