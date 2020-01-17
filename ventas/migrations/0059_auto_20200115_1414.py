# Generated by Django 2.2.6 on 2020-01-15 20:14

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('ventas', '0058_auto_20200115_1413'),
    ]

    operations = [
        migrations.AlterField(
            model_name='venta',
            name='fecha',
            field=models.DateTimeField(default=datetime.datetime(2020, 1, 15, 20, 14, 5, 182663, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='venta',
            name='id_medio_venta',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='ventas.Medio_Venta'),
        ),
    ]
