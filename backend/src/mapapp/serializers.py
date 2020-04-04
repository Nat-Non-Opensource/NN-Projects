from .models import Map
from rest_framework import serializers


class MapSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Map
        fields = ('place_name', 'place_description', 'place_latitude', 'place_longitude')
