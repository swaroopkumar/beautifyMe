from rest_framework import permissions
from rest_framework.permissions import IsAdminUser


class SalonPermissions(permissions.BasePermission):
     def has_permission(self, request, view):
          if request.method not in permissions.SAFE_METHODS:
               return False
          print request
          print request.method
          #if IsAdminUser.has_permission(self, request, view):
          return True