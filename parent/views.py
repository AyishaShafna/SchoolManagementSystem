from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.conf import settings
# from admn.models import Admin,Teacher
from teacher.models import Student,Result,Attendance
from admn.models import Notification
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
    result = Result.objects.filter(student_id = sid)
    notification = Notification.objects.all()
    context ={
        'student_data':student_dt,
        'result':result,
        'notification':notification
    }
    return render(request,'parent_app/stdnt_dtls.html',context)

def view_attendance(request,sid):
    attendance = Attendance.objects.filter(student = sid)
    return render(request,'parent_app/view_attendance.html',{'attendance_data':attendance})

def parent_logout(request):
    del request.session['parent']
    request.session.flush()
    return redirect('common:parent_login')