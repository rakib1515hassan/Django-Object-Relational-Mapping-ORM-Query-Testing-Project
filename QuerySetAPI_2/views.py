from django.shortcuts import render, redirect
from QuerySetAPI.models import Student, Teacher

from django.db.models import Q
from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist
from django.db import IntegrityError
from django.http import HttpResponse
from datetime import datetime, date, time

# Create your views here.
def QuerySetAPI_2(request):
    return render(request, 'QuerySetAPI_2.html')

def test(request):
    return render(request, 'add_teacher.html')


#----------------------------------------------------------------------------------------------------------------------------
#------------------------first()---------------------------------
def first(request):   
    std_obj = Student.objects.first()  # If you want to see the first data of a table
    data = {
        'std_obj_get': std_obj,
        'SQL_querry': '',
        # 'SQL_querry': std_obj.query, #'Student' object has no attribute 'query'
        'total_student': Student.objects.all().count(),
        'querry_title': ".first()",
        'total_obj': 1,
        'descripetion': "If you want to see the first data of a table",
    }    
    return render(request, 'all_query.html', data)
#_______________________________________________________________
#------------------------last()---------------------------------
def last(request):   
    std_obj = Student.objects.last()  # If you want to see the last data of a table
    data = {
        'std_obj_get': std_obj,
        'SQL_querry': '',
        # 'SQL_querry': std_obj.query, # 'Student' object has no attribute 'query'
        'total_student': Student.objects.all().count(),
        'querry_title': ".last()",
        'total_obj': 1,
        'descripetion': "If you want to see the last data of a table",
    }    
    return render(request, 'all_query.html', data)
#_______________________________________________________________

#------------------------last()---------------------------------
def latest(request):   
    std_obj = Student.objects.latest('date_of_birth') # what was the last insurt data in a table, earliest() and latest() require
    # either fields as positional arguments so we given a argument that we can get a letest data.
    
    data = {
        'std_obj_get': std_obj,
        'SQL_querry': '',
        # 'SQL_querry': std_obj.query, # 'Student' object has no attribute 'query'
        'total_student': Student.objects.all().count(),
        'querry_title': ".latest('date_of_birth')",
        'total_obj': 1, # std_obj.count() is not work
        'descripetion': "what was the last insurt data in a table, earliest() and latest() require either fields as positional arguments so we given a argument that we can get a letest data.",
    }    
    return render(request, 'all_query.html', data)
#_______________________________________________________________

#------------------------earliest()---------------------------------
def earliest(request):   
    std_obj = Student.objects.earliest('date_of_birth') # last month এ কোন data insurt করা হয়েছে। 
    # earliest() and latest() require either fields as positional arguments so we given a argument that we can get a letest data.
    data = {
        'std_obj_get': std_obj,
        'SQL_querry': '',
        # 'SQL_querry': std_obj.query, # 'Student' object has no attribute 'query'
        'total_student': Student.objects.all().count(),
        'querry_title': ".latest('date_of_birth')",
        'total_obj': 1, # std_obj.count() is not work
        'descripetion': "last month এ কোন data insurt করা হয়েছে। earliest() and latest() require either fields as positional arguments so we given a argument that we can get a earliest data.",
    }    
    return render(request, 'all_query.html', data)
#_______________________________________________________________

#---------------------------CRUD---------------------------------
from django.forms.models import model_to_dict
import json
# from datetime import date

