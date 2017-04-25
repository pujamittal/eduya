# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-25 03:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0002_coursecomment_professorcomment'),
    ]

    operations = [
        migrations.CreateModel(
            name='FileLinker',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('typeOfInfo', models.CharField(max_length=20)),
                ('infoLink', models.TextField()),
                ('description', models.TextField(blank=True, max_length=250, null=True)),
            ],
        ),
    ]
