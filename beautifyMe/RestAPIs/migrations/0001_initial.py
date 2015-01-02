# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Area',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('area_name', models.CharField(unique=True, max_length=150)),
                ('pin_code', models.IntegerField()),
                ('city_name', models.CharField(max_length=100)),
                ('creation_date', models.DateTimeField(default=datetime.datetime(2014, 12, 30, 14, 28, 50, 296309))),
                ('last_updated', models.DateTimeField(default=datetime.datetime(2014, 12, 30, 14, 28, 50, 296345))),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='MenuItem',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Item_Name', models.CharField(unique=True, max_length=150)),
                ('Item_Description', models.CharField(max_length=2000)),
                ('Item_cost', models.IntegerField()),
                ('Duration', models.IntegerField()),
                ('creation_date', models.DateTimeField(default=datetime.datetime(2014, 12, 30, 14, 28, 50, 299477))),
                ('last_updated', models.DateTimeField(default=datetime.datetime(2014, 12, 30, 14, 28, 50, 299519))),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='PhoneNumber',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('area_code', models.CharField(unique=True, max_length=5)),
                ('phone_number', models.CharField(unique=True, max_length=10)),
                ('is_verified', models.BooleanField(default=False)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Photos',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('foriegn_key', models.IntegerField()),
                ('s3_key', models.CharField(unique=True, max_length=200)),
                ('creation_date', models.DateTimeField(default=datetime.datetime(2014, 12, 30, 14, 28, 50, 302825))),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('rating', models.IntegerField()),
                ('review_text', models.CharField(max_length=200, null=True)),
                ('creation_date', models.DateTimeField(default=datetime.datetime(2014, 12, 30, 14, 28, 50, 301832))),
                ('last_updated', models.DateTimeField(default=datetime.datetime(2014, 12, 30, 14, 28, 50, 301872))),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Salon',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('salon_name', models.CharField(unique=True, max_length=250)),
                ('address_line1', models.CharField(max_length=700)),
                ('land_mark', models.CharField(max_length=200)),
                ('price_range', models.IntegerField(default=1, choices=[(1, b'Budget'), (2, b'Expensive'), (3, b'Premium')])),
                ('email_id', models.CharField(max_length=200)),
                ('is_mail_id_verified', models.BooleanField(default=False)),
                ('salon_type', models.IntegerField(default=1, choices=[(1, b'UniSex'), (2, b'Male'), (3, b'Female')])),
                ('rating', models.IntegerField()),
                ('parking_available', models.BooleanField(default=False)),
                ('latitude', models.FloatField()),
                ('longitude', models.FloatField()),
                ('creation_date', models.DateTimeField(default=datetime.datetime(2014, 12, 30, 14, 28, 50, 297839))),
                ('last_updated', models.DateTimeField(default=datetime.datetime(2014, 12, 30, 14, 28, 50, 297867))),
                ('area', models.ForeignKey(to='RestAPIs.Area')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='SalonTimings',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Day_of_week', models.IntegerField(default=1, choices=[(1, b'Monday'), (2, b'Tuesday'), (3, b'Wednesday'), (4, b'Thursday'), (5, b'Friday'), (6, b'Saturday'), (7, b'Sunday')])),
                ('open_time', models.TimeField(default=datetime.datetime.now)),
                ('end_time', models.TimeField(default=datetime.datetime.now)),
                ('Salon_Id', models.ForeignKey(to='RestAPIs.Salon')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Stylist',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('first_name', models.CharField(unique=True, max_length=150)),
                ('last_name', models.CharField(unique=True, max_length=150)),
                ('rating', models.IntegerField()),
                ('specialization', models.CharField(max_length=200)),
                ('short_description', models.CharField(max_length=200)),
                ('type', models.IntegerField(choices=[(1, b'Makeup Artist'), (2, b'Hair Stylist'), (3, b'Massasuer'), (4, b'Hair and Makeup Artist')])),
                ('creation_date', models.DateTimeField(default=datetime.datetime(2014, 12, 30, 14, 28, 50, 300729))),
                ('last_updated', models.DateTimeField(default=datetime.datetime(2014, 12, 30, 14, 28, 50, 300774))),
                ('salon', models.ForeignKey(to='RestAPIs.Salon')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='review',
            name='salon',
            field=models.ForeignKey(to='RestAPIs.Salon'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='review',
            name='stylist',
            field=models.ForeignKey(to='RestAPIs.Stylist'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='review',
            name='user',
            field=models.ForeignKey(default=1, to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='menuitem',
            name='Salon_Id',
            field=models.ForeignKey(to='RestAPIs.Salon'),
            preserve_default=True,
        ),
    ]
