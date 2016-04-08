# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-04-06 16:15
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_markdown.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app', '0007_auto_20160406_2142'),
    ]

    operations = [
        migrations.CreateModel(
            name='CodehubQuestionModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_heading', models.CharField(max_length=200)),
                ('question_description', django_markdown.models.MarkdownField()),
                ('question_link', models.CharField(blank=True, max_length=100)),
                ('question_tags', models.CharField(max_length=200)),
                ('timeStamp', models.DateTimeField(auto_now_add=True)),
                ('question_type', models.CharField(max_length=20)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]