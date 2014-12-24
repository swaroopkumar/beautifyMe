from django.db import models
from datetime import datetime

# Create your models here.

class Area(models.Model):
    Area_Name= models.CharField(max_length=150,null=False,blank=False,unique=True)
    Pin_Code = models.IntegerField(max_length=6,null=False,blank=False,unique=False)
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
     
class Customer(models.Model):
    Customer_FB_GP_ID_REASON_choices = ((1,'Facebook'),(2,'GooglePlus')) 
    Customer_name = models.CharField(max_length=200,null=False,blank=False)
    Email_Id = models.CharField(max_length=200,null=False,blank=False)
    is_mail_Id_verified = models.BooleanField(null=False,blank=False,default=False)
    Phone_Number = models.ForeignKey(PhoneNumber)
    Customer_FB_GP_ID = models.CharField(max_length=30,null=False,blank=False,default=0)
    Customer_FB_GP_ID_REASON = models.IntegerField(max_length=1,null=False,blank=False,choices=Customer_FB_GP_ID_REASON_choices,default=1)
    def __str__(self):
        return self.Customer_name

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
    Photo_Count = models.IntegerField(max_length=100,null=False,unique=False,default=0)
    Area = models.ForeignKey(Area)
    Price_Range= models.IntegerField(max_length=1,null=False,blank = False,choices=Price_Range_Choices,default=1)
    Email_Id = models.CharField(max_length=200,null=False,blank=False)
    is_mail_Id_verified = models.BooleanField(null=False,blank=False,default=False)
    Salon_Type = models.IntegerField(max_length= 1 ,choices = Salon_Type_Choices,null=False,blank = False,default=1)
    Rating = models.IntegerField(max_length=1 )
    Parking_Available= models.BooleanField(null= False,blank = False)
    Latitude = models.FloatField(null=False,blank=False)
    Longitude=models.FloatField(null=False,blank=False)
    def __str__(self):
        return self.salon_name

class SalonTimings(models.Model):
    Day_Of_Week_Choices = ((1,'Monday'),(2,'Tuesday'),(3,'Wednesday'),(4,'Thursday'),(5,'Friday'),(6,'Saturday'),
                           (7,'Sunday'))
    Day_of_week = models.IntegerField(max_length= 1,choices=Day_Of_Week_Choices,null=False,unique=False,default=1)
    open_time = models.TimeField(null=False,blank = False,default=datetime.now)
    end_time= models.TimeField(null=False,blank = False,default=datetime.now)
    Salon_Id = models.ForeignKey(Salon)     

class MenuItem(models.Model):
    Item_Name= models.CharField(max_length=150,null=False,blank=False,unique=True)
    Item_Description=models.CharField(max_length=2000,null=False,blank=False,unique=False)
    Item_cost = models.IntegerField(max_length=5 ,null=False,blank = False)
    Duration = models.IntegerField(max_length=5,null=False,blank = False)
    Salon_Id = models.ForeignKey(Salon)

class Stylist(models.Model):
    Salon_Type_Choices = ((1,'Makeup Artist'),(2,'Hair Stylist'),(3,'Massasuer'),(4,'Hair and Makeup Artist'))
    Stylist_First_name = models.CharField(max_length=150,null=False,blank=False,unique=True)
    Stylist_Last_name = models.CharField(max_length=150,null=False,blank=False,unique=True)
    Rating = models.IntegerField(max_length=1,null=False,blank=False)
    Specialization=models.CharField(max_length=200,null=False,blank=False)
    Photo_Count = models.IntegerField(max_length=200,null=False,blank=False)
    Short_Description = models.CharField(max_length=200,null=False,blank=False)
    Stylist_Type = models.IntegerField(max_length=1,null=False,blank=False,)
    Salon_Id = models.ForeignKey(Salon)

class Review(models.Model):
    salon_Id = models.ForeignKey(Salon) 
    Stylist_Id = models.ForeignKey(Stylist)
    Customer_Id = models.ForeignKey(Customer) 
    Photo_Count = models.IntegerField(max_length=100,null=False,unique=False,default=0)
    Rating = models.IntegerField(max_length=1,null=False,blank=False)
    Review_String = models.CharField(max_length= 200,null=True)
     


