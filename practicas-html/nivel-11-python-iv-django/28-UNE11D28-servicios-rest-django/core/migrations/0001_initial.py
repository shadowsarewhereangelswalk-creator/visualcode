from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True
    dependencies = []
    operations = [
        migrations.CreateModel(name="Nota", fields=[("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")), ("titulo", models.CharField(max_length=120)), ("contenido", models.TextField()), ("creada_en", models.DateTimeField(auto_now_add=True))]),
    ]

