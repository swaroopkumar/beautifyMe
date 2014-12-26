# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('RestAPIs', '0006_auto_20141226_0644'),
    ]

    operations = [
       migrations.RenameField(
            model_name='review',
            old_name='Photo_Count',
            new_name='photo_count',
        ),
        migrations.RenameField(
            model_name='review',
            old_name='Rating',
            new_name='rating',
        ),
        migrations.RenameField(
            model_name='review',
            old_name='Review_Text',
            new_name='review_text',
        ),
        migrations.RenameField(
            model_name='review',
            old_name='salon_Id',
            new_name='salon',
        ),
        migrations.RenameField(
            model_name='review',
            old_name='Stylist_Id',
            new_name='stylist',
        ),
        migrations.RenameField(
            model_name='review',
            old_name='user_id',
            new_name='user',
        )
   ]
