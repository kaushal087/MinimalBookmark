# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-04 07:23
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bookmark', '0002_auto_20151227_0713'),
    ]

    operations = [
        migrations.AlterField(
            model_name='t_url_tag',
            name='TAGID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bookmark.t_tag'),
        ),
        migrations.AlterField(
            model_name='t_url_tag',
            name='URLID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bookmark.t_url'),
        ),
    ]
