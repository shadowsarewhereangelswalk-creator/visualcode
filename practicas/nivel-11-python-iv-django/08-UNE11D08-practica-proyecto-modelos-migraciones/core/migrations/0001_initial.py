import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True
    dependencies = []
    operations = [
        migrations.CreateModel(name="Autor", fields=[("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")), ("nombre", models.CharField(max_length=100)), ("pais", models.CharField(max_length=80))]),
        migrations.CreateModel(name="Libro", fields=[("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")), ("titulo", models.CharField(max_length=150)), ("publicado", models.PositiveIntegerField()), ("disponible", models.BooleanField(default=True)), ("autor", models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name="libros", to="core.autor"))]),
    ]

