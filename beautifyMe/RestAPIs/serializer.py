from rest_framework import serializers
from .models import Area
from .models import Salon
from .models import Stylist
from .models import Review
from django.contrib.auth.models import User

class AreaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Area
        fields = ('id', 'area_name', 'pin_code', 'city_name')

class SalonSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Salon
        fields = ('id', 'salon_name', 'address_line1', 'land_mark', 'area', 
                  'price_range', 'email_id', 'is_mail_id_verified', 
                  'salon_type', 'rating', 'parking_available', 'latitude', 
                  'longitude')

class StylistSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Stylist
        fields = ('id', 'first_name','last_name', 'rating','specialization',
                  'short_description', 'type','salon')

class ReviewSerializer(serializers.HyperlinkedModelSerializer):
    photos = serializers.ImageField()
    class Meta:
        model = Review
        fields = ('id', 'salon','stylist','user','rating','review_text')

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'last_name')
