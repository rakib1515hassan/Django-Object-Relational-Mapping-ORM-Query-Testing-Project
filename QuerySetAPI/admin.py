from django.contrib import admin
from QuerySetAPI.models import Student, Teacher


# Register your models here.


# admin.site.register(Student)
@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'roll', 'date_of_birth', 'city', 'marks', 'gread', 'result', 'pass_date']

@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'emplyee_id', 'city', 'salary', 'join']

