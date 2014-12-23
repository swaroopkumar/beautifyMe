# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('RestAPIs', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='Customer_FB_GP_ID',
            field=models.CharField(default=0, max_length=30),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='customer',
            name='Customer_FB_GP_ID_REASON',
            field=models.IntegerField(default=1, max_length=1, choices=[(1, b'Facebook'), (2, b'GooglePlus')]),
            preserve_default=True,
        ),
    ]
