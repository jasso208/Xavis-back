# Generated by Django 2.1.2 on 2019-04-14 06:20

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ventas', '0020_auto_20190414_0102'),
    ]

    operations = [
        migrations.AlterField(
            model_name='venta',
            name='fecha',
            field=models.DateTimeField(default=datetime.datetime(2019, 4, 14, 1, 20, 47, 177316)),
        ),
    ]
