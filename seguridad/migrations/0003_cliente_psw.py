# Generated by Django 2.1.2 on 2019-04-14 06:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('seguridad', '0002_auto_20190412_0825'),
    ]

    operations = [
        migrations.AddField(
            model_name='cliente',
            name='psw',
            field=models.CharField(default='', max_length=10),
            preserve_default=False,
        ),
    ]
