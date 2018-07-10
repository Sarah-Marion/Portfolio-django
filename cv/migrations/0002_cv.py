# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-07-09 18:22
from __future__ import unicode_literals

from django.db import migrations, models
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('cv', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cv',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cv_body', tinymce.models.HTMLField()),
                ('cv_name', models.CharField(max_length=250)),
            ],
        ),
    ]
