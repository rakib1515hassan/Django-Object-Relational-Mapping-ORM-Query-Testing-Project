from django.shortcuts import render, redirect
from django.contrib import messages
from QuerySetAPI.models import Student, Teacher
from django.core.exceptions import ObjectDoesNotExist, ValidationError
from django.http import HttpResponse

# Create your views here.

def home(request):
    std_obj = Student.objects.all().order_by('roll')
    teacher_obj = Teacher.objects.all().order_by('emplyee_id')

    data = {
        'std_obj': std_obj,
        'all_student': Student.objects.all().count(),
        'teacher_obj': teacher_obj,
        'all_teacher': Teacher.objects.all().count(),
    }
    return render(request, 'home.html', data)


def QuerySetAPI_1(request):
    return render(request, 'QuerySetAPI_1.html')


        
# NOTE All Querry Set in Django ORM-------------------------------------------------------------------------------
#---------------------------------all()------------------------------------
def show_all(request):
    std_obj = Student.objects.all().order_by('roll')    
    # print(Student.objects.all().exists()) # যদি std_obj থাকে তবে True return করবে else False return করবে    

    data = {
        'std_obj': std_obj,
        'SQL_querry': std_obj.query,
        'querry_title': ".all()",
        'total_obj': std_obj.count(),
        'descripetion': "Show all data",
    }    
    return render(request, 'all_query.html', data)
#__________________________________________________________________________
#---------------------------------get()------------------------------------
def get_by_id(request, id):
    try:
        std_obj_get = Student.objects.get(id=id)
        s_id = std_obj_get.id
        data = {
            'std_obj_get': std_obj_get,
            'querry_title': ".get( id = id )",
            'total_student': Student.objects.all().count(),
            # 'SQL_querry': std_obj_get.query,
            'descripetion': "Show a student who's id is ="+str(s_id),
        }    
        return render(request, 'all_query.html', data)
    except Student.DoesNotExist:
        messages.error(request, "This Student is't found.")
        return redirect(home)

def get_by_pk(request, pk):
    try:
        std_obj_get = Student.objects.get( pk = pk )
        s_id = std_obj_get.id
        data = {
            'std_obj_get': std_obj_get,
            'querry_title': ".get( pk = pk )",
            'total_student': Student.objects.all().count(),
            # 'SQL_querry': std_obj_get.query,
            'descripetion': "Show a student who's pk is ="+str(s_id),
        }    
        return render(request, 'all_query.html', data)
    except Student.DoesNotExist:
        messages.error(request, "This Student is't found.")
        return redirect(home)
#__________________________________________________________________________    
#---------------------------------filter()---------------------------------
def filter_by_mark(request):
    std_obj = Student.objects.filter(marks = 75)
    
    # std_obj = Student.objects.filter(roll__isnull = True) # এটি চেক করে roll field এ কোন Null value আছে কি না।

    # std_obj = Student.objects.filter(id=3).update(marks = 70) # id=3 হলে তার marks = 70 করে দেতি চাইলে।

    ## print("SQL Querry Of This Object = ", std_obj.query)
    ## Result = SELECT "QuerySetAPI_student"."id", "QuerySetAPI_student"."name", "QuerySetAPI_student"."roll", "QuerySetAPI_student"."date_of_birth", "QuerySetAPI_student"."city", "QuerySetAPI_student"."marks", "QuerySetAPI_student"."pass_date" FROM "QuerySetAPI_student" WHERE "QuerySetAPI_student"."marks" = 75
    data = {
            'std_obj': std_obj,
            'querry_title': ".filter(marks = 75)",
            'total_student': Student.objects.all().count(),
            'total_obj': std_obj.count(),
            'SQL_querry': std_obj.query,
            'descripetion': "Show all students, those makes is =75",
        }    
    return render(request, 'all_query.html', data)

def filter_by_mark_first(request):
    std_obj = Student.objects.filter(marks = 75).first()
    # std_obj = Student.objects.filter(marks = 75).last()
    data = {
            'std_obj_get': std_obj,
            'querry_title': ".filter(marks = 75).first()",
            'total_student': Student.objects.all().count(),
            'total_obj': 1,
            'descripetion': "Show a student, whos makes is =75 and id is first",
        }    
    return render(request, 'all_query.html', data)

