from django.contrib import admin

# Register your models here.
from models import *

class AreaAdmin(admin.ModelAdmin):
    list_display = ('Area_Name','Pin_Code', 'City_Name')

admin.site.register(PhoneNumber)
admin.site.register(Area, AreaAdmin)
admin.site.register(Salon)
admin.site.register(SalonTimings)
admin.site.register(Stylist)
admin.site.register(MenuItem)
admin.site.register(Review)








