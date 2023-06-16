from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('QuerySetAPI.urls')),
    path('', include('QuerySetAPI_2.urls')),
    path('', include('QuerySetAPI_4.urls')),
]