def filter_by_mark_and_city(request):
    std_obj = Student.objects.filter(marks = 75, city = 'Chandpur')

    ## print("SQL Querry Of This Object = ", std_obj.query)
    ## Result = SELECT "QuerySetAPI_student"."id", "QuerySetAPI_student"."name", "QuerySetAPI_student"."roll", "QuerySetAPI_student"."date_of_birth", "QuerySetAPI_student"."city", "QuerySetAPI_student"."marks", "QuerySetAPI_student"."pass_date" FROM "QuerySetAPI_student" WHERE ("QuerySetAPI_student"."city" = Chandpur AND "QuerySetAPI_student"."marks" = 75)

    data = {
            'std_obj': std_obj,
            'SQL_querry': std_obj.query,
            'querry_title': ".filter(marks = 75, city = 'Chandpur')",
            'total_student': Student.objects.all().count(),
            'total_obj': std_obj.count(),
            'descripetion': "Show a student, whos makes is = 75 and city = 'Chandpur'",
        }    
    return render(request, 'all_query.html', data)

#__________________________________________________________________________

#---------------------------------exclude()---------------------------------
def exclude_mark(request):
    std_obj = Student.objects.exclude(marks = 75)
    ## print("SQL Querry Of This Object = ", std_obj.query)
    ## Result = SELECT "QuerySetAPI_student"."id", "QuerySetAPI_student"."name", "QuerySetAPI_student"."roll", "QuerySetAPI_student"."date_of_birth", "QuerySetAPI_student"."city", "QuerySetAPI_student"."marks", "QuerySetAPI_student"."pass_date" FROM "QuerySetAPI_student" WHERE NOT ("QuerySetAPI_student"."marks" = 75 AND "QuerySetAPI_student"."marks" IS NOT NULL)
    data = {
            'std_obj': std_obj,
            'SQL_querry': std_obj.query,
            'querry_title': ".exclude(marks = 75)",
            'total_student': Student.objects.all().count(),
            'total_obj': std_obj.count(),
            'descripetion': "যে সব ছাত্রের মার্ক ৭৫ না, তাদের সকলকে দেখাবে।",
        }    
    return render(request, 'all_query.html', data)

def exclude_city(request):
    std_obj = Student.objects.exclude(city = 'Chandpur')
    std_obj = Student.objects.exclude(marks = 75, city = 'Chandpur')
    data = {
            'std_obj': std_obj,
            'SQL_querry': std_obj.query,
            'querry_title': ".exclude(city = 'Chandpur')",
            'total_student': Student.objects.all().count(),
            'total_obj': std_obj.count(),
            'descripetion': "যে সব ছাত্রের city = chandpur না, তাদের সকলকে দেখাবে।",
        }    
    return render(request, 'all_query.html', data)

def exclude_city_and_mark(request):
    std_obj = Student.objects.exclude(marks = 75, city = 'Chandpur')
    data = {
            'std_obj': std_obj,
            'SQL_querry': std_obj.query,
            'querry_title': ".exclude(marks = 75, city = 'Chandpur')",
            'total_student': Student.objects.all().count(),
            'total_obj': std_obj.count(),
            'descripetion': "যে সব ছাত্রের city = chandpur এবং mark = 75 পেয়েছে, তাদের সকলকে বাদ দিয়ে, বাকি দের দেখাবে।",
        }    
    return render(request, 'all_query.html', data)

#__________________________________________________________________________

#---------------------------------order_by()---------------------------------
def ascending_order_by_city(request):
    std_obj = Student.objects.order_by('city') ## Ascending Order

    ## print("SQL Querry Of This Object = ", std_obj.query)
    ## Result = SELECT "QuerySetAPI_student"."id", "QuerySetAPI_student"."name", "QuerySetAPI_student"."roll", "QuerySetAPI_student"."date_of_birth", "QuerySetAPI_student"."city", "QuerySetAPI_student"."marks", "QuerySetAPI_student"."pass_date" FROM "QuerySetAPI_student" ORDER BY "QuerySetAPI_student"."city" ASC
    data = {
            'std_obj': std_obj,
            'SQL_querry': std_obj.query,
            'querry_title': ".order_by('city')",
            'total_student': Student.objects.all().count(),
            'total_obj': std_obj.count(),
            'descripetion': "সবগুলো Data কে city অনুসারে Ascending order এ সাজানো হয়েছে।",
        }    
    return render(request, 'all_query.html', data)

