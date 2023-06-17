from django.shortcuts import render, redirect
from QuerySetAPI.models import Student, Teacher
from QuerySetAPI_4.models import Book, Author, Publisher, Store

from django.core.paginator import Paginator
from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist
from django.db import IntegrityError
from django.http import HttpResponse
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


    

    