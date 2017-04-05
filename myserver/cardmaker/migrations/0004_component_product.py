# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cardmaker', '0003_products_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='component',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('product_id', models.CharField(default='', max_length=100)),
                ('width', models.CharField(default='', max_length=100)),
                ('height', models.CharField(default='', max_length=100)),
                ('position', models.CharField(default='', max_length=100)),
                ('component_id', models.CharField(default='', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='product',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('product_id', models.CharField(default='', max_length=100)),
                ('width', models.CharField(default='', max_length=100)),
                ('height', models.CharField(default='', max_length=100)),
            ],
        ),
    ]
