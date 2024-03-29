# Generated by Django 2.1.2 on 2019-03-01 02:56

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('inventario', '0034_auto_20190228_2056'),
        ('ventas', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Carrito_Compras',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('session', models.CharField(max_length=18)),
                ('cantidad', models.IntegerField()),
                ('id_producto', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='inventario.Productos')),
                ('talla', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='inventario.Tallas')),
            ],
        ),
        migrations.AlterField(
            model_name='venta',
            name='fecha',
            field=models.DateTimeField(default=datetime.datetime(2019, 2, 28, 20, 55, 59, 750034)),
        ),
    ]
