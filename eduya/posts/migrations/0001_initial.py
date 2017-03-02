# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-02 22:43
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=50)),
                ('course', models.CharField(max_length=50)),
                ('location', models.CharField(max_length=50)),
                ('datetime', models.DateTimeField()),
                ('price', models.DecimalField(decimal_places=2, default=7.25, max_digits=5)),
                ('notes', models.TextField(max_length=250, null=True)),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]