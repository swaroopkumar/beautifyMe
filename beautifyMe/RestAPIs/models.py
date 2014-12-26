from django.db import models
from datetime import datetime
from django.contrib.auth.models import User

# Create your models here.

class Area(models.Model):
    Area_Name= models.CharField(max_length=150,null=False,blank=False,unique=True)
    Pin_Code = models.IntegerField(null=False,blank=False,unique=False)
    City_Name= models.CharField(max_length=100,null=False,blank=False,unique=False)
    def __str__(self):
        return ' '.join([self.Area_Name])

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
    Address_Line1= models.CharField(max_length=700,null=False,blank=False,unique=False) 
    Land_mark = models.CharField(max_length=200,null=False,blank=False,unique=False)
    Photo_Count = models.IntegerField(null=False,unique=False,default=0)
    Area = models.ForeignKey(Area)
    Price_Range= models.IntegerField(null=False,blank = False,choices=Price_Range_Choices,default=1)
    Email_Id = models.CharField(max_length=200,null=False,blank=False)
    is_mail_Id_verified = models.BooleanField(null=False,blank=False,default=False)
    Salon_Type = models.IntegerField(choices = Salon_Type_Choices,null=False,blank = False,default=1)
    Rating = models.IntegerField()
    Parking_Available= models.BooleanField(null= False,blank = False)
    Latitude = models.FloatField(null=False,blank=False)
    Longitude=models.FloatField(null=False,blank=False)
    def __str__(self):
        return self.salon_name

class SalonTimings(models.Model):
    Day_Of_Week = ((1,'Monday'),(2,'Tuesday'),(3,'Wednesday'),(4,'Thursday'),(5,'Friday'),(6,'Saturday'),
                           (7,'Sunday'))
    Day_of_week = models.IntegerField(choices=Day_Of_Week,null=False,unique=False,default=1)
    open_time = models.TimeField(null=False,blank = False,default=datetime.now)
    end_time= models.TimeField(null=False,blank = False,default=datetime.now)
    Salon_Id = models.ForeignKey(Salon)

class MenuItem(models.Model):
    Item_Name= models.CharField(max_length=150,null=False,blank=False,unique=True)
    Item_Description=models.CharField(max_length=2000,null=False,blank=False,unique=False)
    Item_cost = models.IntegerField(null=False,blank = False)
    Duration = models.IntegerField(null=False,blank = False)
    Salon_Id = models.ForeignKey(Salon)

class Stylist(models.Model):
    salon_type = ((1,'Makeup Artist'),(2,'Hair Stylist'),(3,'Massasuer'),(4,'Hair and Makeup Artist'))
    first_name = models.CharField(max_length=150,null=False,blank=False,unique=True)
    last_name = models.CharField(max_length=150,null=False,blank=False,unique=True)
    rating = models.IntegerField(null=False,blank=False)
    specialization=models.CharField(max_length=200,null=False,blank=False)
    photo_count = models.IntegerField(null=False,blank=False)
    short_description = models.CharField(max_length=200,null=False,blank=False)
    type = models.IntegerField(null=False,blank=False,choices=salon_type)
    salon = models.ForeignKey(Salon)
    def __str__(self):
        return self.First_name + ' ' + self.Last_name

class Review(models.Model):
    salon = models.ForeignKey(Salon) 
    stylist = models.ForeignKey(Stylist)
    user = models.ForeignKey(User,default=1)
    photo_count = models.IntegerField(null=False,unique=False,default=0)
    rating = models.IntegerField(null=False,blank=False)
    review_text = models.CharField(max_length=200,null=True)
     


