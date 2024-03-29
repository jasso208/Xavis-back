# Generated by Django 2.1.2 on 2018-12-02 01:52

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('inventario', '0013_categorias_rel_producto_categoria'),
    ]

    operations = [
        migrations.CreateModel(
            name='Detalle_Venta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('precio', models.DecimalField(decimal_places=2, max_digits=20)),
                ('id_producto', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='inventario.Productos')),
            ],
        ),
        migrations.CreateModel(
            name='Direccion_Envio_Venta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_recibe', models.CharField(max_length=20)),
                ('apellido_p', models.CharField(max_length=20)),
                ('apellido_m', models.CharField(max_length=20)),
                ('calle', models.CharField(max_length=50)),
                ('numero', models.CharField(max_length=10)),
                ('cp', models.CharField(max_length=10)),
                ('municipio', models.CharField(default='', max_length=50)),
                ('estado', models.CharField(default='', max_length=50)),
                ('pais', models.CharField(default='', max_length=50)),
                ('telefono', models.CharField(max_length=20)),
                ('correo_electronico', models.CharField(max_length=50)),
                ('referencia', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Venta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateTimeField(default=datetime.datetime(2018, 12, 1, 19, 52, 28, 469743))),
                ('sub_total', models.DecimalField(decimal_places=2, max_digits=20)),
                ('descuento', models.DecimalField(decimal_places=2, max_digits=20)),
                ('iva', models.DecimalField(decimal_places=2, max_digits=20)),
                ('total', models.DecimalField(decimal_places=2, max_digits=20)),
            ],
        ),
        migrations.AddField(
            model_name='direccion_envio_venta',
            name='id_venta',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='inventario.Venta'),
        ),
        migrations.AddField(
            model_name='detalle_venta',
            name='id_venta',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='inventario.Venta'),
        ),
    ]
