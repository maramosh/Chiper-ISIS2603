# Generated by Django 2.2 on 2020-03-21 23:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0003_remove_producto_ventas'),
        ('venta', '0002_auto_20200321_1840'),
    ]

    operations = [
        migrations.AddField(
            model_name='venta',
            name='productos',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='productos.Producto'),
        ),
    ]
