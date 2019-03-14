# -*- coding: utf-8 -*-
# Generated by Django 1.11.18 on 2019-03-13 07:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Depart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32, verbose_name='部门名称')),
                ('desc', models.TextField(blank=True, null=True, verbose_name='职责')),
            ],
        ),
    ]
