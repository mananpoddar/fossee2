# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-03-13 15:13
from __future__ import unicode_literals

from django.db import migrations, models
import fossee2.validators


class Migration(migrations.Migration):

    dependencies = [
        ('fossee2', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='documents',
            name='document',
            field=models.FileField(upload_to='document/', validators=[fossee2.validators.validate_file_extension]),
        ),
    ]
