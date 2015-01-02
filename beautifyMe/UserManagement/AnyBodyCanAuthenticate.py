from rest_framework.authentication import SessionAuthentication
class  AnyBodyCanAuthenticate(SessionAuthentication):
     def authenticate(self, request):
          return None
     