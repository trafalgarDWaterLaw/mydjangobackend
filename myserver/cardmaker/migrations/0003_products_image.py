# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-22 15:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cardmaker', '0002_auto_20170219_1605'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='image',
            field=models.ImageField(default='Images/None/No-img.jpg', upload_to='Images/'),
        ),
    ]