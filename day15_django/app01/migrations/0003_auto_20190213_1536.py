# -*- coding: utf-8 -*-
# Generated by Django 1.11.18 on 2019-02-13 07:36
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0002_publisher'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Publisher',
            new_name='Systemuser',
        ),
    ]