def descending_order_by_city(request):
    std_obj = Student.objects.order_by('-city') ## Descending Order
    ## print("SQL Querry Of This Object = ", std_obj.query)
    ## Result = SELECT "QuerySetAPI_student"."id", "QuerySetAPI_student"."name", "QuerySetAPI_student"."roll", "QuerySetAPI_student"."date_of_birth", "QuerySetAPI_student"."city", "QuerySetAPI_student"."marks", "QuerySetAPI_student"."pass_date" FROM "QuerySetAPI_student" ORDER BY "QuerySetAPI_student"."city" DESC
    data = {
            'std_obj': std_obj,
            'SQL_querry': std_obj.query,
            'querry_title': ".order_by('-city')",
            'total_student': Student.objects.all().count(),
            'total_obj': std_obj.count(),
            'descripetion': "সবগুলো Data কে city অনুসারে Descending order এ সাজানো হয়েছে।",
        }    
    return render(request, 'all_query.html', data)

def random_order_by_city(request):
    std_obj = Student.objects.order_by('?') ## Randomly

    ## print("SQL Querry Of This Object = ", std_obj.query)
    ## Result = SELECT "QuerySetAPI_student"."id", "QuerySetAPI_student"."name", "QuerySetAPI_student"."roll", "QuerySetAPI_student"."date_of_birth", "QuerySetAPI_student"."city", "QuerySetAPI_student"."marks", "QuerySetAPI_student"."pass_date" FROM "QuerySetAPI_student" ORDER BY RAND() ASC

    data = {
            'std_obj': std_obj,
            'SQL_querry': std_obj.query,
            'querry_title': ".order_by('?')",
            'total_student': Student.objects.all().count(),
            'total_obj': std_obj.count(),
            'descripetion': "সবগুলো Data কে city অনুসারে Randomly order এ সাজানো হয়েছে।",
        }    
    return render(request, 'all_query.html', data)

def descending_order_by_id(request):
    std_obj = Student.objects.order_by('-id')[:5] ## লাষ্ট থেকে ৫ টি data দেখাবে [start=0 : end = 5]

    ## print("SQL Querry Of This Object = ", std_obj.query)
    ## Result = SELECT "QuerySetAPI_student"."id", "QuerySetAPI_student"."name", "QuerySetAPI_student"."roll", "QuerySetAPI_student"."date_of_birth", "QuerySetAPI_student"."city", "QuerySetAPI_student"."marks", "QuerySetAPI_student"."pass_date" FROM "QuerySetAPI_student" ORDER BY "QuerySetAPI_student"."id" DESC LIMIT 5

    data = {
            'std_obj': std_obj,
            'SQL_querry': std_obj.query,
            'querry_title': ".order_by('-id')[:5]",
            'total_student': Student.objects.all().count(),
            'total_obj': std_obj.count(),
            'descripetion': "সবগুলো Data কে id অনুসারে Descending order এ সাজানো হয়েছে এবং প্রথম ৫ টি data কে দেখানো হয়েছে।",
        }    
    return render(request, 'all_query.html', data)

def ascending_order_by_id_show_5_data(request):
    std_obj = Student.objects.order_by('id').reverse()[:5] ## লাষ্ট থেকে ৫ টি data দেখাবে [start=0 : end = 5]

    ## print("SQL Querry Of This Object = ", std_obj.query)
    ## Result = SELECT "QuerySetAPI_student"."id", "QuerySetAPI_student"."name", "QuerySetAPI_student"."roll", "QuerySetAPI_student"."date_of_birth", "QuerySetAPI_student"."city", "QuerySetAPI_student"."marks", "QuerySetAPI_student"."pass_date" FROM "QuerySetAPI_student" ORDER BY "QuerySetAPI_student"."id" DESC LIMIT 5

    data = {
            'std_obj': std_obj,
            'SQL_querry': std_obj.query,
            'querry_title': ".order_by('id').reverse()[:5]",
            'total_student': Student.objects.all().count(),
            'total_obj': std_obj.count(),
            'descripetion': "লাষ্ট থেকে ৫ টি data দেখাবে [start=0 : end = 5]।",
        }    
    return render(request, 'all_query.html', data)

