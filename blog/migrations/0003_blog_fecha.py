# Generated by Django 2.1.2 on 2019-03-05 04:42

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_blog_imagen_blog'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='fecha',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]
