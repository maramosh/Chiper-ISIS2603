# Generated by Django 2.2 on 2020-03-22 00:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Factura',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('valor', models.FloatField()),
                ('fecha', models.DateField()),
                ('codigo', models.IntegerField()),
                ('direccion', models.CharField(max_length=50)),
                ('nombreEmisor', models.CharField(max_length=60)),
            ],
        ),
    ]