# NOTE If We want to see the data in HttpResponse
def get_or_create_http(request):
    # যদি এই same record টি আগেথাকতে database save থাকে তবে তাকে return করবে, আগেথাকতে save না থাকলে save করে return করবে।
    std_obj, created = Student.objects.get_or_create(
        name = "Abu Bokkor",
        roll = 5689,
        city = 'Chandpur',
        marks = 60,
        date_of_birth= '1998-05-06',
        pass_date = '2013-01-06'
        )

    """ NOTE যেহেতু এখানে Date field আছে তেই এইভাবে দেখনো যাবে না। অন্যথায় দেখানো যেতো।
        data = {
        'name': std_obj.name,
        'roll': std_obj.roll,
        'city': std_obj.city,
        'marks': std_obj.marks,
        'date_of_birth': std_obj.date_of_birth,
        'pass_date': std_obj.pass_date
        }
        json_data = json.dumps(data)  # Convert data to JSON format
    """

    """ NOTE model_to_dict(std_obj)
        std_data = model_to_dict(std_obj) 

        Return a dict containing the data in instance suitable for passing as a Form's initial keyword argument. fields is an optional
        list of field names. If provided, return only the named. exclude is an optional list of field names. If provided, exclude the
        named from the returned dict, even if they are listed in the fields argument.
    """ 
    """ NOTE When i create new data, face 'str' object has no attribute 'strftime' error, But created না হয়ে যখন শুধু fatch করে দেখায় তখন
        কোন error দেখায় না। তাই এটিকে না ব্যবহার করে নিচের টি ব্যবহার করা হয়েছে।

        std_data['date_of_birth'] = std_data['date_of_birth'].strftime('%Y-%m-%d')
        std_data['pass_date'] = std_data['pass_date'].strftime('%Y-%m-%d')
    """
    std_data = model_to_dict(std_obj)
    std_data['date_of_birth'] = std_data['date_of_birth'].strftime('%Y-%m-%d') if isinstance(
        std_data['date_of_birth'], date) else std_data['date_of_birth']
    
    std_data['pass_date'] = std_data['pass_date'].strftime('%Y-%m-%d') if isinstance(
        std_data['pass_date'], date) else std_data['pass_date']
    
    std_data['created_status'] = created
    json_data = json.dumps(std_data)
    return HttpResponse(json_data, content_type='application/json')


def get_or_create(request):
    if request.method == "POST":
        full_name = request.POST.get('full_name')
        roll      = request.POST.get('roll')
        date_of_birth = request.POST.get('date_of_birth')
        address   = request.POST.get('address')
        marks     = request.POST.get('marks')
        gread     = request.POST.get('gread')
        result     = request.POST.get('result')
        pass_date = request.POST.get('pass_date')

        # যদি এই same record টি আগেথাকতে database save থাকে তবে তাকে return করবে, আগেথাকতে save না থাকলে save করে return করবে।
        std_obj, created = Student.objects.get_or_create(
            name = full_name,
            roll = roll,
            city = address,
            marks = marks,
            gread = gread,
            result = result,
            date_of_birth= date_of_birth,
            pass_date = pass_date
            )
        if created == True:
            msg = full_name + " record is Created successfully."
            messages.success(request, msg)
            data = {
                'std_obj_get':std_obj,
                'SQL_querry': '',
                # 'SQL_querry': std_obj.query, # 'Student' object has no attribute 'query'
                'total_student': Student.objects.all().count(),
                'querry_title': ".get_or_create()",
                'total_obj': 1, # std_obj.count() is not work
                'descripetion': "",
            }
            return render(request, 'all_query.html', data)
        else:
            msg = full_name + " record are already have in database."
            messages.warning(request, msg)
            data = {
                'std_obj_get':std_obj,
                'SQL_querry': '',
                # 'SQL_querry': std_obj.query, # 'Student' object has no attribute 'query'
                'total_student': Student.objects.all().count(),
                'querry_title': ".get_or_create()",
                'total_obj': 1, # std_obj.count() is not work
                'descripetion': "",
            }
            return render(request, 'all_query.html', data)

    data = {
        'update':'update',
        'method': 'get_or_create',
    }
    return render(request, 'add.html', data)



def update(request, given_id):  
    # একটি বিষয় মনে রাখতে হবে যে .update() metheod কিন্তু .get() এর সাথে দেয়া যাবে না। তা invalid .
    # given_id = 1 
    try:
        std = Student.objects.filter(id = given_id).update(marks = 90, city = 'Lalbagh') # এটি update করে, কয়টি field কে সে পরিবর্তন ক্রেছে তা return করে।
        std_obj = Student.objects.get(id = given_id) # তাই সেই id দিয়ে আবার object টিকে আবার খুজে বের করা হয়েছে

        # আমরা চাইলে একাধিক data কেও এক সাথে update করতে পারি, 
        # std = Student.objects.filter(marks = 80).update( city = 'Dhaka')              
        
        data = {
            'std_obj_get': std_obj,
            'SQL_querry': '',
            # 'SQL_querry': std_obj.query, # 'Student' object has no attribute 'query'
            'total_student': Student.objects.all().count(),
            'querry_title': ".filter(id = 1).update(marks = 90, city = 'Lalbagh')",
            'total_obj': 1, # std_obj.count() is not work
            'descripetion': "যার id = 1 তার marks এবং city যাই থাকুক না কেন marks = 90, city = 'Lalbagh' বানিয়ে দিবে। তবে একটি বিষয় মনে রাখতে হবে যে .update() metheod কিন্তু .get() এর সাথে দেয়া যাবে না। তা invalid. আমরা চাইলে একাধিক data কেও এক সাথে update করতে পারি, যেমন যাদের mark =80 তাদের সবার city কে যদি Dhaka বানাতে চাই, Student.objects.filter(marks = 80).update( city = 'Dhaka')",
        }    
        return render(request, 'all_query.html', data)
    except Student.DoesNotExist:
        messages.error(request, "This Record is not exist in data base.")
        return redirect('home')



