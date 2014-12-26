# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('RestAPIs', '0005_auto_20141226_0341'),
    ]

    operations = [
      migrations.AddField(
            model_name='review',
            name='user_id',
            field=models.ForeignKey(default=1, to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='stylist',
            name='Type',
            field=models.IntegerField(choices=[(1, b'Makeup Artist'), (2, b'Hair Stylist'), (3, b'Massasuer'), (4, b'Hair and Makeup Artist')]),
            preserve_default=True,
        ),
        migrations.RemoveField(
            model_name='customer',
            name='Phone_Number',
        ),
        migrations.RemoveField(
            model_name='review',
            name='Customer_Id',
        ),
        migrations.DeleteModel(
            name='Customer',
        )
   ]
