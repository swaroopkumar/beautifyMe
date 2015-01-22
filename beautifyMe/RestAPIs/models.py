from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey

# Create your models here.
limit_content_type = models.Q(app_label = 'RestAPIs', model = 'salon') | models.Q(app_label = 'RestAPIs', model = 'stylist') |models.Q(app_label = 'auth', model = 'user') 
entity_type_choices = ((1,'salon'),(2,'stylist'),(3,'user'))


class Area(models.Model):
    area_name= models.CharField(max_length=150,null=False,blank=False,unique=True)
    pin_code = models.IntegerField(null=False,blank=False,unique=False)
    city_name= models.CharField(max_length=100,null=False,blank=False,unique=False)
    creation_date = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User,null=False,blank=False,related_name = '%(class)s_created_user')
    last_updated_by = models.ForeignKey(User,null=False,blank=False,related_name='%(class)s_updated_user')
    def __str__(self):
        return ' '.join([self.area_name])


class PhoneNumber(models.Model):
    country_code_choices = ( (1,'+91'), )
    country_code = models.IntegerField(max_length=2,null=False,blank=False,unique=False,choices = country_code_choices,default=1) 
    area_code = models.CharField(max_length=5,null=False,blank=False,unique=False)
    phone_number = models.CharField(max_length=10,unique = True,null=False,blank=False)
    is_verified = models.BooleanField(null = False,blank = False,default=False)
    content_type = models.ForeignKey(ContentType,limit_choices_to = limit_content_type)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')
    creation_date = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User,null=False,blank=False,related_name = '%(class)s_created_user')
    last_updated_by = models.ForeignKey(User,null=False,blank=False,related_name='%(class)s_updated_user')

    def __str__(self):
        return ' '.join([self.area_code,self.phone_number])

class Salon(models.Model):
    price_range_choices = (
                         (1,'Budget'),
                         (2,'Expensive'),
                         (3,'Premium'))
    salon_type_choices = (
                         (1,'UniSex'),
                         (2,'Male'),
                         (3,'Female'))
    salon_name= models.CharField(max_length=250,null=False,blank=False,unique=True)
    address_line1= models.CharField(max_length=700,null=False,blank=False,unique=False) 
    land_mark = models.CharField(max_length=200,null=False,blank=False,unique=False)
    area = models.ForeignKey(Area,null=False,blank=False)
    price_range= models.IntegerField(null=False,blank = False,choices=price_range_choices,default=1)
    email_id = models.CharField(max_length=200,null=False,blank=False)
    is_mail_id_verified = models.BooleanField(null=False,blank=False,default=False)
    salon_type = models.IntegerField(choices = salon_type_choices,null=False,blank = False,default=1)
    rating = models.IntegerField()
    parking_available= models.BooleanField(null=False,blank=False,default=False)
    latitude = models.FloatField(null=False,blank=False)
    longitude=models.FloatField(null=False,blank=False)
    creation_date = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User,null=False,blank=False,related_name = '%(class)s_created_user')
    last_updated_by = models.ForeignKey(User,null=False,blank=False,related_name='%(class)s_updated_user')
    def __str__(self):
        return self.salon_name

class SalonTimings(models.Model):
    day_of_week_choices = ((1,'Monday'),(2,'Tuesday'),(3,'Wednesday'),(4,'Thursday'),(5,'Friday'),(6,'Saturday'),
                           (7,'Sunday'))
    day_of_week = models.IntegerField(choices=day_of_week_choices,null=False,unique=False,default=1)
    open_time = models.TimeField(null=False,blank = False,default=timezone.now)
    end_time= models.TimeField(null=False,blank = False,default=timezone.now)
    salon = models.ForeignKey(Salon,null=False,blank=False)
    creation_date = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User,null=False,blank=False,related_name = '%(class)s_created_user')
    last_updated_by = models.ForeignKey(User,null=False,blank=False,related_name='%(class)s_updated_user')


class MenuItem(models.Model):
    item_name= models.CharField(max_length=150,null=False,blank=False,unique=True)
    item_description=models.CharField(max_length=2000,null=False,blank=False,unique=False)
    item_cost = models.IntegerField(null=False,blank = False)
    duration = models.IntegerField(null=False,blank = False)
    salon = models.ForeignKey(Salon,null=False,blank=False)
    creation_date = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User,null=False,blank=False,related_name = '%(class)s_created_user',editable=False)
    last_updated_by = models.ForeignKey(User,null=False,blank=False,related_name='%(class)s_updated_user',editable=False)

class Stylist(models.Model):
    stylist_type_choices = ((1,'Makeup Artist'),(2,'Hair Stylist'),(3,'Massasuer'),(4,'Hair and Makeup Artist'))
    first_name = models.CharField(max_length=150,null=False,blank=False,unique=True)
    last_name = models.CharField(max_length=150,null=False,blank=False,unique=True)
    rating = models.IntegerField(null=False,blank=False)
    specialization=models.CharField(max_length=200,null=False,blank=False)
    short_description = models.CharField(max_length=200,null=False,blank=False)
    type = models.IntegerField(null=False,blank=False,choices=stylist_type_choices)
    salon = models.ForeignKey(Salon,null=False,blank=False)
    creation_date = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User,null=False,blank=False,related_name = '%(class)s_created_user')
    last_updated_by = models.ForeignKey(User,null=False,blank=False,related_name='%(class)s_updated_user')
    def __str__(self):
        return self.first_name + ' ' + self.last_name

class Review(models.Model):
    salon = models.ForeignKey(Salon,null=False,blank=False)
    stylist = models.ForeignKey(Stylist,null=False,blank=False)
    user = models.ForeignKey(User,null=False,blank=False)
    rating = models.IntegerField(null=False,blank=False)
    review_text = models.CharField(max_length=2000,null=False,blank=False)
    creation_date = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User,null=False,blank=False,related_name = '%(class)s_created_user')
    last_updated_by = models.ForeignKey(User,null=False,blank=False,related_name='%(class)s_updated_user')
     
class Photo(models.Model):
    content_type = models.ForeignKey(ContentType,limit_choices_to = limit_content_type)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')
    cloud_id = models.CharField(max_length=200,null=False,blank=False,unique=True)
    creation_date = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User,null=False,blank=False,related_name = '%(class)s_created_user')
    last_updated_by = models.ForeignKey(User,null=False,blank=False,related_name='%(class)s_updated_user')

