# Generated by Django 2.1.2 on 2019-05-26 04:31

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ventas', '0022_auto_20190525_2329'),
    ]

    operations = [
        migrations.AlterField(
            model_name='venta',
            name='fecha',
            field=models.DateTimeField(default=datetime.datetime(2019, 5, 25, 23, 31, 4, 292215)),
        ),
    ]
