# Generated by Django 2.1.2 on 2018-12-02 02:14

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('inventario', '0014_auto_20181201_1952'),
    ]

    operations = [
        migrations.RenameField(
            model_name='detalle_venta',
            old_name='precio',
            new_name='precio_total',
        ),
        migrations.AddField(
            model_name='detalle_venta',
            name='cantidad',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='detalle_venta',
            name='precio_unitario',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='detalle_venta',
            name='talla',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.PROTECT, to='inventario.Tallas'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='venta',
            name='fecha',
            field=models.DateTimeField(default=datetime.datetime(2018, 12, 1, 20, 11, 26, 626842)),
        ),
    ]
