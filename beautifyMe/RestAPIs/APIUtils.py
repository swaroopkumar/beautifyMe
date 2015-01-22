from __future__ import division
from RestAPIs.models import Review, PhoneNumber, Salon,Stylist, MenuItem
from .serializer import ReviewListSerializer,PhoneNumberSerializer,MenuItemSerializer
from django.db import connection
from django.contrib.contenttypes.models import ContentType


class APIUtils :
    @staticmethod
    def getSalonOverallRatingandVotes(**kwargs):
        cursor = connection.cursor()
        cursor.execute("select sum(rating),count(*) from restapis_review where salon_id = "+kwargs.get('pk'))
        aggregate_rating = 0.0
        try :
            total_rows = cursor.fetchone()
            aggregate_rating= total_rows[0]/total_rows[1]
        except ZeroDivisionError:
            pass
        return {'total_rating' :round(aggregate_rating,1),'total_votes':total_rows[1]}

    
    @staticmethod
    def getReviewsBySalonWithStylistAndUserData(**kwargs):
        review_objects= Review.objects.all().filter(salon=kwargs.get('pk')).select_related('stylist','user')
        review_dict = ReviewListSerializer(review_objects,many=True).data
        stylist_dict = {}
        users_dict = {}
        for review in review_dict:
            stylist_dict[review['stylist']['id']] = review['stylist']
            users_dict[review['user']['id']] = review['user']
            review['stylist'] = review['stylist']['id']
            review['user'] = review['user']['id']
        
        return {'review_data' : review_dict ,'stylist_data' : stylist_dict ,'user_data' : users_dict}  
    
    @staticmethod
    def getPhoneNumberBySalon(**kwargs):
        phone_objects = PhoneNumber.objects.all().filter(object_id = kwargs.get('pk'),content_type = ContentType.objects.get_for_model(Salon))
        return PhoneNumberSerializer(phone_objects,many=True).data
        
    @staticmethod
    def getPhoneNumberByStylist(**kwargs):
        phone_objects = PhoneNumber.objects.all().filter(object_id = kwargs.get('pk'),content_type = ContentType.objects.get_for_model(Stylist))
        return PhoneNumberSerializer(phone_objects,many=True).data
    
    @staticmethod
    def getMenuItemsBySalon(**kwargs):
        menu_objects = MenuItem.objects.all().filter(salon=kwargs.get('pk'))
        return MenuItemSerializer(menu_objects,many=True).data
    
    
                
