# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-08-06 18:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dreambuy', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='Product_bids',
            field=models.IntegerField(),
        ),
    ]