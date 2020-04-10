from .models import Map
from .models import Map_Image
from rest_framework import serializers


class MapSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Map
        fields = '__all__'


# class MapImageSerializer(serializers, HyperlinkedModelSerializer):
#     class Meta:
#         model = Map_Image
#         fields = '__all__'
