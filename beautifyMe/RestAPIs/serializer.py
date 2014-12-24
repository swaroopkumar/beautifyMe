from rest_framework import serializers
from .models import Area

class AreaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Area
        fields = ('Area_Name','Pin_Code', 'City_Name')