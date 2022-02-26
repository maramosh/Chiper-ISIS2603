# Generated by Django 2.2 on 2020-03-25 23:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('bodega', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Zona',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipoProducto', models.CharField(max_length=60)),
                ('especialidad', models.CharField(max_length=60)),
                ('capacidad', models.IntegerField()),
                ('bodega', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bodega.Bodega')),
            ],
        ),
    ]
