from django.urls import path #, include
# from rest_framework import routers
from django.conf.urls import url

from . import views

# router = routers.DefaultRouter()
# router.register(r'location', views.MapViewSet)

urlpatterns = [
    # path('', views.index, name="index")
    # path('', include(router.urls))
    url(r'^$', views.map_list),
    url(r'^(?P<pk>[0-9]+)$', views.map_detail),
    # path('images', views.display_place_images, name = 'placeImages'),
]
