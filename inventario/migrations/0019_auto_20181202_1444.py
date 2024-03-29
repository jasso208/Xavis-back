# Generated by Django 2.1.2 on 2018-12-02 20:44

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventario', '0018_auto_20181202_1205'),
    ]

    operations = [
        migrations.AddField(
            model_name='detalle_venta',
            name='descuento',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=20),
        ),
        migrations.AddField(
            model_name='detalle_venta',
            name='iva',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=20),
        ),
        migrations.AlterField(
            model_name='venta',
            name='fecha',
            field=models.DateTimeField(default=datetime.datetime(2018, 12, 2, 14, 44, 0, 839168)),
        ),
    ]