#__________________________________________________________________________


#---------------------------------values()---------------------------------
from django.db.models.aggregates import Count
def values(request):
    std_obj = Student.objects.values() 
    data = {
            'std_obj': std_obj,
            'SQL_querry': std_obj.query,
            'querry_title': ".values()",
            'total_student': Student.objects.all().count(),
            'total_obj': std_obj.count(),
            'descripetion': "এই ক্ষেত্রে সবগুলো data return হবে। একটি list এর ভেতর dictionary আকারে return করে।",
        }    
    return render(request, 'all_query.html', data)

def values_name_and_city(request):
    std_obj = Student.objects.values('name', 'city')
    
    # a = Student.objects.values('marks').annotate(Count('marks')) # একটি নির্দিষ্ট mark এ কতজন student আছে তা দেখায়।
    """
        <QuerySet [{'marks': 20, 'marks__count': 1}, {'marks': 25, 'marks__count': 1}, {'marks': 29, 'marks__count': 1}, {'marks': 30, 'marks__count': 1}, {'marks': 31, 'marks__count': 1}, {'marks': 32, 'marks__count': 1}, {'marks': 33, 'marks__count': 1}, {'marks': 40, 'marks__count': 2}, {'marks': 50, 'marks__count': 3}, {'marks': 52, 'marks__count': 1}, {'marks': 60, 'marks__count': 2}, {'marks': 61, 'marks__count': 1}, {'marks': 65, 'marks__count': 1}, {'marks': 66, 'marks__count': 1}, {'marks': 70, 'marks__count': 1}, {'marks': 75, 'marks__count': 3}, {'marks': 80, 'marks__count': 3}, {'marks': 90, 'marks__count': 2}, {'marks': 94, 'marks__count': 1}]>
    """


    data = {
            'std_obj_value': std_obj,
            'SQL_querry': std_obj.query,
            'querry_title': ".values('name', 'city')",
            'total_student': Student.objects.all().count(),
            'total_obj': std_obj.count(),
            'descripetion': "এই ক্ষেত্রে সবগুলো data return হবে, তবে শুধু name and city column টি ছাড়া আরকোন column এর data show করবেনা।",
        }    
    return render(request, 'all_query.html', data)
#__________________________________________________________________________

#---------------------------------distinct()---------------------------------
def distinct_name(request):
    # Duplicate কোন Row থকলে তা remove করে দেয়, আমাদের যেহেতু কোন duplicate row
    # নাই তেই এইটি দেখানো সম্ভব না।
    # std_obj = Student.objects.distinct('name') 
    # print("-------------")
    # print("Distinct = ", std_obj)
    # print("-------------")
    data = {
            'std_obj_value': 'hello',
            'SQL_querry': '',
            'querry_title': ".distinct('name')",
            'total_student': Student.objects.all().count(),
            'total_obj': 0,
            'descripetion': "Duplicate কোন Row থকলে তা remove করে দেয়, আমাদের যেহেতু কোন duplicate row নাই তেই এইটি দেখানো সম্ভব না।",
        }    
    return render(request, 'all_query.html', data)

