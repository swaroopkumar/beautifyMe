from .models import Area, Salon, Stylist, Review
from django.contrib.auth.models import User
from rest_framework import viewsets, generics
from .serializer import AreaSerializer, SalonSerializer, StylistSerializer, ReviewSerializer, UserSerializer
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response

class AreaViewSet(viewsets.ModelViewSet):
    queryset = Area.objects.all()
    serializer_class = AreaSerializer
    permission_classes = [IsAdminUser]

class SalonRetrieveView(generics.RetrieveAPIView):
    queryset = Salon.objects.all()
    serializer_class = SalonSerializer

class SalonCreateView(generics.CreateAPIView):
    queryset = Salon.objects.all()
    serializer_class = SalonSerializer
    permission_classes = [IsAdminUser]

class StylistRetrieveView(generics.RetrieveAPIView):
    queryset = Stylist.objects.all()
    serializer_class = StylistSerializer

class StylistsBySalonView(generics.ListAPIView):
    queryset = Stylist.objects.all()
    serializer_class = StylistSerializer
    
    def list(self, request, *args, **kwargs):
        if kwargs.get('pk') is None:
            return Response('[]')
        self.queryset = Stylist.objects.filter(salon=kwargs.get('pk'))
        return generics.ListAPIView.list(self, request, *args, **kwargs)

class StylistCreateView(generics.CreateAPIView):
    queryset = Stylist.objects.all()
    serializer_class = StylistSerializer
    permission_classes = [IsAdminUser]
        
class ReviewsBySalonView(generics.ListAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

    def list(self, request, *args, **kwargs):
        if kwargs.get('pk') is None:
            return Response('[]')
        self.queryset = Review.objects.filter(salon=kwargs.get('pk'))
        return generics.ListAPIView.list(self, request, *args, **kwargs)

class ReviewsByStylistView(generics.ListAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

    def list(self, request, *args, **kwargs):
        if kwargs.get('pk') is None:
            return Response('[]')
        self.queryset = Review.objects.filter(stylist=kwargs.get('pk'))
        return generics.ListAPIView.list(self, request, *args, **kwargs)

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAdminUser]
