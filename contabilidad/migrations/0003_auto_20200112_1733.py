# Generated by Django 2.2.6 on 2020-01-12 23:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contabilidad', '0002_auto_20200112_1719'),
    ]

    operations = [
        migrations.RenameField(
            model_name='movs_gasto',
            old_name='id_venta',
            new_name='id_v',
        ),
        migrations.RenameField(
            model_name='movs_ingreso',
            old_name='id_venta',
            new_name='id_v',
        ),
    ]
