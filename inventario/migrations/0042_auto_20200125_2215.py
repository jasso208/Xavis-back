# Generated by Django 2.2.6 on 2020-01-26 04:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventario', '0041_auto_20200125_2214'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productos',
            name='publicado_ml',
            field=models.CharField(max_length=10),
        ),
    ]