def update_or_create(request, given_id, given_name):
    try:
        std, created = Student.objects.update_or_create(pk=given_id, name= given_name,defaults={
            'name':"Md Hassan Ali",
            'date_of_birth': '1995-10-20',
            'pass_date': '2015-06-25',
            })

        if created == True:
            std_obj = Student.objects.filter(name = 'Md Hassan Ali').first()
            messages.success(request, "This Record Is Created.")
            data = {
                'std_obj_get':std_obj,
                'SQL_querry': '',
                # 'SQL_querry': std_obj.query, # 'Student' object has no attribute 'query'
                'total_student': Student.objects.all().count(),
                'querry_title': ".update_or_create()",
                'total_obj': 1, # std_obj.count() is not work
                'descripetion': "If given data is exist then update, else create.",
            }
            return render(request, 'all_query.html', data)
        else:
            std_obj = Student.objects.get(id = given_id)
            msg = std_obj.name + "Record is updated."
            messages.warning(request, msg)
            data = {
                'std_obj_get':std_obj,
                'SQL_querry': '',
                # 'SQL_querry': std_obj.query, # 'Student' object has no attribute 'query'
                'total_student': Student.objects.all().count(),
                'querry_title': ".update_or_create()",
                'total_obj': 1, # std_obj.count() is not work
                'descripetion': "If given data is exist then update, else create.",
            }
            return render(request, 'all_query.html', data)

    except IntegrityError:
        std_obj = Student.objects.get(id = given_id)
        messages.error(request, 'Your given name is not exist in this id. Give Correct name.')
        data = {
                'std_obj_get':std_obj,
                'SQL_querry': '',
                'total_student': Student.objects.all().count(),
                'querry_title': ".update_or_create()",
                'total_obj': 0,
                'descripetion': "Your given name is not exist in this id. Give Correct name.",
            }
        return render(request, 'all_query.html', data)



def bulk_create(request):   
    # এক সাথে অনেক গুলো data data base এ insurt কোরতে চাইলে,
    obj=[
        Student(name = 'mojnu',  roll = 1568, city = 'Chandpur', marks = 80, date_of_birth = '1996-11-30', pass_date = '2020-04-20'),
        Student(name = 'kalam',  roll = 5438, city = 'Chandpur', marks = 69, date_of_birth = '1996-11-30', pass_date = '2020-04-20'),
        Student(name = 'junaed', roll = 8761, city = 'Chandpur', marks = 55, date_of_birth = '1996-11-30', pass_date = '2020-04-20'),
        Student(name = 'rofik',  roll = 1458, city = 'Chandpur', marks = 76, date_of_birth = '1996-11-30', pass_date = '2020-04-20'),
    ]
    std_obj = Student.objects.bulk_create(obj)

    data = {
        'std_obj': std_obj,
        'SQL_querry': '',
        # 'SQL_querry': std_obj.query, # 'Student' object has no attribute 'query'
        'total_student': Student.objects.all().count(),
        'querry_title': ".bulk_create(obj)",
        'total_obj': '', ## std_obj.count()
        'descripetion': "জতবার click করা হবে তত বার save data create হয়ে যাবে। সুতরাং বার বার click করা যাবে না।",
    }    
    return render(request, 'all_query.html', data)


 # all_student_data=Student.objects.all()
    
    # for std in all_student_data:
    #     std.std_Dept = "BSC in CSE"    
    # student_data=Student.objects.bulk_update(all_student_data,['std_Dept'])    
    
    # student_data=Student.objects.in_bulk([1,2])
    
    student_data=Student.objects.in_bulk()
    
    # print(student_data[1].std_name)

    # std_obj.save(force_insert=True) # Force করে যদি কোন data ডুকাতে চাই।
#_______________________________________________________________






def QuerySetAPI_3(request):
    return render(request, 'QuerySetAPI_3.html')

