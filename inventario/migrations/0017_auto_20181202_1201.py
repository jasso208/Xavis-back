# Generated by Django 2.1.2 on 2018-12-02 18:01

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventario', '0016_auto_20181202_1014'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='venta',
            name='descuento',
        ),
        migrations.AlterField(
            model_name='venta',
            name='fecha',
            field=models.DateTimeField(default=datetime.datetime(2018, 12, 2, 12, 1, 54, 969629)),
        ),
    ]
