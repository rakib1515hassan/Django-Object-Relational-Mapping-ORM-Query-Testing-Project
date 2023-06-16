from django.db import models
from django.conf import settings

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=50, null=True, blank=True)
    roll = models.IntegerField(null=True, blank=True)
    # date_of_birth = models.DateField(settings.DATE_INPUT_FORMATS)
    date_of_birth = models.DateField()
    city = models.CharField(max_length=50, null=True, blank=True)
    marks = models.IntegerField(null=True, blank=True)
    result = models.CharField(max_length=20, choices=(
        ('Pass','Pass'),
        ('Fail','Fail')
        ), null=True, blank=True)
    gread = models.CharField(max_length=10, choices=(
        ('A+','A+'),
        ('A' ,'A' ),
        ('A-','A-'),
        ('B' ,'B' ),
        ('C' ,'C' ),
        ('D' ,'D' ),
        ('E' ,'E' ),
        ('F' ,'F' ),
    ),null=True, blank=True)
    # pass_date = models.DateField(settings.DATE_INPUT_FORMATS)
    pass_date = models.DateField()

    def __str__(self):
        return self.name



class Teacher(models.Model):
    emplyee_id = models.IntegerField(unique=True, null=False)

    name = models.CharField(max_length=50, null=True, blank=True)
    city = models.CharField(max_length=50, null=True, blank=True)
    salary = models.IntegerField()
    join = models.DateTimeField()

    def __str__(self):
        return self.name





## Show Data in html <p>Date: {{ std_obj.date_of_birth|date:"m/d/Y" }}</p> 
