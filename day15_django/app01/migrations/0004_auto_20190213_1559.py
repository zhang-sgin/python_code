# -*- coding: utf-8 -*-
# Generated by Django 1.11.18 on 2019-02-13 07:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0003_auto_20190213_1536'),
    ]

    operations = [
        migrations.CreateModel(
            name='test',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('t1', models.CharField(max_length=32)),
                ('pwd', models.CharField(max_length=32)),
            ],
        ),
        migrations.AddField(
            model_name='systemuser',
            name='password',
            field=models.CharField(default='', max_length=32),
        ),
    ]