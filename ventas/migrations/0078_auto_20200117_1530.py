# Generated by Django 2.2.6 on 2020-01-17 21:30

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('ventas', '0077_auto_20200117_1529'),
    ]

    operations = [
        migrations.AlterField(
            model_name='venta',
            name='fecha',
            field=models.DateTimeField(default=datetime.datetime(2020, 1, 17, 21, 30, 31, 716547, tzinfo=utc)),
        ),
    ]
