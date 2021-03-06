from .models import Area, Salon, Stylist, Review,PhoneNumber,MenuItem
from django.contrib.auth.models import User
from rest_framework import viewsets, generics
from .serializer import AreaSerializer, SalonSerializer, StylistSerializer, UserSerializer,PhoneNumberSerializer
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.response import Response
from RestAPIs.serializer import ReviewCreateSerializer, ReviewListSerializer,\
    MenuItemSerializer
from rest_framework.generics import GenericAPIView
from rest_framework.exceptions import APIException, PermissionDenied
from math import radians, cos, sin, asin, sqrt
from APIUtils import APIUtils
from rest_framework.decorators import permission_classes


    
class SalonRetrieveView(generics.RetrieveAPIView):
    queryset = Salon.objects.all()
    serializer_class = SalonSerializer

class SalonListBySearchLocationView(generics.ListAPIView):
    queryset = Salon.objects.all()
    serializer_class = SalonSerializer
    
    def list(self, request, *args, **kwargs):
        # TODO: use the below lat,lon,city from constant variables or more cleaner way
        lat = request.query_params['lat']
        lon = request.query_params['lon']
        city = request.query_params['city']
        salons_serialized = get_salons_within_range(float(lat), float(lon), city)
        if salons_serialized == None:
            raise APIException(detail='Could not find any salons for the given location.')
        return Response({'salons': salons_serialized}, status=200)

def get_salons_within_range(latitude, longitude, city=None):
    if latitude == None or longitude == None:
        return None
    city_salons = Salon.objects.filter(area__city_name=city)
    salons = []
    for salon in city_salons:
        if get_distance_using_haversine(longitude, latitude, salon.longitude, salon.latitude) <= 5:
            serializer = SalonSerializer(salon)
            salons.append(serializer.data)
    return salons

def get_distance_using_haversine(lon1, lat1, lon2, lat2):
    """
    Calculate the great circle distance between two points 
    on the earth (specified in decimal degrees)
    """
    # convert decimal degrees to radians 
    lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])

    # haversine formula 
    dlon = lon2 - lon1 
    dlat = lat2 - lat1 
    a = sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlon / 2) ** 2
    c = 2 * asin(sqrt(a))

    # 6367 km is the radius of the Earth
    km = 6367 * c
    return km

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
    
class PhoneNumberUpdateView(generics.UpdateAPIView):
    queryset = PhoneNumber.objects.all()
    serializer_class = PhoneNumberSerializer
    permission_classes = [IsAdminUser]


class ReviewCreateView(generics.CreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewCreateSerializer
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.validated_data['user'] = request.user
        serializer.save()
        return Response(serializer.data, status=201)

class ReviewUpdateView(generics.UpdateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewCreateSerializer
    permission_classes = [IsAuthenticated]

    def update(self, request, *args, **kwargs):
        review = self.get_object()
        if request.user.is_staff or request.user == review.user:
            return generics.UpdateAPIView.update(self, request, *args, **kwargs)
        else:
            raise PermissionDenied('Review cannot be modified by current user')
    
class ReviewsBySalonView(GenericAPIView):
    queryset = Review.objects.all()
    def get(self, request, *args, **kwargs):
        if kwargs.get('pk') is None:
            return Response('[]')
        response_data = {'reviews_data': APIUtils.getReviewsBySalonWithStylistAndUserData(**kwargs) ,
                          'aggregate_rating':APIUtils.getSalonOverallRatingandVotes(**kwargs) }

        return Response(response_data, status=200)
             
class MenuItemsBySalonView(GenericAPIView):
     queryset = MenuItem.objects.all()
     def get(self,request,*args,**kwargs):
        if kwargs.get('pk') is None:
            return Response('[]')
        response_data = {}
        return Response(response_data,status=200)
               

class ReviewsByStylistView(generics.ListAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewListSerializer

    def list(self, request, *args, **kwargs):
        if kwargs.get('pk') is None:
            return Response('[]')
        self.queryset = Review.objects.filter(stylist=kwargs.get('pk'))
        return generics.ListAPIView.list(self, request, *args, **kwargs)

class ReviewsByUserView(generics.ListAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewListSerializer

    def list(self, request, *args, **kwargs):
        if kwargs.get('pk') is None:
            return Response('[]')
        self.queryset = Review.objects.filter(user=kwargs.get('pk'))
        return generics.ListAPIView.list(self, request, *args, **kwargs)

    
class MenuItemCreateView(generics.CreateAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer
    permission_classes = [IsAdminUser]


class MenuItemUpdateView(generics.UpdateAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer
    permission_classes = [IsAdminUser]

