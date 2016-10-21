# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-23 11:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0007_auto_20161023_1149'),
    ]

    operations = [
        migrations.AlterField(
            model_name='board',
            name='color',
            field=models.CharField(choices=[('blue', 'blue'), ('green', 'green'), ('yellow', 'yellow'), ('red', 'red')], default='blue', max_length=7),
        ),
        migrations.AlterField(
            model_name='task',
            name='status',
            field=models.CharField(choices=[('todo', 'To do'), ('wip', 'Work in progress'), ('done', 'Done'), ('wish', 'Wish')], default='wish', max_length=20),
        ),
    ]
