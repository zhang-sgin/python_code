# -*- coding: utf-8 -*-
# Generated by Django 1.11.18 on 2019-02-27 08:23
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0017_auto_20190227_1623'),
    ]

    operations = [
        migrations.CreateModel(
            name='User_Services',
            fields=[
                ('pid', models.AutoField(primary_key=True, serialize=False)),
                ('service_id', models.ManyToManyField(to='user.Service')),
                ('user_id', models.ManyToManyField(to='user.User')),
            ],
            options={
                'db_table': 'User_Services',
            },
        ),
        migrations.AlterField(
            model_name='host',
            name='service',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.Service'),
        ),
    ]
