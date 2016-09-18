# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-17 10:06
from __future__ import unicode_literals

from django.db import migrations, models
import photos.models


class Migration(migrations.Migration):

    dependencies = [
        ('photos', '0003_auto_20160915_0025'),
    ]

    operations = [
        migrations.AddField(
            model_name='photo',
            name='edited_image',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='photo',
            name='image',
            field=models.ImageField(null=True, upload_to=photos.models.get_upload_file_name),
        ),
    ]