#----------------------- Field Lookups -------------------------
def exact_mark(request):
    std_obj = Student.objects.filter(marks__exact = 50) 
    data = {
            'std_obj': std_obj,
            'SQL_querry': std_obj.query,
            'querry_title': ".filter(marks__exact = 50)",
            'total_student': Student.objects.all().count(),
            'total_obj': std_obj.count(),
            'descripetion': "যাদের Mark 50 ( mark = 50 ) তাদের দেখাবে। এটি যদি নাম হতো তবে আমাদের exact value দেয়া লাগতো, কারন এটি Case Sensitive",
        }    
    return render(request, 'all_query.html', data)


def less_then_mark(request):
    std_obj = Student.objects.filter(marks__lt = 50) 
    data = {
            'std_obj': std_obj,
            'SQL_querry': std_obj.query,
            'querry_title': ".filter(marks__lt = 50)",
            'total_student': Student.objects.all().count(),
            'total_obj': std_obj.count(),
            'descripetion': "যাদের Mark 50 এর কম ( mark < 50 ) তাদের দেখাবে।",
        }    
    return render(request, 'all_query.html', data)

def less_then_or_equeal(request):
    std_obj = Student.objects.filter(marks__lte = 50)
    data = {
            'std_obj': std_obj,
            'SQL_querry': std_obj.query,
            'querry_title': ".filter(marks__lte = 50)",
            'total_student': Student.objects.all().count(),
            'total_obj': std_obj.count(),
            'descripetion': "যাদের Mark 50 এর সামান কিংবা এর কম ( mark <= 50 ) তাদের দেখাবে।",
        }    
    return render(request, 'all_query.html', data)


def getter_then_mark(request):
    std_obj = Student.objects.filter(marks__gt = 50) 
    data = {
            'std_obj': std_obj,
            'SQL_querry': std_obj.query,
            'querry_title': ".filter(marks__gt = 50)",
            'total_student': Student.objects.all().count(),
            'total_obj': std_obj.count(),
            'descripetion': "যাদের Mark 50 এর বেশি ( mark > 50 ) তাদের দেখাবে।",
        }    
    return render(request, 'all_query.html', data)


def getter_then_or_equeal(request):
    std_obj = Student.objects.filter(marks__gte = 50)
    data = {
            'std_obj': std_obj,
            'SQL_querry': std_obj.query,
            'querry_title': ".filter(marks__gte = 50)",
            'total_student': Student.objects.all().count(),
            'total_obj': std_obj.count(),
            'descripetion': "যাদের Mark 50 এর সামান কিংবা এর বেশি ( mark >= 50 ) তাদের দেখাবে।",
        }    
    return render(request, 'all_query.html', data)


def exact_name(request):
    std_obj = Student.objects.filter(name__exact = 'Md Rakib Hassan') 
    data = {
            'std_obj': std_obj,
            'SQL_querry': std_obj.query,
            'querry_title': ".filter(name__exact = 'Md Rakib Hassan')",
            'total_student': Student.objects.all().count(),
            'total_obj': std_obj.count(),
            'descripetion': "এখানে যেহেতু exact দ্বারা filter করা হয়েছে,এবং এটি Case Sensitive। তাই আমাদের exact value দেয়া লাগবে।",
        }    
    return render(request, 'all_query.html', data)


def iexact_name(request):
    std_obj = Student.objects.filter(name__iexact = 'md rakib hassan') 
    data = {
            'std_obj': std_obj,
            'SQL_querry': std_obj.query,
            'querry_title': ".filter(name__iexact = 'md rakib hassan')",
            'total_student': Student.objects.all().count(),
            'total_obj': std_obj.count(),
            'descripetion': "এখানে যেহেতু iexact দ্বারা filter করা হয়েছে,এবং এটি Case Sensitive না, তাই কাছা কাছি পেলে সে Output দিবে।",
        }    
    return render(request, 'all_query.html', data)


def contains_name(request):
    std_obj = Student.objects.filter(name__contains = 'md') 
    data = {
            'std_obj': std_obj,
            'SQL_querry': std_obj.query,
            'querry_title': ".filter(name__contains = 'md')",
            'total_student': Student.objects.all().count(),
            'total_obj': std_obj.count(),
            'descripetion': "নামের মধ্যে যেখানে যেখানে md পাবে ঐ সকল record গুলোকে দেখাবে ,এবং এটি Case Sensitive না। তবে কিছু কিছু Database এ প্রবলেম করতে পারে, তাই icontains user করা যেতে পারে।",
        }    
    return render(request, 'all_query.html', data)


