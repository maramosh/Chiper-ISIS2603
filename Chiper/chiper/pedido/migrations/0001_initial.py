# Generated by Django 2.2 on 2020-03-25 23:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('facturabodega', '0001_initial'),
        ('camion', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pedido',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipoPago', models.CharField(max_length=60)),
                ('valor', models.FloatField()),
                ('cantidadProducto', models.IntegerField()),
                ('Factura', models.ManyToManyField(to='facturabodega.FacturaBodega')),
                ('camion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='camion.Camion')),
            ],
        ),
    ]
