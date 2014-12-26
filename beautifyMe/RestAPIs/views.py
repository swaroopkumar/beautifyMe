from django.shortcuts import render
from .models import Area, Salon, Stylist, Review
from rest_framework import viewsets
from .serializer import AreaSerializer
from .serializer import SalonSerializer
from .serializer import StylistSerializer
from .serializer import ReviewSerializer

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