# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2015-12-26 21:34
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='T_Tag',
            fields=[
                ('TagID', models.AutoField(default=1, primary_key=True, serialize=False)),
                ('Tag', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='T_URL',
            fields=[
                ('URLID', models.AutoField(default=1, primary_key=True, serialize=False)),
                ('URL', models.CharField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='T_URL_Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('TAGID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bookmark.T_Tag')),
                ('URLID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bookmark.T_URL')),
            ],
        ),
    ]