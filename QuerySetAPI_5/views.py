from django.shortcuts import render, redirect
from QuerySetAPI.models import Student, Teacher
from QuerySetAPI_4.models import Book, Author, Publisher, Store

from django.core.paginator import Paginator
from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist
from django.db import IntegrityError
from django.http import HttpResponse, HttpRequest
from datetime import datetime, date, time

from django.db.models import Q, F, Value, FloatField
from django.db.models.aggregates import Avg, Max, Min, Count, Sum

# Create your views here.
def QuerySetAPI_5(request):
    return render(request, 'QuerySetAPI_5.html')


def Q_marks(request):
    std_obj = Student.objects.filter(Q(marks__gte = 33) & Q(marks__lt = 50))
    data = {
        'std_obj': std_obj,

        'SQL_querry': std_obj.query, #'Student' object has no attribute 'query'
        'total_student': Student.objects.all().count(),
        'querry_title': ".filter(Q(marks__gte = 33) & Q(marks__lt = 50))",
        'total_obj': std_obj.count(),
        'descripetion': "The records of those who scored 33 to 49 in the exam are displayed here.",
    }    
    return render(request, 'all_query.html', data)


def Q_book_publisher(request):
    book = Book.objects.filter(Q(publisher__name__exact='Jupiter Book House') | Q(publisher__name__exact='Onupom Book House'))

    data = {
        'book': book,

        'SQL_querry': book.query,
        'total_student': Book.objects.all().count(),
        'querry_title': ".filter(Q(publisher__name__exact='Jupiter Book House') | Q(publisher__name__exact='Onupom Book House'))",
        'total_obj': book.count(),
        'descripetion': "এখানে দেখানো হয়েছে ঐ সকল Book যার Publisher ছিলো 'Jupiter Book House অথবা 'Onupom Book House'.",
    }    
    return render(request, 'all_query.html', data)


def Q_storage_book_auther(request):
    storage = Store.objects.filter(Q(books__authors__name__iexact='Mr Rakib') & Q(books__price__exact = 150))
    
    """NOTE যদি আমরা get_author এর মাধ্যমে author কে না বের করে view function এ বেরকরতে চাই তবে এই ভাবে করতে হবে।
    storage = Store.objects.filter(Q(books__authors__name__iexact='Mr Rakib') & Q(books__price__exact = 150)).first()
    authors = []
    for book in storage.books.all():
        authors.extend(book.authors.all())
    author_names = ", ".join([author.name for author in authors])

    print(author_names)

    """
    data = {
        'storage': storage,

        'SQL_querry': storage.query,
        'total_student': Book.objects.all().count(),
        'querry_title': "Q(books__authors__name__iexact='Mr Rakib') & Q(books__price__exact = 150))",
        'total_obj': storage.count(),
        'descripetion': "একট বাই যার Author = 'Mr Rakib' এবং এর Price = 150 টাকা, এটি কোন Storage এ আছে তা এখানে দেখানো হয়েছে । তার পাশা পাশি এখানে দেখানো হয়েছে তাদের এখানে কোন কোন Author এর Book আছে এবং Book গুলোর নামে কি, এবং কোন কোন Publisher এর Book তারা Store করে।",
    }    
    return render(request, 'all_query.html', data)

    


from django.views import View
class FilteredBooksView(View):
    def get(self, request):
        # Get the authors with names 'a' and 'b'
        authors = Author.objects.filter(name__in=['Mr Rakib', 'Md Rasel'])
        
        # Get the books that have only the authors 'a' and 'b'
        books = Book.objects.filter(authors__in=authors).exclude(authors__in=Author.objects.exclude(name__in=['Mr Rakib', 'Md Rasel']))
        
        # Exclude books that have any other authors
        for author in authors:
            books = books.filter(authors=author)

        books = books.distinct()  # Eliminate duplicates
        

        data = {
            'book': books,

            'SQL_querry': books.query,
            'total_student': Book.objects.all().count(),
            'querry_title': "authors = Author.objects.filter(name__in=['Mr Rakib', 'Md Rasel']) and Book.objects.filter(authors__in=authors).exclude(authors__in=Author.objects.exclude(name__in=['Mr Rakib', 'Md Rasel']))",
            'total_obj': books.count(),
            'descripetion': "আমার কাছে 2টি বই আছে একটির নাম x এবং অন্যটির নাম y. x এর লেখক a এবং b, এবং আরেকটি বই y এর লেখক a,b, এবং c. এখন আমি ফিল্টার করতে চাই, যেই book এর  লেখক শুধুমাত্র a এবং b, আর কেউ নয়, সেই বইটির query set.",
        }    
        return render(request, 'all_query.html', data)
    



