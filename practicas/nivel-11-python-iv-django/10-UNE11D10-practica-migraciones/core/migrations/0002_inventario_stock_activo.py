from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [("core", "0001_initial")]
    operations = [
        migrations.AddField(model_name="inventario", name="stock", field=models.PositiveIntegerField(default=0)),
        migrations.AddField(model_name="inventario", name="activo", field=models.BooleanField(default=True)),
    ]

