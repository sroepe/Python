# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-15 00:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dojoninja_first', '0003_ninja_dojo'),
    ]

    operations = [
        migrations.AddField(
            model_name='dojo',
            name='desc',
            field=models.TextField(null=True),
        ),
    ]