def Q_book__auther(request):
    # list_of_authors = ['Mr Rakib', 'Md Hassan', 'Tanin']
    # list_of_authors = ['Md Rasel', 'Tanin']
    # list_of_authors = ['a', 'b']
    list_of_authors = ['a', 'b', 'c']

    # Get the authors with names 'a' and 'b' এখানে Given author দের filter করে বের করা হয়েছে।
    authors = Author.objects.filter(name__in = list_of_authors)


    # Get the books that have only the authors 'a' and 'b'
    books = Book.objects.filter(authors__in=authors).exclude(authors__in=Author.objects.exclude(name__in = list_of_authors))

    # Exclude books that have any other authors ( author a,b,c book = y এবং author a,b = x,  এবং author a,c = z)
    # নিচের for loop টি যদি না দেই, তবে এর result আসবে <QuerySet [<Book: x>, <Book: y>, <Book: z>]>
    # এখানে ঐ সকল book কে বাদ দেয়া হয়েছে, author a,b = x,  এবং author a,c = z তবে correct result আসবে <QuerySet [<Book: y>]>
    for author in authors:
        books = books.filter(authors=author)

    books = books.distinct()  # Eliminate duplicates

    # print("--------------------")
    # print(authors)
    # print(books)
    # print("--------------------")

    data = {
        'book': books,

        'SQL_querry': books.query,
        'total_student': Book.objects.all().count(),
        'querry_title': "authors = Author.objects.filter(name__in=['Mr Rakib', 'Md Rasel']) and Book.objects.filter(authors__in=authors).exclude(authors__in=Author.objects.exclude(name__in=['Mr Rakib', 'Md Rasel']))",
        'total_obj': books.count(),
        'descripetion': "আমার কাছে 2টি বই আছে একটির নাম x এবং অন্যটির নাম y. x এর লেখক a এবং b, এবং আরেকটি বই y এর লেখক a,b, এবং c. এখন আমি ফিল্টার করতে চাই, যেই book এর  লেখক শুধুমাত্র a এবং b, আর কেউ নয়, সেই বইটির query set.",
    }    
    return render(request, 'all_query.html', data)





def Q_book__name_price(request):
    
    book_name = 'python'
    min_price = 400
    max_price = 600

    books = Book.objects.filter( Q(name__icontains = book_name) & (Q( price__gt = min_price) & Q( price__lt = max_price)) )


    data = {
        'book': books,

        'SQL_querry': books.query,
        'total_student': Book.objects.all().count(),

        'querry_title': "Book.objects.filter( Q(name__icontains = book_name) & (Q( price__gt = min_price) & Q( price__lt = max_price)) )",
        'total_obj': books.count(),
        'descripetion': "বই এর নাম python এবং এর price min > 400 এবং max price  < 600 এমন book কোনটি ?",
    }    
    return render(request, 'all_query.html', data)


def Q_book__name_price_2(request):
    
    book_name = 'python'
    min_price = 500
    max_price = 1000

    books = Book.objects.filter( Q(name__icontains = book_name) & (Q( price__gt = min_price) & Q( price__lt = max_price)) )

    data = {
        'book': books,

        'SQL_querry': books.query,
        'total_student': Book.objects.all().count(),

        'querry_title': "Book.objects.filter( Q(name__icontains = book_name) & (Q( price__gt = min_price) & Q( price__lt = max_price)) )",

        'total_obj': books.count(),

        'descripetion': "বই এর নাম python এবং এর price min > 500 এবং max price  < 1000 এমন book কোনটি ?",
    }    
    return render(request, 'all_query.html', data)


def student__not_pass(request):
    
    status = 'Pass'

    std_obj = Student.objects.filter( ~Q(result__exact = status) )
    print("--------------------")
    print(std_obj)
    print("--------------------")
   
    data = {
        'std_obj': std_obj,

        'SQL_querry': std_obj.query, #'Student' object has no attribute 'query'
        'total_student': Student.objects.all().count(),
        'querry_title': ".filter( ~Q(result__exact = status) )",
        'total_obj': std_obj.count(),
        'descripetion': "যে সকল student pass করে নি।",
    }    
    return render(request, 'all_query.html', data)


def student__city_pass(request):
    
    city = 'Dhaka'
    status = 'Pass'
    # std_obj = Student.objects.filter(Q(city__icontains = city) & Q(result__exact = status))
    std_obj = Student.objects.filter( Q(city__icontains = city) & (~Q(result__exact = status)) )
   
    data = {
        'std_obj': std_obj,

        'SQL_querry': std_obj.query, #'Student' object has no attribute 'query'
        'total_student': Student.objects.all().count(),
        'querry_title': ".filter( Q(city__icontains = city) & (~Q(result__exact = status)) )",
        'total_obj': std_obj.count(),
        'descripetion': "Studen দের city = Dhaka এবং তারা pass করে নি।",
    }    
    return render(request, 'all_query.html', data)







# def filtered_books_view(request):
#     # Get the authors with names 'Mr Rakib' and 'Md Rasel'
#     authors = Author.objects.filter(name__in=['Mr Rakib', 'Md Rasel'])

#     # Get the books that have only the authors 'Mr Rakib' and 'Md Rasel'
#     books = Book.objects.filter(authors__in=authors).exclude(~Q(authors__name__in=['Mr Rakib', 'Md Rasel'])).distinct()





def test_auth(request):
    # auth_list = ['a', 'b', 'c']
    auth_list = ['a', 'b']

    authors = Author.objects.filter(name__in = auth_list)

    # books = Book.objects.filter( Q(authors__name__iexact = 'a, b') )
    # books = Book.objects.filter( Q(authors__name__in = 'a') | Q(authors__name__in = 'b') )
    books = Book.objects.annotate(authors_count=Count('authors')).filter( Q(authors__name__in = 'a') & Q(authors__name__in ='b') & Q(authors_count=2) )


    print("---------------------------------")
    print(books)
    print("---------------------------------")

    # for book in books:
    #     print("---------------------------------")
    #     print(book)
    #     print("---------------------------------")

    return HttpResponse('test')
    