from django.http import HttpResponse
from .models import Map
from .serializers import MapSerializer
from rest_framework import viewsets, status
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from django.views.decorators.csrf import csrf_exempt


# Create your views here.
def index(request):
    return HttpResponse("<h1>Map</h1>")


class MapViewSet(viewsets.ModelViewSet):
    queryset = Map.objects.all()
    serializer_class = MapSerializer


# API
@csrf_exempt
def map_list(request):
    # Get list
    if request.method == 'GET':
        maps = Map.objects.all()
        maps_serializer = MapSerializer(maps, many=True)
        return JsonResponse(maps_serializer.data, safe=False)

    # Add one
    if request.method == 'POST':
        map_data = JSONParser().parser(request)
        maps_serializer = MapSerializer(data=map_data)
        if maps_serializer.is_valid():
            maps_serializer.save()
            return JsonResponse(map_data.data, status=status.HTTP_201_CREATED)
        return JsonResponse(maps_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # Delete list
    if request.method == 'DELETE':
        Map.objects.all().delete()
        return HttpResponse(status=status.HTTP_204_NO_CONTENT)


@csrf_exempt
def map_detail(request, pk):
    try:
        mapping = Map.objects.get(pk=pk)
    except mapping.DoesNotExist:
        return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    # Retrieve one record
    if request.method == 'GET':
        map_serializer = MapSerializer(mapping)
        return JsonResponse(map_serializer.data)

    # Update one record
    if request.method == 'PUT':
        map_data = JSONParser().parser(request)
        map_serializer = MapSerializer(mapping, data=map_data)
        if map_serializer.is_valid():
            map_serializer.save()
            return JsonResponse(map_serializer.data)
        return JsonResponse(map_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # Delete one record
    if request.method == 'DELETE':
        Map.delete()
        return HttpResponse(status=status.HTTP_204_NO_CONTENT)
