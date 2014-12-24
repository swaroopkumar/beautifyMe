from django.shortcuts import render
from .models import Area
from rest_framework import viewsets
from .serializer import AreaSerializer

# Create your views here.

class AreaViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Area.objects.all()
    serializer_class = AreaSerializer