#Adding a comment 
from django.conf.urls import patterns, include, url
from django.contrib import admin
from rest_framework import routers
from RestAPIs.models import Area
from RestAPIs.views import AreaViewSet

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'areas', AreaViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^admin/', include(admin.site.urls))
]

# urlpatterns = patterns('',
#     # Examples:
#     # url(r'^$', 'beautifyMe.views.home', name='home'),
#     # url(r'^blog/', include('blog.urls')),
# 
#     url(r'^admin/', include(admin.site.urls)),
# )
