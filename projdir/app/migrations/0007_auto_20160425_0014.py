# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-04-24 18:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_proposeeventmodel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='proposeeventmodel',
            name='downVotes',
            field=models.CharField(default=0, max_length=10),
        ),
        migrations.AlterField(
            model_name='proposeeventmodel',
            name='upVotes',
            field=models.CharField(default=0, max_length=10),
        ),
    ]
