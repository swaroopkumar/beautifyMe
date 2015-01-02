from django.conf.urls import include, url
from django.contrib import admin

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url(r'^apis/', include('RestAPIs.urls')),
    url(r'^admin/', include(admin.site.urls))
]

# urlpatterns = patterns('',
#     # Examples:
#     # url(r'^$', 'beautifyMe.views.home', name='home'),
#     # url(r'^blog/', include('blog.urls')),
# 
#     url(r'^admin/', include(admin.site.urls)),
# )
