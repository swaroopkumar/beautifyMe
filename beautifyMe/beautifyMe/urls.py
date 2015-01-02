from django.conf.urls import include, url
from django.contrib import admin
from rest_framework import routers
from RestAPIs.views import AreaViewSet, UserViewSet, SalonRetrieveView, StylistRetrieveView, StylistsBySalonView,\
    SalonCreateView, StylistCreateView, ReviewsBySalonView, ReviewsByStylistView,\
    ReviewCreateView, ReviewsByUserView, SalonUpdateView, StylistUpdateView,\
    ReviewUpdateView, SalonListBySearchLocationView


# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'areas', AreaViewSet)
router.register(r'users', UserViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^salons/(?P<pk>\d+)/$', SalonRetrieveView.as_view(), name='salon-detail'),
    url(r'^salons/$', SalonCreateView.as_view(), name='salon-create'),
    url(r'^salons/search/$', SalonListBySearchLocationView.as_view(), name='salon-search'),
    url(r'^salons/update/(?P<pk>\d+)/$', SalonUpdateView.as_view(), name='salon-update'),
    url(r'^salons/(?P<pk>\d+)/stylists/$', StylistsBySalonView.as_view(), name='salon-stylist-list'),
    url(r'^salons/(?P<pk>\d+)/reviews/$', ReviewsBySalonView.as_view(), name='salon-reviews-list'),
    url(r'^stylists/(?P<pk>\d+)/$', StylistRetrieveView.as_view(), name='stylist-detail'),
    url(r'^stylists/$', StylistCreateView.as_view(), name='stylist-create'),
    url(r'^stylists/update/(?P<pk>\d+)/$', StylistUpdateView.as_view(), name='stylist-update'),
    url(r'^stylists/(?P<pk>\d+)/reviews/$', ReviewsByStylistView.as_view(), name='stylist-reviews-list'),
    url(r'^reviews/$', ReviewCreateView.as_view(), name='review-create'),
    url(r'^reviews/update/(?P<pk>\d+)/$', ReviewUpdateView.as_view(), name='review-update'),
    url(r'^users/(?P<pk>\d+)/reviews/$', ReviewsByUserView.as_view(), name='user-reviews-list'),
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
