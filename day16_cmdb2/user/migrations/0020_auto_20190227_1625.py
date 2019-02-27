# -*- coding: utf-8 -*-
# Generated by Django 1.11.18 on 2019-02-27 08:25
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0019_auto_20190227_1624'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user_services',
            name='service_id',
        ),
        migrations.RemoveField(
            model_name='user_services',
            name='user_id',
        ),
        migrations.AlterField(
            model_name='host',
            name='service',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.Service'),
        ),
        migrations.DeleteModel(
            name='User_Services',
        ),
    ]
