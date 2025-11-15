from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from constellations.views import index
from objects.views import index

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('constellations.urls')),
    path('', include('objects.urls')),
    path('accounts/', include ('django.contrib.auth.urls'))
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
