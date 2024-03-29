# Generated by Django 2.2.6 on 2020-01-15 20:10

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('ventas', '0056_auto_20200115_0331'),
    ]

    operations = [
        migrations.AlterField(
            model_name='detalle_venta',
            name='id_venta',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='ventas.Venta'),
        ),
        migrations.AlterField(
            model_name='venta',
            name='fecha',
            field=models.DateTimeField(default=datetime.datetime(2020, 1, 15, 20, 10, 48, 504227, tzinfo=utc)),
        ),
    ]
