# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('RestAPIs', '0003_auto_20141223_1636'),
    ]

    operations = [
        migrations.RenameField(
            model_name='review',
            old_name='Review_String',
            new_name='Review_Text',
        ),
        migrations.AlterField(
            model_name='area',
            name='Pin_Code',
            field=models.IntegerField(),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='customer',
            name='Customer_FB_GP_ID_REASON',
            field=models.IntegerField(default=1, choices=[(1, b'Facebook'), (2, b'GooglePlus')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='menuitem',
            name='Duration',
            field=models.IntegerField(),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='menuitem',
            name='Item_cost',
            field=models.IntegerField(),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='review',
            name='Photo_Count',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='review',
            name='Rating',
            field=models.IntegerField(),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='salon',
            name='Photo_Count',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='salon',
            name='Price_Range',
            field=models.IntegerField(default=1, choices=[(1, b'Budget'), (2, b'Expensive'), (3, b'Premium')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='salon',
            name='Rating',
            field=models.IntegerField(),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='salon',
            name='Salon_Type',
            field=models.IntegerField(default=1, choices=[(1, b'UniSex'), (2, b'Male'), (3, b'Female')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='salontimings',
            name='Day_of_week',
            field=models.IntegerField(default=1, choices=[(1, b'Monday'), (2, b'Tuesday'), (3, b'Wednesday'), (4, b'Thursday'), (5, b'Friday'), (6, b'Saturday'), (7, b'Sunday')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='stylist',
            name='Photo_Count',
            field=models.IntegerField(),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='stylist',
            name='Rating',
            field=models.IntegerField(),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='stylist',
            name='Stylist_Type',
            field=models.IntegerField(),
            preserve_default=True,
        ),
    ]
