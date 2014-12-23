# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('RestAPIs', '0002_auto_20141223_1540'),
    ]

    operations = [
        migrations.AlterField(
            model_name='salon',
            name='Price_Range',
            field=models.IntegerField(default=1, max_length=1, choices=[(1, b'Budget'), (2, b'Expensive'), (3, b'Premium')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='salon',
            name='Salon_Type',
            field=models.IntegerField(default=1, max_length=1, choices=[(1, b'UniSex'), (2, b'Male'), (3, b'Female')]),
            preserve_default=True,
        ),
    ]
