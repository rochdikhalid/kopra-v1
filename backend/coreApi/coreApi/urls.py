from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/stations/', include('stations.urls')),
    path('api/drivers/', include('drivers.urls')),
]
