# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-06-29 17:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0037_theinfoqueryanswermodel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='theinfoqueryanswermodel',
            name='answer_vote',
            field=models.IntegerField(default=0),
        ),
    ]