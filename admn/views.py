from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.conf import settings
from admn.models import Admin,Teacher
from teacher.models import Student
from django.views.decorators.cache import cache_control
import random

# Create your views here.

def admin_login(request):
    msg =""
    if request.method == 'POST':
        admin_username = request.POST['a_username']
        admin_password = request.POST['a_password']
        try:
            admin_data = Admin.objects.get(username = admin_username, password = admin_password)
            request.session['admin'] = admin_data.id
            return redirect('admn:home')
        except:
            msg = 'invalid username or password'

    return render(request,'admn/admin_login.html',{'message':msg})


@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def admin_logout(request):
    del request.session['admin']
    request.session.flush()
    return redirect('admn:admin_login')




def home(request):
    return render(request,'admn/home.html')

def teachers_page(request):
    


    return render(request,'admn/teachers_page.html')




def add_teacher(request):
    if request.method == 'POST':
        teacher_name = request.POST['t_name']
        teacher_address = request.POST['t_address']
        teacher_gender = request.POST['t_gender']
        teacher_dob = request.POST['t_dob']
        teacher_mobile = request.POST['t_mobile']
        teacher_email = request.POST['t_email']
        teacher_department = request.POST['t_department']
        teacher_subject = request.POST['t_subject']
        teacher_salary = request.POST['t_salary']
        teacher_image = request.FILES['t_image']
        teacher_class = request.POST['t_class']
        teacher_username = teacher_name.lower()
        teacher_password = teacher_name.lower() + str(teacher_dob)
        
        new_teacher = Teacher(
            name = teacher_name,
            address = teacher_address,
            gender = teacher_gender,
            dob = teacher_dob,
            mobile = teacher_mobile,
            email = teacher_email,
            department = teacher_department,
            subject = teacher_subject,
            salary = teacher_salary,
            image = teacher_image,
            clas = teacher_class,
            username = teacher_username,
            password = teacher_password
        )
        new_teacher.save()

    return render(request,'admn/add_teacher.html')






def view_teacher(request):
    teacher_dt = Teacher.objects.all()
    return render(request,'admn/view_teacher.html',{'teacher_details':teacher_dt})

def salary_page(request):
    return render(request,'admn/salary_page.html')

def view_salary(request):
    return render(request,'admn/view_salary.html')

def edit_salary(request):
    return render(request,'admn/edit_salary.html')

def student_page(request):
    return render(request,'admn/student_page.html')

def view_student(request):
    student = Student.objects.all()
    return render(request,'admn/view_student.html',{'student':student})

def update_student(request):
    return render(request,'admn/update_student.html')

def fees_page(request):
    return render(request,'admn/fees_page.html')

def view_feesdetails(request):
    return render(request,'admn/view_feesdetails.html')

def notification_page(request):
    return render(request,'admn/notification_page.html')

def add_notification(request):
    return render(request,'admn/add_notification.html')

def view_notification(request):
    return render(request,'admn/view_notification.html')

def complaints_page(request):
    return render(request,'admn/complaints_page.html')