def icontains_name(request):
    std_obj = Student.objects.filter(name__icontains = 'md') 
    data = {
            'std_obj': std_obj,
            'SQL_querry': std_obj.query,
            'querry_title': ".filter(name__icontains = 'md')",
            'total_student': Student.objects.all().count(),
            'total_obj': std_obj.count(),
            'descripetion': "নামের মধ্যে যেখানে যেখানে md পাবে ঐ সকল record গুলোকে দেখাবে ,এবং এটি Case Sensitive না।",
        }    
    return render(request, 'all_query.html', data)


def id_in(request):
    std_obj = Student.objects.filter( id__in = [1, 3, 4, 9, 10, 19, 4444 ] ) 
    data = {
            'std_obj': std_obj,
            'SQL_querry': std_obj.query,
            'querry_title': ".filter(id__in = [1, 3, 4, 9, 10, 19, 4444])",
            'total_student': Student.objects.all().count(),
            'total_obj': std_obj.count(),
            'descripetion': "যাদের id 1, 3, 4, 9, 10, 19, 4444 তাদেরকে দেখাবে। এমন কোন id যদি থাকে যা data base exist করে না, সেগুলোকে দেখাবে না। তবে এ ক্ষেত্রে কোন error দেখাবে না। যেমন এখানে 4444 id টি data base এ নেই। তাও এখানে কোন error দেখাছে না।",
        }    
    return render(request, 'all_query.html', data)


def marks_in(request):
    std_obj = Student.objects.filter( marks__in = [ 31, 32 ] ) 
    data = {
            'std_obj': std_obj,
            'SQL_querry': std_obj.query,
            'querry_title': ".filter( marks__in = [ 31, 32 ] )",
            'total_student': Student.objects.all().count(),
            'total_obj': std_obj.count(),
            'descripetion': "যাদের marks 31, 32 তাদেরকে দেখাবে। এমন কোন marks যদি থাকে যা data base exist করে না, সেগুলোকে দেখাবে না। তবে এ ক্ষেত্রে কোন error দেখাবে না। ",
        }    
    return render(request, 'all_query.html', data)


def startswith_name(request):
    std_obj = Student.objects.filter( name__startswith = 'A' ) 
    data = {
            'std_obj': std_obj,
            'SQL_querry': std_obj.query,
            'querry_title': ".filter( name__startswith = 'A' )",
            'total_student': Student.objects.all().count(),
            'total_obj': std_obj.count(),
            'descripetion': "'A' দিয়ে যাদের নাম শুরু হয়েছে তাদের দেখাবে, এটি case sensitive । তবে কিছু কিছু data base case insensitive দেখায়। যেমন sqlite3 তা কাজ করছে না। এখানে 'a' দিয়ে যাদের name start হয়েছে তাদের ও দেখায়।",
        }    
    return render(request, 'all_query.html', data)


def istartswith_name(request):
    std_obj = Student.objects.filter( name__istartswith = 'A' ) 
    data = {
            'std_obj': std_obj,
            'SQL_querry': std_obj.query,
            'querry_title': ".filter( name__istartswith = 'A' )",
            'total_student': Student.objects.all().count(),
            'total_obj': std_obj.count(),
            'descripetion': " 'a' বা 'A' দিয়ে যাদের নাম শুরু হয়েছে তাদের দেখাবে, এটি case insensitive ।",
        }    
    return render(request, 'all_query.html', data)

def endswith_name(request):
    std_obj = Student.objects.filter( name__endswith = 'N' ) 
    data = {
            'std_obj': std_obj,
            'SQL_querry': std_obj.query,
            'querry_title': ".filter( name__endswith = 'N' )",
            'total_student': Student.objects.all().count(),
            'total_obj': std_obj.count(),
            'descripetion': " 'N' দিয়ে যাদের নাম শেষ হয়েছে তাদের দেখাবে, এটি case sensitive । তবে কিছু কিছু data base case insensitive দেখায়। যেমন sqlite3 তা কাজ করছে না। এখানে 'n' দিয়ে যাদের name শেষ হয়েছে তাদের ও দেখায়।",
        }    
    return render(request, 'all_query.html', data)


def iendswith_name(request):
    std_obj = Student.objects.filter( name__iendswith = 'N' ) 
    data = {
            'std_obj': std_obj,
            'SQL_querry': std_obj.query,
            'querry_title': ".filter( name__iendswith = 'N' )",
            'total_student': Student.objects.all().count(),
            'total_obj': std_obj.count(),
            'descripetion': " 'n' বা 'N' দিয়ে যাদের নাম শেষ হয়েছে তাদের দেখাবে, এটি case insensitive ।",
        }    
    return render(request, 'all_query.html', data)


