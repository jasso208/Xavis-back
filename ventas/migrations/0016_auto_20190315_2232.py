# Generated by Django 2.1.2 on 2019-03-16 04:32

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ventas', '0015_auto_20190309_1040'),
    ]

    operations = [
        migrations.AlterField(
            model_name='venta',
            name='fecha',
            field=models.DateTimeField(default=datetime.datetime(2019, 3, 15, 22, 32, 33, 896411)),
        ),
    ]
