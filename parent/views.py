from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.conf import settings
# from admn.models import Admin,Teacher
from teacher.models import Student,Result
from django.views.decorators.cache import cache_control

# Create your views here.
def parent_home(request):
    student = Student.objects.filter(father_name = request.session['parent']).values('id','name','clas','roll_no','image')
    #since .values used image will display only when the path mentions in html page
    # print(request.session['parent'])
    # print(student) will print in cmd
    return render(request,'parent_app/parent_home.html',{'stdnt':student})

def stdnt_dtls(request,sid):
    student_dt = Student.objects.get(id = sid)
    return render(request,'parent_app/stdnt_dtls.html',{'student_data':student_dt})