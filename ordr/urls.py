from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^order$', views.order_list),
    url(r'^order/(?P<order_id>[0-9]+)$', views.order_detail)
]
