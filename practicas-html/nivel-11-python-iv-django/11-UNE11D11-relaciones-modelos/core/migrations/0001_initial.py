import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True
    dependencies = []
    operations = [
        migrations.CreateModel(name="Autor", fields=[("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")), ("nombre", models.CharField(max_length=100))]),
        migrations.CreateModel(name="Categoria", fields=[("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")), ("nombre", models.CharField(max_length=60, unique=True))]),
        migrations.CreateModel(name="Perfil", fields=[("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")), ("biografia", models.TextField(blank=True)), ("autor", models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name="perfil", to="core.autor"))]),
        migrations.CreateModel(name="Articulo", fields=[("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")), ("titulo", models.CharField(max_length=150)), ("publicado", models.BooleanField(default=False)), ("autor", models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name="articulos", to="core.autor")), ("categorias", models.ManyToManyField(blank=True, related_name="articulos", to="core.categoria"))]),
    ]

