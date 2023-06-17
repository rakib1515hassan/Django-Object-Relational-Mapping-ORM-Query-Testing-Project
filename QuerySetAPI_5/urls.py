from django.urls import path, include
from QuerySetAPI_5.views import *

urlpatterns = [
    path('QuerySetAPI_5/', QuerySetAPI_5, name='QuerySetAPI_5'),   

    path('Q_marks/', Q_marks, name='Q_marks'),    
    path('Q_book_publisher/', Q_book_publisher, name='Q_book_publisher'),    
    path('Q_storage_book_auther/', Q_storage_book_auther, name='Q_storage_book_auther'),    
]
