# Generated by Django 2.0.8 on 2018-08-20 03:33

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='nombre')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creacion')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Fecha de actualizacion')),
            ],
            options={
                'verbose_name': 'Categoria',
                'verbose_name_plural': 'categorias',
                'ordering': ['-created'],
            },
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='titulo')),
                ('content', models.TextField(verbose_name='contenido')),
                ('published', models.DateTimeField(default=datetime.datetime(2018, 8, 20, 3, 33, 30, 332212, tzinfo=utc), verbose_name='Fecha de actualizacion')),
                ('image', models.ImageField(blank=True, null=True, upload_to='blog', verbose_name='imagen')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creacion')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Fecha de actualizacion')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='autor')),
                ('categories', models.ManyToManyField(to='blog.Category', verbose_name='categorias')),
            ],
            options={
                'verbose_name': 'entrada',
                'verbose_name_plural': 'entradas',
                'ordering': ['-created'],
            },
        ),
    ]
