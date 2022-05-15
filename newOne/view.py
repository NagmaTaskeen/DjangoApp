from django.http import HttpResponse
from django.shortcuts import render
import json
from testapp.models import Employee

#def index(request):
#    return render(request,'newOne/index.html')'''
#    return HttpResponse('hello,world')

def emp_data(request):
    emp_data2={
    'id':100,
    'name':'tash'
    }
    jsonData=json.dumps(emp_data2)
    return HttpResponse(jsonData,content_type='application/json')

def emp_datatrytemplate(request):
    emp_data2={
    'id':100,
    'name':'tashgrtgy'
    }
    jsonData=json.dumps(emp_data2)
    return render(request,'testapp/result.html',{'yt':jsonData})
    #return HttpResponse(jsonData,content_type='application/json')

from django.http import JsonResponse
def emp_dataJsonRes(request):
        emp_data2={
        'id':100,
        'name':'tash'
        }
        jsonData=json.dumps(emp_data2)
        return JsonResponse(jsonData);
    #return HttpResponse('hello,world'+ str(emp_data2))
    #return HttpResponse(str(emp_data2))


#learning DB stuff
# how to display emp data
def emp_datafromDB(request):
    employee= Employee.objects.all()
    employee= Subjects.objects.all()
    employee= Teachers.objects.all()
    employee= ClassTable.objects.all()
    employee= Students.objects.all()

    return render(request,'testapp/result.html',{'empdata':employee})