#__________________________________________________________________________
#---------------------------------distinct()---------------------------------
def values_list_name(request):
    # values এবং values_list একই , শুধু values_list এ list এর ভেতর dictionary পরিবর্তে tuple return করে।
    # যেহেতু এখানে tuple retrun করে তাই তাদের key argument name, id, city, roll ইত্যাদি দ্বারা ধরা যায় না। 
    # তাই console এ print করা হয়েছে।
    std_obj_all = Student.objects.values_list() 
    std_obj_name_id = Student.objects.values_list('id', 'name') 
    std_obj = Student.objects.values_list('id', 'name', named=True) 
    
    print("-------------")
    print("All =", std_obj_all)
    """ Result:- All =
        <QuerySet [(1, 'Md Rakib Hassan', 1001, datetime.date(1994, 10, 20), 'Dhaka', 81, datetime.date(2023, 5, 8)), (3, 'Md Hassan', 1003, datetime.date(1998, 10, 20), 'Chandpur', 75, datetime.date(2023, 2, 14)), (4, 'Md Rasel', 1004, datetime.date(1999, 5, 1), 'Saver', 60, datetime.date(2023, 3, 14)), (5, 'Anu Ontora', 1005, datetime.date(1995, 6, 1), 'Dhaka', 80, datetime.date(2015, 2, 15)), (6, 'Nabil', 1006, datetime.date(2002, 9, 27), 'Chitogong', 40, datetime.date(2023, 3, 24)), (7, 'Jarry', 1008, datetime.date(2001, 12, 11), 'Commila', 69, datetime.date(2023, 2, 24)), (8, 'Ratul', 1009, datetime.date(1998, 5, 3), 'Lalbagh', 66, datetime.date(2023, 1, 11)), (9, 'Rasel', 1009, datetime.date(1999, 4, 11), 'Azimpur', 54, datetime.date(2023, 2, 23)), (10, 'Md Sarwar Alam', 1010, datetime.date(1996, 7, 21), 'Dhanmondi', 56, datetime.date(2023, 2, 21)), (11, 'iOpu', 1011, datetime.date(2009, 1, 13), 'Gazipur', 60, datetime.date(2023, 4, 11)), (16, 'Monju', 1012, datetime.date(1995, 12, 3), 'Noakhali', 75, datetime.date(2015, 12, 20)), (17, 'Siddek', 1013, datetime.date(1999, 6, 14), 'Sonaimuri', 75, datetime.date(2015, 12, 10)), (18, 'Md Omi Hassan', 1014, datetime.date(1995, 8, 15), 'Chandpur', 75, datetime.date(2015, 12, 6)), (19, 'Md Hassan', 1015, datetime.date(1995, 10, 20), 'Dhaka', 80, datetime.date(2018, 6, 4))]>
    """
    print("-------------")
    print("Only Id and Name = ", std_obj_name_id)
    """ Result:- Only Id and Name =
         <QuerySet [(1, 'Md Rakib Hassan'), (3, 'Md Hassan'), (4, 'Md Rasel'), (5, 'Anu Ontora'), (6, 'Nabil'), (7, 'Jarry'), (8, 'Ratul'), (9, 'Rasel'), (10, 'Md Sarwar Alam'), (11, 'iOpu'), (16, 'Monju'), (17, 'Siddek'), (18, 'Md Omi Hassan'), (19, 'Md Hassan')]>
    """
    print("-------------")
    print("When named is True, then =", std_obj)
    """ Result:- When named is True, then =
         <QuerySet [Row(id=1, name='Md Rakib Hassan'), Row(id=3, name='Md Hassan'), Row(id=4, name='Md Rasel'), Row(id=5, name='Anu Ontora'), Row(id=6, name='Nabil'), Row(id=7, name='Jarry'), Row(id=8, name='Ratul'), Row(id=9, name='Rasel'), Row(id=10, name='Md Sarwar Alam'), Row(id=11, name='iOpu'), Row(id=16, name='Monju'), Row(id=17, name='Siddek'), Row(id=18, name='Md Omi Hassan'), Row(id=19, name='Md Hassan')]>
    """
    print("-------------")
    data = {
            'std_obj_value': std_obj,
            'SQL_querry': '',
            'querry_title': ".values_list('id', 'name')",
            'total_student': Student.objects.all().count(),
            'total_obj': 0,
            'descripetion': "values এবং values_list একই , শুধু values_list এ list এর ভেতর dictionary পরিবর্তে tuple return করে। যেহেতু এখানে tuple retrun করে তাই তাদের key argument name, id, city, roll ইত্যাদি দ্বারা ধরা যায় না। তাই console এ print করা হয়েছে।",
        }    
    return render(request, 'all_query.html', data)
#__________________________________________________________________________

#---------------------------------distinct()---------------------------------
def using(request):
    # যখন আমরা এখাধিক Database use করি, তখন কোন data base থেকে data retrieve কোরতে চাই এই querry set এ তা এখানে বলে দিতে পারি। আমরা যদি Default
    # data base দেখতে চাই তবে, setting.py file এ গিয়ে DATABASES = {'default':{'ENGINE':'','NAME':''}} দেয়া আছে।
    std_obj = Student.objects.using('default')
    data = {
            'std_obj': std_obj,
            'SQL_querry': '',
            'querry_title': ".values_list('id', 'name')",
            'total_student': Student.objects.all().count(),
            'total_obj': std_obj.count(),
            'descripetion': "যখন আমরা এখাধিক Database use করি, তখন কোন data base থেকে data retrieve কোরতে চাই এই querry set এ তা এখানে বলে দিতে পারি। আমরা যদি Default data base দেখতে চাই তবে, setting.py file এ গিয়ে DATABASES = {'default':{'ENGINE':'','NAME':'',}} দেয়া আছে।",
        }    
    return render(request, 'all_query.html', data)
