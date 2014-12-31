from django.shortcuts import render_to_response
from django.shortcuts import  RequestContext
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from UserManagement.AnyBodyCanAuthenticate import AnyBodyCanAuthenticate
from allauth.socialaccount.models import SocialLogin, SocialToken, SocialApp
from allauth.socialaccount.providers.facebook.views import fb_complete_login
from allauth.socialaccount.helpers import complete_social_login
from rest_framework.parsers import JSONParser
from rest_framework.response import Response

# Create your views here.

class FacebookLoginOrSignup(APIView):   
     permission_classes = (AllowAny,)
     authentication_classes = (AnyBodyCanAuthenticate,)
             
    
     def post(self, request):  
          print "posting data"      
          data = JSONParser().parse(request)
          access_token = data.get('access_token', '')    
        
          try:
               print request
               app = SocialApp.objects.get(provider="facebook")
               token = SocialToken(app=app, token=access_token)
                            
               login = fb_complete_login(app, token)
               login.token = token
               login.state = SocialLogin.state_from_request(request)
               print login
               ret = complete_social_login(request, login)
               return Response(status=200, data={
                'success': True,
                'username': request.user.username,
                'user_id': request.user.pk,
            })
          except:
               return Response(status=401 ,data={
                'success': False,
                'reason': "Bad Access Token",
            })
