# Generated by Django 2.1.2 on 2019-06-24 02:37

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ventas', '0032_auto_20190619_2352'),
    ]

    operations = [
        migrations.AlterField(
            model_name='venta',
            name='fecha',
            field=models.DateTimeField(default=datetime.datetime(2019, 6, 23, 21, 37, 35, 355546)),
        ),
    ]
