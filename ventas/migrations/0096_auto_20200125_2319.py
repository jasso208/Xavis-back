# Generated by Django 2.2.6 on 2020-01-26 05:19

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('ventas', '0095_auto_20200125_2309'),
    ]

    operations = [
        migrations.AlterField(
            model_name='venta',
            name='fecha',
            field=models.DateTimeField(default=datetime.datetime(2020, 1, 26, 5, 19, 12, 911886, tzinfo=utc)),
        ),
    ]
