# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-19 19:09
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('course_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='course',
            old_name='description',
            new_name='desc',
        ),
    ]
