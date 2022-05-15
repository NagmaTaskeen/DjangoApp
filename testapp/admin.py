from django.contrib import admin
from testapp.models import Employee
from testapp.models import Students
from testapp.models import ClassTable
from testapp.models import Teachers
from testapp.models import Subjects


# Register your models here.
class EmployeeAdmin(admin.ModelAdmin):
    list_display=['eno','ename','esal','eaddr']


admin.site.register(Employee,EmployeeAdmin)

class SubjectsAdmin(admin.ModelAdmin):
    list_display=['subId','subName']


admin.site.register(Subjects,SubjectsAdmin)

class TeachersAdmin(admin.ModelAdmin):
    list_display=['teacherId','teacherName','teachersQual']


admin.site.register(Teachers,TeachersAdmin)

class ClassTableAdmin(admin.ModelAdmin):
    list_display=[]


admin.site.register(ClassTable,ClassTableAdmin)

class StudentsAdmin(admin.ModelAdmin):
    list_display=['stdID','studentName','studentAddr','studentGrade','classTeacherId','studentClass']



admin.site.register(Students,StudentsAdmin)
