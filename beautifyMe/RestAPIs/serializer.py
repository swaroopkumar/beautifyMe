from rest_framework import serializers
from .models import Area
from .models import Salon
from .models import Stylist
from .models import Review
from django.contrib.auth.models import User

class AreaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Area
        fields = ('id', 'area_name', 'pin_code', 'city_name')

class SalonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Salon
        fields = ('id', 'salon_name', 'address_line1', 'land_mark', 'area', 
                  'price_range', 'email_id', 'is_mail_id_verified', 
                  'salon_type', 'rating', 'parking_available', 'latitude', 
                  'longitude')

class SalonMinDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = Salon
        fields = ('id', 'salon_name', 'area', 'rating')


class StylistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stylist
        fields = ('id', 'first_name','last_name', 'rating','specialization',
                  'short_description', 'type','salon')

class StylistMinDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stylist
        fields = ('id', 'first_name','last_name', 'rating')
        
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'last_name')


class ReviewListSerializer(serializers.ModelSerializer):
    stylist = StylistMinDataSerializer()
    user = UserSerializer()    
    class Meta:
        model = Review
        fields = ('id', 'salon', 'stylist', 'rating', 'review_text', 'user')
        
class ReviewCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ('id', 'salon', 'stylist', 'rating', 'review_text')


