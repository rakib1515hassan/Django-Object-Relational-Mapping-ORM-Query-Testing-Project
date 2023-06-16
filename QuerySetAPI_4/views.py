from django.shortcuts import render, redirect
from QuerySetAPI.models import Student, Teacher
from QuerySetAPI_4.models import Book, Author, Publisher, Store

from django.core.paginator import Paginator
from django.db.models import Q
from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist
from django.db import IntegrityError
from django.http import HttpResponse
from datetime import datetime, date, time

from django.db.models import Q, F, Value, FloatField
from django.db.models.aggregates import Avg, Max, Min, Count, Sum

# Create your views here.

def QuerySetAPI_4(request):
    stu_obj = Student.objects.all().order_by('roll')

    """
        Book.objects.aggregate(average_price = Avg("price"))
        Result:- {'average_price': 34.35}
    """

    """
        Book.objects.aggregate(Avg("price"), Max("price"), Min("price"))
        Result:- {'price__avg': 34.35, 'price__max': Decimal('81.20'), 'price__min': Decimal('12.99')}
    """

    # average = stu_obj.aggregate(Avg('marks'))['marks__avg']
    average = Student.objects.aggregate(Avg('marks'))['marks__avg'] # উপরের টা এবং এটি একই

    # total = stu_obj.aggregate(Sum('marks'))['marks__sum']
    total = Student.objects.aggregate(Sum('marks'))['marks__sum']   # উপরের টা এবং এটি একই

    # minimum = stu_obj.aggregate(Min('marks'))['marks__min']
    minimum = Student.objects.aggregate(Min('marks'))['marks__min']  # উপরের টা এবং এটি একই

    # maximum = stu_obj.aggregate(Max('marks'))['marks__max']
    maximum = Student.objects.aggregate(Max('marks'))['marks__max']  # উপরের টা এবং এটি একই

    # total_stu = stu_obj.aggregate(Count('marks'))['marks__count']
    total_stu = Student.objects.aggregate(Count('marks'))['marks__count']  # উপরের টা এবং এটি একই

    # Create a paginator object
    paginator = Paginator(stu_obj, per_page=10) # Assuming 10 items per page
    # Get the current page number from the request's GET parameters
    page_number = request.GET.get('page')
    # Get the Page object for the requested page number
    page_obj = paginator.get_page(page_number)


    data = {
        'stu_obj':stu_obj,
        'row_set':( len(stu_obj) /2 ) + 1,
        'stu_len':len(stu_obj),
        'total':total,
        'average':average,
        'minimum':minimum,
        'maximum':maximum,
        'total_stu':total_stu,


        'page_obj':page_obj,
    }
    return render(request, 'QuerySetAPI_4.html', data)



def aggregate_testing(request):
    # Total number of books.
    total_book = Book.objects.count()  # 3

    # Total number of books with publisher = Sumilon Store
    book_obj = Book.objects.filter(publisher__name="Anu Book House")
    book_count = Book.objects.filter(publisher__name="Anu Book House").count()

    # Average price across all books.
    avg_price = Book.objects.aggregate(Avg('price'))['price__avg']

    # Max price across all books.
    max_price = Book.objects.aggregate(Max('price'))['price__max']

    # Difference between the highest priced book and the average price of all books.
    # Difference between highest and average price
    Difference = Book.objects.aggregate(
        price_diff=Max("price") - Avg("price")
        )['price_diff']
    

# -------------------------------------------------------------------------------------------------------------------
    # a = Student.objects.values('marks').annotate(Count('marks'))

    # Each publisher, each with a count of books as a "num_books" attribute.
    # এখানে book টি হল Table এর নাম যা ForeignKey key দ্বারা সংযুক্ত,
    # pubs = Publisher.objects.annotate(Count("book")) # এখানে সব গুলো publisher এর আন্ডারে যতগুলো book আছে তা return করে।
    """ RESULT:-
        <QuerySet [<Publisher: Sumilon Store>, <Publisher: Mou Book House>, <Publisher: Anu Book House>]>
    """



    # pubs = Publisher.objects.annotate(Count("book"))[2] # এখানে যে publisher এর id = 2, তা return করে।
    """RESULT:-
        Anu Book House
    """

    """ এই দুইটা publisher id return করে
        pubs = Publisher.objects.annotate(num_books=Count("book"))[2]
        pub_id = pubs.num_books

        pubs = Publisher.objects.annotate(num_books=Count("book"))
        pub_id = pubs[2].num_books
    """

#_________________________________________________________________________________________________________________________

# -------------------------------------------------------------------------------------------------------------------------
    # Each publisher, with a separate count of books with a rating above and below 4.3
    above_5 = Count("book", filter=Q(book__rating__gt=5)) # Count(F(book), filter=(AND: ('book__rating__gt', 4.3)))

    below_5 = Count("book", filter=Q(book__rating__lte=5)) # Count(F(book), filter=(AND: ('book__rating__lte', 4.3)))

    pubs = Publisher.objects.annotate(below_5=below_5).annotate(above_5=above_5)
    # <QuerySet [<Publisher: Sumilon Store>, <Publisher: Mou Book House>, <Publisher: Anu Book House>]>

    above = pubs[0].above_5

    below = pubs[0].below_5
#_________________________________________________________________________________________________________________________

    # The top 5 publishers, in order by number of books.
    pubs = Publisher.objects.annotate(num_books=Count("book")).order_by("-num_books")[:5]
    top_5_publishers = pubs[0].num_books

    print('----------------------------')
    print()
    # print(below_5)
    # print(pubs)
    # print(above)
    # print(below)
    print('----------------------------')

    return HttpResponse('Test')
