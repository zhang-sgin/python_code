# -*- coding: utf-8 -*-
# Generated by Django 1.11.18 on 2019-02-27 08:13
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0008_auto_20190227_1532'),
    ]

    operations = [
        migrations.CreateModel(
            name='User_Services',
            fields=[
                ('pid', models.AutoField(primary_key=True, serialize=False)),
            ],
        ),
        migrations.RemoveField(
            model_name='service',
            name='user_id',
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
        migrations.AddField(
            model_name='user_services',
            name='service_id',
            field=models.ManyToManyField(to='user.Service'),
        ),
        migrations.AddField(
            model_name='user_services',
            name='user_id',
            field=models.ManyToManyField(to='user.User'),
        ),
    ]