#__________________________________________________________________________
#---------------------------------dates()---------------------------------
# def dates(request):
#     # date(field, kind, order='ASC')
#     std_obj = Student.objects.dates(field_name='name', kind='ye')
#     data = {
#             'std_obj': std_obj,
#             'SQL_querry': '',
#             'querry_title': ".values_list('id', 'name')",
#             'total_student': Student.objects.all().count(),
#             'total_obj': std_obj.count(),
#             'descripetion': "date(field, kind, order='ASC') Here, field = It Should be name of a DateField of your model. kind=It should be either 'year', 'month', 'week', 'day'.",
#         }    
#     return render(request, 'all_query.html', data)
#__________________________________________________________________________

#---------------------------------none()---------------------------------
# def dates(request):
#     std_obj = Student.objects.none()
#     data = {
#             'std_obj': std_obj,
#             'SQL_querry': '',
#             'querry_title': ".values_list('id', 'name')",
#             'total_student': Student.objects.all().count(),
#             'total_obj': std_obj.count(),
#             'descripetion': "date(field, kind, order='ASC') Here, field = It Should be name of a DateField of your model. kind=It should be either 'year', 'month', 'week', 'day'.",
#         }    
#     return render(request, 'all_query.html', data)
#__________________________________________________________________________

#---------------------------------union()---------------------------------
def union(request):
    # qs_1 এবং qs_2 সবগুলো data এর  name যাদের মিল রয়েছে তাদের একবার নিয়ে এবং বাকি গুলোকে দেখাবে।
    # a = {4,5,6,7,8} b={1,2,3,4,5} Now a.union(b) = {1,2,3,4,5,6,7,8}
    qs_1 = Student.objects.values_list('name',  named=True)
    qs_2 = Teacher.objects.values_list('name',  named=True)
    std_obj = qs_1.union(qs_2)

    data = {
            'std_obj_value': std_obj,
            'SQL_querry': std_obj.query,
            'querry_title': "qs_1.union(qs_2)",
            'total_student': qs_1.count() + qs_2.count(),
            'total_obj': std_obj.count(),
            'descripetion': "qs_1 এবং qs_2 সবগুলো data এর  name যাদের মিল রয়েছে তাদের একবার নিয়ে এবং বাকি গুলোকে দেখাবে।  a = {4,5,6,7,8} b={1,2,3,4,5} Now a.union(b) = {1,2,3,4,5,6,7,8}",
        }    
    return render(request, 'all_query.html', data)

def union_name_city(request):
    # qs_1 এবং qs_2 সবগুলো data এর  name যাদের মিল রয়েছে তাদের একবার নিয়ে এবং বাকি গুলোকে দেখাবে।
    # a = {(a,b), (c,d), (e,f)}  b={(x,y), (a,b), (e,g)} Now a.union(b) = {(a,b), (c,d),(e,f), (x,y), (e,g)}
    qs_1 = Student.objects.values_list('name', 'city', named=True)
    qs_2 = Teacher.objects.values_list('name', 'city', named=True)

    std_obj = qs_1.union(qs_2) 
    # std_obj = qs_1.union(qs_2, all=True) # all=True দিলে সব গুলা দেখাবে।

    data = {
            'std_obj_value': std_obj,
            'SQL_querry': std_obj.query,
            'querry_title': "qs_1.union(qs_2)",
            'total_student': qs_1.count() + qs_2.count(),
            'total_obj': std_obj.count(),
            'descripetion': "qs_1 এবং qs_2 সবগুলো data এর  name যাদের মিল রয়েছে তাদের একবার নিয়ে এবং বাকি গুলোকে দেখাবে।  a = {(a,b), (c,d), (e,f)}  b={(x,y), (a,b), (e,g)} Now a.union(b) = {(a,b), (c,d),(e,f), (x,y), (e,g)}",
        }    
    return render(request, 'all_query.html', data)
