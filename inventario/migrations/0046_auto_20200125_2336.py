# Generated by Django 2.2.6 on 2020-01-26 05:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventario', '0045_auto_20200125_2328'),
    ]

    operations = [
        migrations.RenameField(
            model_name='productos',
            old_name='publicad_ml',
            new_name='publicado_ml',
        ),
    ]
