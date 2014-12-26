# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('RestAPIs', '0007_auto_20141226_0703'),
    ]

    operations = [
        migrations.RenameField(
            model_name='stylist',
            old_name='First_name',
            new_name='first_name',
        ),
        migrations.RenameField(
            model_name='stylist',
            old_name='Last_name',
            new_name='last_name',
        ),
        migrations.RenameField(
            model_name='stylist',
            old_name='Photo_Count',
            new_name='photo_count',
        ),
        migrations.RenameField(
            model_name='stylist',
            old_name='Rating',
            new_name='rating',
        ),
        migrations.RenameField(
            model_name='stylist',
            old_name='Salon_Id',
            new_name='salon',
        ),
        migrations.RenameField(
            model_name='stylist',
            old_name='Short_Description',
            new_name='short_description',
        ),
        migrations.RenameField(
            model_name='stylist',
            old_name='Specialization',
            new_name='specialization',
        ),
        migrations.RenameField(
            model_name='stylist',
            old_name='Type',
            new_name='type',
        ),
    ]
