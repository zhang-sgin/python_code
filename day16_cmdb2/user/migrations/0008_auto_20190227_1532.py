# -*- coding: utf-8 -*-
# Generated by Django 1.11.18 on 2019-02-27 07:32
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0007_auto_20190227_1029'),
    ]

    operations = [
        migrations.AddField(
            model_name='service',
            name='user_id',
            field=models.ManyToManyField(to='user.User'),
        ),
        migrations.AlterField(
            model_name='host',
            name='service',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.Service'),
        ),
        migrations.AlterField(
            model_name='test',
            name='spid',
            field=models.ManyToManyField(to='user.Service'),
        ),
    ]
