from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True
    dependencies = []
    operations = [
        migrations.CreateModel(name="Venta", fields=[("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")), ("producto", models.CharField(max_length=100)), ("categoria", models.CharField(max_length=60)), ("total", models.DecimalField(decimal_places=2, max_digits=10)), ("fecha", models.DateField())]),
    ]

