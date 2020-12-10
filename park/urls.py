from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^parks$', views.park_list),
    url(r'^parks/(?P<pk>[0-9]+)$', views.park_detail),
]
