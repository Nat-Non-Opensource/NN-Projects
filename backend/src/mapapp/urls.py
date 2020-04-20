from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [

    url(r'^$', views.map_list),
    url(r'^(?P<pk>[0-9]+)$', views.map_detail),
]
