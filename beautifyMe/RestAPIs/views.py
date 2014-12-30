from .models import Area, Salon, Stylist, Review
from django.contrib.auth.models import User
from rest_framework import viewsets, generics
from .serializer import AreaSerializer, SalonSerializer, StylistSerializer, ReviewSerializer, UserSerializer
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FormParser

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

class SalonUpdateView(generics.UpdateAPIView):
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

class StylistUpdateView(generics.UpdateAPIView):
    queryset = Stylist.objects.all()
    serializer_class = StylistSerializer
    permission_classes = [IsAdminUser]

class ReviewCreateView(generics.CreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [IsAuthenticated]
    parser_classes = (MultiPartParser, FormParser)

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response();

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

class ReviewsByUserView(generics.ListAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

    def list(self, request, *args, **kwargs):
        if kwargs.get('pk') is None:
            return Response('[]')
        self.queryset = Review.objects.filter(user=kwargs.get('pk'))
        return generics.ListAPIView.list(self, request, *args, **kwargs)

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAdminUser]
