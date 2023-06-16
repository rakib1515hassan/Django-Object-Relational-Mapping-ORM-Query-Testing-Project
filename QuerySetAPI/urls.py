from django.urls import path
from QuerySetAPI.views import *

urlpatterns = [
    path('', home, name='home'),

    path('add-student', add_student, name='add_student'),
    path('edit-student/<int:id>/', edit_student, name='edit_student'),
    path('delete-student/', delete_student, name='delete_student'),

    path('QuerySetAPI_1/', QuerySetAPI_1, name='QuerySetAPI_1'),


    path('show_all/', show_all, name='show_all'),

    path('get_by_id/<int:id>/', get_by_id, name='get_by_id'),
    path('get_by_pk/<int:pk>/', get_by_pk, name='get_by_pk'),

    path('filter_by_mark/', filter_by_mark, name='filter_by_mark'),
    path('filter_by_mark_first/', filter_by_mark_first, name='filter_by_mark_first'),
    path('filter_by_mark_and_city/', filter_by_mark_and_city, name='filter_by_mark_and_city'),

    path('exclude_mark/', exclude_mark, name='exclude_mark'),
    path('exclude_city/', exclude_city, name='exclude_city'),
    path('exclude_city_and_mark/', exclude_city_and_mark, name='exclude_city_and_mark'),
    
    path('ascending_order_by_city/', ascending_order_by_city, name='ascending_order_by_city'),
    path('descending_order_by_city/', descending_order_by_city, name='descending_order_by_city'),
    path('random_order_by_city/', random_order_by_city, name='random_order_by_city'),
    path('descending_order_by_id/', descending_order_by_id, name='descending_order_by_id'),
    path('ascending_order_by_id_show_5_data/', ascending_order_by_id_show_5_data, name='ascending_order_by_id_show_5_data'),

    path('values/', values, name='values'),
    path('values_name_and_city/', values_name_and_city, name='values_name_and_city'),

    path('distinct_name/', distinct_name, name='distinct_name'),

    path('values_list_name/', values_list_name, name='values_list_name'),

    path('using/', using, name='using'),

    path('union/', union, name='union'),
    path('union_name_city/', union_name_city, name='union_name_city'),

    path('intersection_name/', intersection_name, name='intersection_name'),
    path('intersection_name_city/', intersection_name_city, name='intersection_name_city'),

    path('difference_name/', difference_name, name='difference_name'),
    path('difference_name_city/', difference_name_city, name='difference_name_city'),


]
