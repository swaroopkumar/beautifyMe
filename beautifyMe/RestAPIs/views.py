from django.shortcuts import render
from .models import Area, Salon, Stylist, Review
from django.contrib.auth.models import User
from rest_framework import viewsets
from .serializer import AreaSerializer, SalonSerializer, StylistSerializer, ReviewSerializer, UserSerializer

class AreaViewSet(viewsets.ModelViewSet):
    queryset = Area.objects.all()
    serializer_class = AreaSerializer

class SalonViewSet(viewsets.ModelViewSet):
    queryset = Salon.objects.all()
    serializer_class = SalonSerializer

class StylistViewSet(viewsets.ModelViewSet):
    queryset = Stylist.objects.all()
    serializer_class = StylistSerializer
    
class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer