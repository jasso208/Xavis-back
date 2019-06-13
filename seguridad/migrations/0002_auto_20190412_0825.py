# Generated by Django 2.1.2 on 2019-04-12 13:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('seguridad', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='direccion_envio_cliente',
            old_name='numero',
            new_name='numero_exterior',
        ),
        migrations.AddField(
            model_name='direccion_envio_cliente',
            name='numero_interior',
            field=models.CharField(default='', max_length=10),
            preserve_default=False,
        ),
    ]