#__________________________________________________________________________

#---------------------------------intersection()---------------------------
def intersection_name(request):
    # qs_1 এবং qs_2 data এর  name এর মধ্যে যে গুলো common আছে সেগুলো কে দেখাবে।
    # a = {4,5,6,7,8} b={1,2,3,4,5} Now a.intersection(b) = {4,5}
    qs_1 = Student.objects.values_list('name', named=True)
    qs_2 = Teacher.objects.values_list('name', named=True)

    std_obj = qs_1.intersection(qs_2)

    data = {
            'std_obj_value': std_obj,
            'SQL_querry': std_obj.query,
            'querry_title': "qs_1.intersection(qs_2)",
            'total_student': qs_1.count() + qs_2.count(),
            'total_obj': std_obj.count(),
            'descripetion': "qs_1 এবং qs_2 data এর  name এর মধ্যে যে গুলো common আছে সেগুলো কে দেখাবে।  a = {4,5,6,7,8} b={1,2,3,4,5} Now a.intersection(b) = {4,5}",
        }    
    return render(request, 'all_query.html', data)



def intersection_name_city(request):
    # qs_1 এবং qs_2 data এর  name এর মধ্যে যে গুলো common আছে সেগুলো কে দেখাবে।
    # a = {(a,b), (c,d), (e,f)}  b={(x,y), (a,b), (e,g)} Now a.intersection(b) = {(a,b)}
    qs_1 = Student.objects.values_list('name', 'city', named=True)
    qs_2 = Teacher.objects.values_list('name', 'city', named=True)

    std_obj = qs_1.intersection(qs_2)

    data = {
            'std_obj_value': std_obj,
            'SQL_querry': std_obj.query,
            'querry_title': "qs_1.intersection(qs_2)",
            'total_student': qs_1.count() + qs_2.count(),
            'total_obj': std_obj.count(),
            'descripetion': "qs_1 এবং qs_2 data এর  name এর মধ্যে যে গুলো common আছে সেগুলো কে দেখাবে।  a = {(a,b), (c,d), (e,f)}  b={(x,y), (a,b), (e,g)} Now a.intersection(b) = {(a,b)}",
        }    
    return render(request, 'all_query.html', data)
#__________________________________________________________________________

#---------------------------------difference()---------------------------
def difference_name(request):
    # qs_1 এবং qs_2 সবগুলো qs_1 থেকে qs_2 বাদ দিয়ে, যারা যারা আছে তাদের দেখাছে কারন আমরা qs_1.difference(qs_2) লিখেছি।
    # যদি qs_2.difference(qs_1) লিখতাম তবে, qs_2 থেকে qs_1 কে বাদ দিয়ে বাকি গুলাকে দেখাতো।
    # a = {4,5,6,7,8} b={1,2,3,4,5} Now a.intersection(b) = {6,7,8}
    qs_1 = Student.objects.values_list('name', named=True)
    qs_2 = Teacher.objects.values_list('name', named=True)

    std_obj = qs_1.difference(qs_2)

    data = {
            'std_obj_value': std_obj,
            'SQL_querry': std_obj.query,
            'querry_title': "qs_1.difference(qs_2)",
            'total_student': qs_1.count() + qs_2.count(),
            'total_obj': std_obj.count(),
            'descripetion': "qs_1 এবং qs_2 সবগুলো qs_1 থেকে qs_2 বাদ দিয়ে, যারা যারা আছে তাদের দেখাছে কারন আমরা qs_1.difference(qs_2) লিখেছি। যদি qs_2.difference(qs_1) লিখতাম তবে, qs_2 থেকে qs_1 কে বাদ দিয়ে বাকি গুলাকে দেখাতো।  a = {4,5,6,7,8} b={1,2,3,4,5} Now a.intersection(b) = {6,7,8}",
        }    
    return render(request, 'all_query.html', data)


