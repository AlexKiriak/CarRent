from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.conf.urls import url, include
# admin.autodiscover()

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include('car.urls')),
    url(r'^', include('park.urls')),
    url(r'^', include('ordr.urls')),
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
