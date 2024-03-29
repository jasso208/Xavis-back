# Generated by Django 2.1.2 on 2019-03-05 04:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_blog', models.CharField(max_length=200)),
                ('contenido_blog', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Estatus_Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estatus', models.CharField(max_length=20)),
            ],
        ),
        migrations.AddField(
            model_name='blog',
            name='id_estatus',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='blog.Estatus_Blog'),
        ),
    ]
