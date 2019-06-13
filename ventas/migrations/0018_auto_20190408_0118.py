# Generated by Django 2.1.2 on 2019-04-08 06:18

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('ventas', '0017_auto_20190406_0015'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='direccion_envio_venta',
            name='cliente',
        ),
        migrations.AddField(
            model_name='venta',
            name='cliente',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='venta',
            name='fecha',
            field=models.DateTimeField(default=datetime.datetime(2019, 4, 8, 1, 18, 11, 485864)),
        ),
    ]