def range_marks(request):
    std_obj = Student.objects.filter( marks__range = ( 33 , 100 )) # YYYY-MM-DD
    data = {
            'std_obj': std_obj,
            'SQL_querry': std_obj.query,
            'querry_title': ".filter( marks__range = ( 33 , 100 ) )",
            'total_student': Student.objects.all().count(),
            'total_obj': std_obj.count(),
            'descripetion': "যাদের Marks 33 থেকে 100 এর ভেতর তাদের দেখাবে।",
        }    
    return render(request, 'all_query.html', data)
#_______________________________________________________________


#-------------------- Time and Date ----------------------------

def range_birthOFdate(request):
    std_obj = Student.objects.filter( date_of_birth__range = ('2000-01-01' , '2023-12-30') ) # YYYY-MM-DD
    data = {
            'std_obj': std_obj,
            'SQL_querry': std_obj.query,
            'querry_title': ".filter( date_of_birth__range = ('2000-01-01' , '2023-12-31') )",
            'total_student': Student.objects.all().count(),
            'total_obj': std_obj.count(),
            'descripetion': "যাদের জন্ম 2000-January-01 থেকে 2023-December-31 এর ভেতর তাদের দেখাবে।",
        }    
    return render(request, 'all_query.html', data)


def date_join(request):
    techer_obj = Teacher.objects.filter( join__date = date(2015, 11, 14)) # YYYY-MM-DD
    data = {
            'techer_obj': techer_obj,
            'SQL_querry': techer_obj.query,
            'querry_title': ".filter( join__date = date(2015, 11, 14) )",
            'total_student': Teacher.objects.all().count(),
            'total_obj': techer_obj.count(),
            'descripetion': "যার Joining Date 2015 December 14 তার data দেখাবে। এখানে exect date দিতে হবে এবং Database অবশ্যই DateTimeField হতে হবে, এবং setting.py ফাইল এ TIME_ZONE = 'Asia/Dhaka' দিতে হবে, এবং from datetime import date করতে হবে।",
        }    
    return render(request, 'all_query.html', data)


def date_join_lessthen(request):
    techer_obj = Teacher.objects.filter( join__date__lt = date(2015, 11, 14)) # YYYY-MM-DD
    data = {
            'techer_obj': techer_obj,
            'SQL_querry': techer_obj.query,
            'querry_title': ".filter( join__date__lt = date(2015, 11, 14) )",
            'total_student': Teacher.objects.all().count(),
            'total_obj': techer_obj.count(),
            'descripetion': "2015 December 14 এর আগে যারা join করেছে তাদের দেখাবে।",
        }    
    return render(request, 'all_query.html', data)

def date_join_geterthen(request):
    techer_obj = Teacher.objects.filter( join__date__gt = date(2015, 11, 14)) # YYYY-MM-DD
    data = {
            'techer_obj': techer_obj,
            'SQL_querry': techer_obj.query,
            'querry_title': ".filter( join__date__gt = date(2015, 11, 14) )",
            'total_student': Teacher.objects.all().count(),
            'total_obj': techer_obj.count(),
            'descripetion': "2015 December 14 এর পরে যারা join করেছে তাদের দেখাবে।",
        }    
    return render(request, 'all_query.html', data)


def date_join_geterthen_equel(request):
    techer_obj = Teacher.objects.filter( join__date__gte = date(2015, 11, 14)) # YYYY-MM-DD
    data = {
            'techer_obj': techer_obj,
            'SQL_querry': techer_obj.query,
            'querry_title': ".filter( join__date__gte = date(2015, 11, 14) )",
            'total_student': Teacher.objects.all().count(),
            'total_obj': techer_obj.count(),
            'descripetion': "2015 December 14 এর পরে কিংবা ঐ date যারা join করেছে তাদের দেখাবে।",
        }    
    return render(request, 'all_query.html', data)


def year_pass(request):
    std_obj = Student.objects.filter(pass_date__year = 2015) # YYYY
    data = {
            'std_obj': std_obj,
            'SQL_querry': std_obj.query,
            'querry_title': ".filter( pass_date__year = 2015 )",
            'total_student': Student.objects.all().count(),
            'total_obj': std_obj.count(),
            'descripetion': "2015 সালে যারা যারা পাশ করেছে তাদের দেখানো হয়েছে ।",
        }    
    return render(request, 'all_query.html', data)

