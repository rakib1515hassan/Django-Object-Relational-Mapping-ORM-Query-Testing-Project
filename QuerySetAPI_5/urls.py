from django.urls import path, include
from QuerySetAPI_5.views import *

urlpatterns = [
    path('QuerySetAPI_5/', QuerySetAPI_5, name='QuerySetAPI_5'),   

    path('Q_marks/', Q_marks, name='Q_marks'),    
    path('Q_book_publisher/', Q_book_publisher, name='Q_book_publisher'),    
    path('Q_storage_book_auther/', Q_storage_book_auther, name='Q_storage_book_auther'),  
      
    path('Q_book__auther/', Q_book__auther, name='Q_book__auther'),    
    path('FilteredBooksView/', FilteredBooksView.as_view(), name='FilteredBooksView'), 

    path('Q_book__name_price/', Q_book__name_price, name='Q_book__name_price'), 
    path('Q_book__name_price_2/', Q_book__name_price_2, name='Q_book__name_price_2'),

    path('student__not_pass/', student__not_pass, name='student__not_pass'), 
    path('student__city_pass/', student__city_pass, name='student__city_pass'), 


    path('test_auth/', test_auth),       
]
