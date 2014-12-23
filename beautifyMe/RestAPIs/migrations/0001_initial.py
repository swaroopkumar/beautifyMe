# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Area',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Area_Name', models.CharField(unique=True, max_length=150)),
                ('Pin_Code', models.IntegerField(max_length=6)),
                ('City_Name', models.CharField(max_length=100)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Customer_name', models.CharField(max_length=200)),
                ('Email_Id', models.CharField(max_length=200)),
                ('is_mail_Id_verified', models.BooleanField(default=False)),
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
                ('Item_cost', models.IntegerField(max_length=5)),
                ('Duration', models.IntegerField(max_length=5)),
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
            name='Review',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Photo_Count', models.IntegerField(default=0, max_length=100)),
                ('Rating', models.IntegerField(max_length=1)),
                ('Review_String', models.CharField(max_length=200, null=True)),
                ('Customer_Id', models.ForeignKey(to='RestAPIs.Customer')),
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
                ('Address_Line1', models.CharField(max_length=700)),
                ('Land_mark', models.CharField(max_length=200)),
                ('Photo_Count', models.IntegerField(default=0, max_length=100)),
                ('Price_Range', models.CharField(default=1, max_length=1, choices=[(1, b'Budget'), (2, b'Expensive'), (3, b'Premium')])),
                ('Email_Id', models.CharField(max_length=200)),
                ('is_mail_Id_verified', models.BooleanField(default=False)),
                ('Salon_Type', models.CharField(default=1, max_length=1, choices=[(1, b'UniSex'), (2, b'Male'), (3, b'Female')])),
                ('Rating', models.IntegerField(max_length=1)),
                ('Parking_Available', models.BooleanField()),
                ('Latitude', models.FloatField()),
                ('Longitude', models.FloatField()),
                ('Area', models.ForeignKey(to='RestAPIs.Area')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='SalonTimings',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Day_of_week', models.IntegerField(default=1, max_length=1, choices=[(1, b'Monday'), (2, b'Tuesday'), (3, b'Wednesday'), (4, b'Thursday'), (5, b'Friday'), (6, b'Saturday'), (7, b'Sunday')])),
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
                ('Stylist_First_name', models.CharField(unique=True, max_length=150)),
                ('Stylist_Last_name', models.CharField(unique=True, max_length=150)),
                ('Rating', models.IntegerField(max_length=1)),
                ('Specialization', models.CharField(max_length=200)),
                ('Photo_Count', models.IntegerField(max_length=200)),
                ('Short_Description', models.CharField(max_length=200)),
                ('Stylist_Type', models.IntegerField(max_length=1)),
                ('Salon_Id', models.ForeignKey(to='RestAPIs.Salon')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='review',
            name='Stylist_Id',
            field=models.ForeignKey(to='RestAPIs.Stylist'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='review',
            name='salon_Id',
            field=models.ForeignKey(to='RestAPIs.Salon'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='menuitem',
            name='Salon_Id',
            field=models.ForeignKey(to='RestAPIs.Salon'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='customer',
            name='Phone_Number',
            field=models.ForeignKey(to='RestAPIs.PhoneNumber'),
            preserve_default=True,
        ),
    ]