def year_pass__lte(request):
    std_obj = Student.objects.filter(pass_date__year__lte = 2015) # YYYY
    data = {
            'std_obj': std_obj,
            'SQL_querry': std_obj.query,
            'querry_title': ".filter( pass_date__year__lte = 2015 )",
            'total_student': Student.objects.all().count(),
            'total_obj': std_obj.count(),
            'descripetion': "2015 সালে কিংবা তার আগে যারা যারা পাশ করেছে তাদের দেখানো হয়েছে ।",
        }    
    return render(request, 'all_query.html', data)


def month_pass__lte(request):
    std_obj = Student.objects.filter(pass_date__month__lte = 2) # Month <= 2
    data = {
            'std_obj': std_obj,
            'SQL_querry': std_obj.query,
            'querry_title': ".filter( pass_date__month__lte = 2 )",
            'total_student': Student.objects.all().count(),
            'total_obj': std_obj.count(),
            'descripetion': " February কিংবা এর আগের (January) মাসে যাদের Result Publish হয়েছে তাদের সবার data দেখাবে।",
        }    
    return render(request, 'all_query.html', data)



def day_pass__lte(request):
    std_obj = Student.objects.filter(pass_date__day__lte = 5) # Day <= 25
    data = {
            'std_obj': std_obj,
            'SQL_querry': std_obj.query,
            'querry_title': ".filter( pass_date__day__lte = 5 )",
            'total_student': Student.objects.all().count(),
            'total_obj': std_obj.count(),
            'descripetion': "যাদের Result Publish এর দিন 5 তারিক কিংবা তার আগে ছিল তাদের সবার data দেখাবে",
        }    
    return render(request, 'all_query.html', data)


def week_pass__lte(request):
    # 1 Year = 12*4 = 48 কিংবা তার থেকে বেশি ইয়ে থাকে।
    std_obj = Student.objects.filter(pass_date__week__lte = 13)  # 13/4 = 3 month 7 days so, 3 month +
    data = {
            'std_obj': std_obj,
            'SQL_querry': std_obj.query,
            'querry_title': ".filter( pass_date__week__lte = 13 )",
            'total_student': Student.objects.all().count(),
            'total_obj': std_obj.count(),
            'descripetion': "যাদের Result Publish 13 Week কিংবা তার আগে হয়েছিল তাদের সবার data দেখাবে। ( 13 week = 3 month + so, 4 month 7 day এর আগে যাদের result publish হয়েছে তাদের data দেখাবে।)",
        }    
    return render(request, 'all_query.html', data)


def week_day_pass(request):
    # Sunday=1, Monday=2, Tuesday=3, Wednesday=4, Thursday=5, Friday=6, Saturday=7
    std_obj = Student.objects.filter(pass_date__week_day = 1) # So This is Sunday
    data = {
            'std_obj': std_obj,
            'SQL_querry': std_obj.query,
            'querry_title': ".filter( pass_date__week_day = 1 )",
            'total_student': Student.objects.all().count(),
            'total_obj': std_obj.count(),
            'descripetion': "এখানে pass_date__week_day = 1 বলতে, যাদের Result Publish এর দিন Sunday ছিল তাকে বুজানো হয়েছে। Sunday=1, Monday=2, Tuesday=3, Wednesday=4, Thursday=5, Friday=6, Saturday=7)",
        }    
    return render(request, 'all_query.html', data)


def week_day_pass__lte(request):
    # Sunday=1, Monday=2, Tuesday=3, Wednesday=4, Thursday=5, Friday=6, Saturday=7
    std_obj = Student.objects.filter(pass_date__week_day__lte = 2) # So This is Sunday
    data = {
            'std_obj': std_obj,
            'SQL_querry': std_obj.query,
            'querry_title': ".filter( pass_date__week__lte = 13 )",
            'total_student': Student.objects.all().count(),
            'total_obj': std_obj.count(),
            'descripetion': "এখানে pass_date__week_day__lte = 2 বলতে, যাদের Result Publish এর দিন Monday, কিংবা তার আগে(Sunday,Monday) ছিল তাকে বুজানো হয়েছে। Sunday=1, Monday=2, Tuesday=3, Wednesday=4, Thursday=5, Friday=6, Saturday=7)",
        }    
    return render(request, 'all_query.html', data)


