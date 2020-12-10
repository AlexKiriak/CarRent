from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^cars$', views.car_list),
    url(r'^cars/(?P<pk>[0-9]+)$', views.car_detail),
]
