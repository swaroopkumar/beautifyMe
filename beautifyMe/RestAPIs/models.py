from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now

# Create your models here.

class Area(models.Model):
    area_name= models.CharField(max_length=150,null=False,blank=False,unique=True)
    pin_code = models.IntegerField(null=False,blank=False,unique=False)
    city_name= models.CharField(max_length=100,null=False,blank=False,unique=False)
    creation_date = models.DateTimeField(null=False,blank=False,default=now)
    last_updated = models.DateTimeField(null=False,blank=False,default=now)
    def __str__(self):
        return ' '.join([self.area_name])

class PhoneNumber(models.Model):
    Phone_Number_Type_Choices = ((1,'Home'),(2,'Mobile'),(3,'Work'))
    area_code = models.CharField(max_length=5,null=False,blank=False,unique=True) 
    phone_number = models.CharField(max_length=10,unique = True,null=False,blank=False)
    is_verified = models.BooleanField(null = False,blank = False,default=False)
    def __str__(self):
        return ' '.join([self.area_code,self.phone_number])

class Salon(models.Model):
    Price_Range_Choices = (
                         (1,'Budget'),
                         (2,'Expensive'),
                         (3,'Premium'))
    Salon_Type_Choices = (
                         (1,'UniSex'),
                         (2,'Male'),
                         (3,'Female'))
    salon_name= models.CharField(max_length=250,null=False,blank=False,unique=True)
    address_line1= models.CharField(max_length=700,null=False,blank=False,unique=False) 
    land_mark = models.CharField(max_length=200,null=False,blank=False,unique=False)
    area = models.ForeignKey(Area,null=False,blank=False)
    price_range= models.IntegerField(null=False,blank = False,choices=Price_Range_Choices,default=1)
    email_id = models.CharField(max_length=200,null=False,blank=False)
    is_mail_id_verified = models.BooleanField(null=False,blank=False,default=False)
    salon_type = models.IntegerField(choices = Salon_Type_Choices,null=False,blank = False,default=1)
    rating = models.IntegerField()
    parking_available= models.BooleanField(null=False,blank=False,default=False)
    latitude = models.FloatField(null=False,blank=False)
    longitude=models.FloatField(null=False,blank=False)
    creation_date = models.DateTimeField(null=False,blank=False,default=now)
    last_updated = models.DateTimeField(null=False,blank=False,default=now)
    def __str__(self):
        return self.salon_name

class SalonTimings(models.Model):
    Day_Of_Week = ((1,'Monday'),(2,'Tuesday'),(3,'Wednesday'),(4,'Thursday'),(5,'Friday'),(6,'Saturday'),
                           (7,'Sunday'))
    Day_of_week = models.IntegerField(choices=Day_Of_Week,null=False,unique=False,default=1)
    open_time = models.TimeField(null=False,blank = False,default=now)
    end_time= models.TimeField(null=False,blank = False,default=now)
    Salon_Id = models.ForeignKey(Salon,null=False,blank=False)

class MenuItem(models.Model):
    Item_Name= models.CharField(max_length=150,null=False,blank=False,unique=True)
    Item_Description=models.CharField(max_length=2000,null=False,blank=False,unique=False)
    Item_cost = models.IntegerField(null=False,blank = False)
    Duration = models.IntegerField(null=False,blank = False)
    Salon_Id = models.ForeignKey(Salon,null=False,blank=False)
    creation_date = models.DateTimeField(null=False,blank=False,default=now)
    last_updated = models.DateTimeField(null=False,blank=False,default=now)

class Stylist(models.Model):
    salon_type = ((1,'Makeup Artist'),(2,'Hair Stylist'),(3,'Massasuer'),(4,'Hair and Makeup Artist'))
    first_name = models.CharField(max_length=150,null=False,blank=False,unique=True)
    last_name = models.CharField(max_length=150,null=False,blank=False,unique=True)
    rating = models.IntegerField(null=False,blank=False)
    specialization=models.CharField(max_length=200,null=False,blank=False)
    short_description = models.CharField(max_length=200,null=False,blank=False)
    type = models.IntegerField(null=False,blank=False,choices=salon_type)
    salon = models.ForeignKey(Salon,null=False,blank=False)
    creation_date = models.DateTimeField(null=False,blank=False,default=now)
    last_updated = models.DateTimeField(null=False,blank=False,default=now)
    def __str__(self):
        return self.first_name + ' ' + self.last_name

class Review(models.Model):
    salon = models.ForeignKey(Salon,null=False,blank=False)
    stylist = models.ForeignKey(Stylist,null=False,blank=False)
    user = models.ForeignKey(User,null=False,blank=False)
    rating = models.IntegerField(null=False,blank=False)
    review_text = models.CharField(max_length=2000,null=False,blank=False)
    creation_date = models.DateTimeField(null=False,blank=False,default=now)
    last_updated = models.DateTimeField(null=False,blank=False,default=now)
     
class Photos(models.Model):
    foriegn_key = models.IntegerField(null=False,blank=False)
    s3_key = models.CharField(max_length=200,null=False,blank=False,unique=True)
    creation_date = models.DateTimeField(null=False,blank=False,default=now)

