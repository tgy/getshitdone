# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-20 21:49
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='board',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='todo.Board'),
        ),
    ]
