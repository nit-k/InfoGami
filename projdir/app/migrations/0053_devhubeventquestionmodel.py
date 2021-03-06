# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-07-15 20:55
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_markdown.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app', '0052_devhubcreateeventmodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='DevhubEventQuestionModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_text', django_markdown.models.MarkdownField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.CodehubCreateEventModel')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('user_profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.UserProfileModel')),
            ],
        ),
    ]