def quarter_pass(request):
    # 1 Year = 4 Quarter. So, (1 Quarter = (January, February, March), 2 Quarter = (April, May, Jun),
    # 3 Quarter = (Jyly, Augest, Septamber), 4 Quarer = (October, November, December))
    # NOTE এটি DateField and DateTimeField উভয় এর সাথে work করে।
    std_obj = Student.objects.filter(pass_date__quarter = 1) # 1 Quarter = (January, February, March)
    data = {
            'std_obj': std_obj,
            'SQL_querry': std_obj.query,
            'querry_title': ".filter( pass_date__quarter = 1 )",
            'total_student': Student.objects.all().count(),
            'total_obj': std_obj.count(),
            'descripetion': "1 Year = 4 Quarter (1 Quarter = (January, February, March), 2 Quarter = (April, May, Jun), 3 Quarter = (Jyly, Augest, Septamber), 4 Quarer = (October, November, December)). NOTE এটি DateField and DateTimeField উভয় এর সাথে work করে।",
        }    
    return render(request, 'all_query.html', data)


def time_join(request):
    # NOTE এটি শুধু মাত্র DateTimeField এর সাথে work করে।
    techer_obj = Teacher.objects.filter( join__time__gt = time(13, 00) ) # 13:00pm means, 1:00 pm এর পর যারা যারা join করেছে
    data = {
            'techer_obj': techer_obj,
            'SQL_querry': techer_obj.query,
            'querry_title': ".filter( join__time__gt = time(13, 00) )",
            'total_student': Teacher.objects.all().count(),
            'total_obj': techer_obj.count(),
            'descripetion': "13:00pm means, 1:00 pm এর পর যারা যারা join করেছে। NOTE এটি শুধু মাত্র DateTimeField এর সাথে work করে।",
        }    
    return render(request, 'all_query.html', data)


def hour_join(request):
    # NOTE এটি শুধু মাত্র DateTimeField এর সাথে work করে।
    techer_obj = Teacher.objects.filter( join__hour__lt = 12 ) # 1 day = 24 hour, 12 hour means দুপুর ১২ টার আগে যারা joid করেছে।
    data = {
            'techer_obj': techer_obj,
            'SQL_querry': techer_obj.query,
            'querry_title': ".filter( join__hour__lt = 12 )",
            'total_student': Teacher.objects.all().count(),
            'total_obj': techer_obj.count(),
            'descripetion': "1 day = 24 hour, 12 hour means দুপুর ১২ টার আগে যারা joid করেছে। NOTE এটি শুধু মাত্র DateTimeField এর সাথে work করে।",
        }    
    return render(request, 'all_query.html', data)


def minute_join(request):
    # NOTE এটি শুধু মাত্র DateTimeField এর সাথে work করে।
    techer_obj = Teacher.objects.filter( join__minute__lt = 30 ) # প্রতি ঘণ্টায় ৩০ মিনিট এর আগে যারা join করেছে তাদের দেখাবে।
    data = {
            'techer_obj': techer_obj,
            'SQL_querry': techer_obj.query,
            'querry_title': ".filter( join__minute__lt = 30 )",
            'total_student': Teacher.objects.all().count(),
            'total_obj': techer_obj.count(),
            'descripetion': "প্রতি ঘণ্টায় ৩০ মিনিট এর আগে যারা join করেছে তাদের দেখাবে। NOTE এটি শুধু মাত্র DateTimeField এর সাথে work করে।",
        }    
    return render(request, 'all_query.html', data)



def second_join(request):
    # NOTE এটি শুধু মাত্র DateTimeField এর সাথে work করে।
    techer_obj = Teacher.objects.filter( join__second__lt = 30 ) # প্রতি মিনিটে ৩০ second এর আগে যারা join করেছে তাদের দেখাবে।
    data = {
            'techer_obj': techer_obj,
            'SQL_querry': techer_obj.query,
            'querry_title': ".filter( join__second__lt = 50 )",
            'total_student': Teacher.objects.all().count(),
            'total_obj': techer_obj.count(),
            'descripetion': "প্রতি মিনিটে ৩০ second এর আগে যারা join করেছে তাদের দেখাবে। এটি ভালো কাজ করে যখন আমরা টাইম টি auto now add করি তখন। NOTE এটি শুধু মাত্র DateTimeField এর সাথে work করে।",
        }    
    return render(request, 'all_query.html', data)



#_______________________________________________________________
#____________________________________________________________________________________________________________________________


