# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-20 12:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Actor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=40, verbose_name='First name')),
                ('last_name', models.CharField(max_length=40, verbose_name='Last name')),
            ],
        ),
        migrations.CreateModel(
            name='Director',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=40, verbose_name='First name')),
                ('last_name', models.CharField(max_length=40, verbose_name='Last name')),
            ],
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Title')),
            ],
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Title')),
                ('rating', models.PositiveIntegerField(choices=[(1, '\uf0e9'), (2, '\uf0e9\uf0e9'), (3, '\uf0e9\uf0e9\uf0e9'), (4, '\uf0e9\uf0e9\uf0e9\uf0e9'), (5, '\uf0e9\uf0e9\uf0e9\uf0e9\uf0e9')], default=5)),
                ('actors', models.ManyToManyField(blank=True, to='movies.Actor')),
                ('directors', models.ManyToManyField(blank=True, to='movies.Director')),
                ('genres', models.ManyToManyField(blank=True, to='movies.Genre')),
            ],
        ),
    ]
