from django.urls import path, include
from QuerySetAPI_4.views import *

urlpatterns = [
    path('QuerySetAPI_4/', QuerySetAPI_4, name='QuerySetAPI_4'),

    path('aggregate_testing/', aggregate_testing, name='aggregate_testing'),
    
]
