from rest_framework import serializers
from .models import Area
from .models import Salon
from .models import Stylist
from .models import Review
from django.contrib.auth.models import User

class AreaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Area
        fields = ('Area_Name','Pin_Code', 'City_Name')

class SalonSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Salon
        fields = ('salon_name', 'Address_Line1', 'Land_mark', 'Photo_Count', 'Area', 
                  'Price_Range', 'Email_Id', 'is_mail_Id_verified', 
                  'Salon_Type', 'Rating', 'Parking_Available', 'Latitude', 
                  'Longitude')

class StylistSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Stylist
        fields = ('First_name','Last_name', 'Rating','Specialization',
                  'Photo_Count','Short_Description', 'Type','Salon_Id')

class ReviewSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Review
        fields = ('salon','stylist','user','photo_count','rating','review_text')

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name')
