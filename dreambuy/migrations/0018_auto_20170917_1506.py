# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-09-17 09:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dreambuy', '0017_auto_20170907_1916'),
    ]

    operations = [
        migrations.AddField(
            model_name='userbids',
            name='cur_prdt_bid_price',
            field=models.IntegerField(default=500),
        ),
        migrations.AddField(
            model_name='userbids',
            name='pymnt_status',
            field=models.CharField(default=1, max_length=10),
        ),
    ]