def difference_name_city(request):
    # qs_1 এবং qs_2 সবগুলো data এর  name যাদের মিল রয়েছে তাদের বাদদিয়ে বাকি সবাইকে দেখাবে।
    # যদি qs_2.difference(qs_1) লিখতাম তবে, qs_2 থেকে qs_1 কে বাদ দিয়ে বাকি গুলাকে দেখাতো।
    # a = {(a,b), (c,d), (e,f)}  b={(x,y), (a,b), (e,g)} Now a.intersection(b) = {(c,d), (e,f)}
    qs_1 = Student.objects.values_list('name', 'city', named=True)
    qs_2 = Teacher.objects.values_list('name', 'city', named=True)

    std_obj = qs_1.difference(qs_2)

    data = {
            'std_obj_value': std_obj,
            'SQL_querry': std_obj.query,
            'querry_title': "qs_1.intersection(qs_2)",
            'total_student': qs_1.count() + qs_2.count(),
            'total_obj': std_obj.count(),
            'descripetion': "qs_1 এবং qs_2 সবগুলো qs_1 থেকে qs_2 বাদ দিয়ে, যারা যারা আছে তাদের দেখাছে কারন আমরা qs_1.difference(qs_2) লিখেছি। যদি qs_2.difference(qs_1) লিখতাম তবে, qs_2 থেকে qs_1 কে বাদ দিয়ে বাকি গুলাকে দেখাতো।  a = {(a,b), (c,d), (e,f)}  b={(x,y), (a,b), (e,g)} Now a.intersection(b) = {(c,d), (e,f)}",
        }    
    return render(request, 'all_query.html', data)
#__________________________________________________________________________











# ________________________________________________________________________________________________________________


def add_student(request):
    if request.method == 'POST':
        full_name = request.POST.get('full_name')
        roll      = request.POST.get('roll')
        date_of_birth = request.POST.get('date_of_birth')
        address   = request.POST.get('address')
        marks     = request.POST.get('marks')
        gread     = request.POST.get('gread')
        result     = request.POST.get('result')
        pass_date     = request.POST.get('pass_date')

        # print("---------------------------------")
        # print(f"Name = {full_name}, Roll = {roll}, Date of Birth = {date_of_birth}, Address = {address}, Marks = {marks}, Gread={gread}, Result={result} Pass_Date = {pass_date}")
        # print("---------------------------------")

        try:
            if not Student.objects.filter(roll = roll).exists():
                std = Student.objects.create(
                    name=full_name,
                    roll=roll,
                    date_of_birth=date_of_birth,
                    marks = marks,
                    result = result,
                    gread = gread,
                    city=address,
                    pass_date=pass_date
                )
                success_message = f"{std.name}'s record,s successfully added."
                messages.success(request, success_message)
                return redirect('home')
            else:
                messages.error(request, "This Roll number is allready exist.")
                return redirect('add_student')
        except ValueError:
            messages.error(request, "Please Fill Up Full Information.")
            return redirect('add_student')
        except ValidationError:
            messages.error(request, "Please Fill Up Valid Dete Field YYYY-MM-DD.")
            return redirect('add_student')
    
    return render(request, 'add.html')


def edit_student(request, id):
    try:
        std_obj = Student.objects.get(id = id)
        if request.method == 'POST':
            std_obj.name      = request.POST.get('full_name')
            std_obj.roll      = request.POST.get('roll')
            std_obj.date_of_birth = request.POST.get('date_of_birth')
            std_obj.city      = request.POST.get('address')
            std_obj.marks     = request.POST.get('marks')
            std_obj.gread     = request.POST.get('gread')
            std_obj.result    = request.POST.get('result')
            std_obj.pass_date = request.POST.get('pass_date')

            std_obj.save()
            # full_name = std_obj.get_fullname()
            full_name = std_obj.name
            success_message = f"{full_name}'s record successfully updated."
            messages.success(request, success_message)
            return redirect('home')
    except ObjectDoesNotExist:
        messages.error(request, 'This Student is not exist.')
        return redirect('home')

    data = {
        'std': std_obj,
    }
    return render(request, 'edit.html', data)


def delete_student(request):
    if request.method == 'POST' and 'delete' in request.POST:
        delete_id = request.POST.get('delete_id')
        try:
            std = Student.objects.get(id = delete_id)
            std.delete()
            success_message = f"{std.name}'s record is successfully Deleted."
            messages.warning(request, success_message)
            return redirect('home')
        except ObjectDoesNotExist:
            messages.error(request, 'This Student record does not exist.')
            return redirect('home')
