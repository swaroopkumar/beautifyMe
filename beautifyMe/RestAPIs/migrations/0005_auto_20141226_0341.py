# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('RestAPIs', '0004_auto_20141226_0340'),
    ]

    operations = [
        migrations.RenameField(
            model_name='stylist',
            old_name='Stylist_First_name',
            new_name='First_name',
        ),
        migrations.RenameField(
            model_name='stylist',
            old_name='Stylist_Last_name',
            new_name='Last_name',
        ),
        migrations.RenameField(
            model_name='stylist',
            old_name='Stylist_Type',
            new_name='Type',
        ),
    ]
