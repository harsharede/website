# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-08-06 18:49
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Product_name', models.CharField(max_length=250)),
                ('Product_brand', models.CharField(max_length=250)),
                ('Product_year', models.CharField(max_length=250)),
                ('Product_price', models.FloatField(max_length=250)),
                ('Product_image', models.CharField(max_length=11250)),
                ('Product_details', models.CharField(max_length=11250)),
                ('Product_bids', models.IntegerField(max_length=250)),
                ('Product_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dreambuy.Category')),
            ],
        ),
    ]