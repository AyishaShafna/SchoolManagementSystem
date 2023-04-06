from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.conf import settings
from admn.models import Admin,Teacher
from teacher.models import Student
from django.views.decorators.cache import cache_control
import random

# Create your views here.
def common_home(request):
    return render(request,'common_app/common_home.html')

def parent_login(request):
    msg=''
    if request.method == 'POST':
        parent_username = request.POST['p_username']
        parent_password = request.POST['p_password']
        try:
            student_dt = Student.objects.get(father_name = parent_username,password = parent_password)
            request.session['parent'] = student_dt.father_name 
            return redirect('parent:parent_home')
        except:
            msg = 'invalid username or password'
     
    return render(request,'common_app/parent_login.html',{'msg':msg})



def teachers_login(request):
    msg=''
    if request.method == 'POST':
        teacher_username = request.POST['t_username']
        teacher_password = request.POST['t_password']
        try:
            teacher_dt = Teacher.objects.get(username = teacher_username,password = teacher_password)
            request.session['teacher'] = teacher_dt.id
            return redirect('teacher:teacher_home')
        except:
            msg = 'invalid username or password'
    return render(request,'common_app/teachers_login.html',{'message':msg})