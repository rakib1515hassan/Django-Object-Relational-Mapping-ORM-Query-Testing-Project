from django.urls import path, include
from QuerySetAPI_2.views import *

urlpatterns = [
    path('QuerySetAPI_2/', QuerySetAPI_2, name='QuerySetAPI_2'),
    path('test/', test, name='test'),

    path('first/', first, name='first'),
    path('last/', last, name='last'),
    path('latest/', latest, name='latest'),
    path('earliest/', earliest, name='earliest'),

    path('get_or_create_http/', get_or_create_http, name='get_or_create_http'),
    path('get_or_create/', get_or_create, name='get_or_create'),
    path('update/<int:given_id>/', update, name='update'),
    path('update_or_create/<int:given_id>/<str:given_name>/', update_or_create, name='update_or_create'),
    path('bulk_create/', bulk_create, name='bulk_create'),



    path('QuerySetAPI_3/', QuerySetAPI_3, name='QuerySetAPI_3'),

    path('exact_mark/', exact_mark, name='exact_mark'),
    path('less_then_mark/', less_then_mark, name='less_then_mark'),
    path('getter_then_mark/', getter_then_mark, name='getter_then_mark'),
    path('less_then_or_equeal/', less_then_or_equeal, name='less_then_or_equeal'),
    path('getter_then_or_equeal/', getter_then_or_equeal, name='getter_then_or_equeal'),

    path('exact_name/', exact_name, name='exact_name'),
    path('iexact_name/', iexact_name, name='iexact_name'),

    path('contains_name/', contains_name, name='contains_name'),
    path('icontains_name/', icontains_name, name='icontains_name'),

    path('id_in/', id_in, name='id_in'),
    path('marks_in/', marks_in, name='marks_in'),

    path('startswith_name/', startswith_name, name='startswith_name'),
    path('istartswith_name/', istartswith_name, name='istartswith_name'),

    path('endswith_name/', endswith_name, name='endswith_name'),
    path('iendswith_name/', iendswith_name, name='iendswith_name'),

    path('range_marks/', range_marks, name='range_marks'),
    path('range_birthOFdate/', range_birthOFdate, name='range_birthOFdate'),

    path('date_join/', date_join, name='date_join'),
    path('date_join_lessthen/', date_join_lessthen, name='date_join_lessthen'),
    path('date_join_geterthen/', date_join_geterthen, name='date_join_geterthen'),
    path('date_join_geterthen_equel/', date_join_geterthen_equel, name='date_join_geterthen_equel'),

    path('year_pass/', year_pass, name='year_pass'),
    path('year_pass__lte/', year_pass__lte, name='year_pass__lte'),

    path('month_pass__lte/', month_pass__lte, name='month_pass__lte'),

    path('day_pass__lte/', day_pass__lte, name='day_pass__lte'),

    path('week_pass__lte/', week_pass__lte, name='week_pass__lte'),

    path('week_day_pass/', week_day_pass, name='week_day_pass'),
    path('week_day_pass__lte/', week_day_pass__lte, name='week_day_pass__lte'),

    path('quarter_pass/', quarter_pass, name='quarter_pass'),
    
    path('time_join/', time_join, name='time_join'),

    path('hour_join/', hour_join, name='hour_join'),

    path('minute_join/', minute_join, name='minute_join'),

    path('second_join/', second_join, name='second_join'),
]
