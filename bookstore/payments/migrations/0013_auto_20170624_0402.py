# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-24 04:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payments', '0012_auto_20170624_0039'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
        migrations.AddField(
            model_name='order',
            name='tax_price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=6),
        ),
    ]
