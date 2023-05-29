from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.conf import settings
from admn.models import Admin,Teacher
from teacher.models import Student,Result,Attendance
from django.views.decorators.cache import cache_control
from . serializers import AttendanceSerializer
from django.http import JsonResponse    #import jsonresponse when using ajax
import json

# Create your views here.
def teacher_home(request):
    teacher_data = Teacher.objects.get(id = request.session['teacher'])

    return render(request,'teacher_app/teacher_home.html',{'teacher_dt':teacher_data})


def teacher_logout(request):
    del request.session['teacher']
    request.session.flush()
    return redirect('common:teachers_login')


def teacher_profile(request):
    teacher = Teacher.objects.get(id = request.session['teacher'])
    return render(request,'teacher_app/teacher_profile.html',{'teacher':teacher})


def change_password(request):
    msg = ''
    if request.method == 'POST':
        current_password = request.POST['c_password']
        new_password = request.POST['n_password']
        try:
            chng_psswrd = Teacher.objects.get( password = current_password)
            update_password = Teacher.objects.filter(id = request.session['teacher']).update(password = new_password)
            msg = 'Password Changed Successfully'
        except:
            msg = 'Incorrect Password'



    return render(request,'teacher_app/change_password.html',{'msg':msg})


def add_students(request):
    teacher_dt = Teacher.objects.get(id = request.session['teacher'])
    if request.method == 'POST':
        student_name = request.POST['s_name']
        student_class = request.POST['s_class']
        student_division = request.POST['s_division']
        student_rollno = request.POST['s_rollno']
        student_enrolno = request.POST['s_enrolno']
        student_address = request.POST['s_address']
        student_gender = request.POST['s_gender']
        student_dob = request.POST['s_dob']
        student_father = request.POST['s_father']
        student_mother = request.POST['s_mother']
        student_mobile = request.POST['s_mobile']
        student_email = request.POST['s_email']
        student_image = request.FILES['s_image']
        student_username = student_name.lower()
        student_password = 'parent-' + student_name.lower()
        teacher_id = request.POST['s_teacherid']

        student = Student(
            name  = student_name,
            clas = student_class,
            division = student_division,
            roll_no = student_rollno,
            enrolment_no = student_enrolno,
            address = student_address,
            gender = student_gender,
            dob = student_dob,
            father_name = student_father,
            mother_name = student_mother,
            mobile = student_mobile,
            email = student_email,
            image = student_image,
            username = student_username,
            password = student_password,
            teacher_id = teacher_id
        )

        student.save()

    return render(request,'teacher_app/add_students.html',{'teacher_data':teacher_dt})









def view_student(request):
    student_details = Student.objects.filter(teacher_id = request.session['teacher'])

    return render(request,'teacher_app/view_student.html',{'s_details':student_details})



def student_details(request,student_id):
    student = Student.objects.get(id = student_id)
    
    return render(request,'teacher_app/student_details.html',{'student_data':student})



def update_student(request,stdnt_id):
    student = Student.objects.get(id = stdnt_id)
    if request.POST:
        sname = request.POST['s_name']
        sclass = request.POST['s_class']
        sdivision = request.POST['s_division']
        srollno = request.POST['s_rollno']
        saddress = request.POST['s_address']
        sgender = request.POST['s_gender']
        smobile = request.POST['s_mobile']
        semail = request.POST['s_email']
        

        #.get() returns an individual object and .update() only works on querysets, such as what would be returned with .filter() instead of .get().
        
        update = Student.objects.filter(id = stdnt_id).update(name = sname,
                                clas = sclass,
                                division = sdivision,
                                roll_no = srollno,
                                address = saddress,
                                gender = sgender,
                                mobile = smobile,
                                email = semail
                                )
        student = Student.objects.get(id = stdnt_id)                        
        try:
            simage = request.FILES['s_image']
            student.image = simage
            student.save()
        except:
            simage = None
        return redirect('teacher:student_details',student_id = stdnt_id)
        
    
    return render(request,'teacher_app/update_student.html',{'stdnt_data': student})

def add_result(request):
    student = Student.objects.filter(teacher_id = request.session['teacher'])
    if request.method == 'POST':
        student_id = request.POST['student_s']
        teacher_id = request.session['teacher']
        result = request.FILES['result']
        student_result = Result(
            result = result,
            student_id = student_id,
            teacher_id = teacher_id
        )
        student_result.save()

    return render(request,'teacher_app/add_result.html',{'student':student})



def view_result(request):
    result = Result.objects.filter(teacher_id = request.session['teacher'])
    return render(request,'teacher_app/view_result.html',{'result':result})

def update_result(request,student_id):
    student = Student.objects.get(id = student_id)
    msg =''
    if request.method == 'POST':
        result = request.FILES['result']
        update_result = Result.objects.get(student_id = student_id)
        update_result.result = result
        update_result.save()
        msg = 'successfully updated'

        
    context = {'msg':msg,'student':student}
    return render(request,'teacher_app/update_result.html',context)



def take_attendance(request):
    student = Student.objects.filter(teacher_id = request.session['teacher']).values('id','name','roll_no')
    if request.method == 'POST':
        attendance = request.POST['attendance_record']
        data = json.loads(attendance)

        serialized_data = AttendanceSerializer(data = data, many = True)
        if serialized_data.is_valid():
            serialized_data.save()
            print('success')
        else:
            print(serialized_data.errors)
        return JsonResponse({'status':'saved'})
        print(attendance)

    return render(request,'teacher_app/take_attendance.html',{'data':student})

def view_attendance(request):
    if request.method == 'POST':
        
        date = request.POST['att_date']
        att = Attendance.objects.filter(student__teacher = request.session['teacher'] , date = date).select_related('student')
        
        return render(request,'teacher_app/view_attendance.html',{'d':att})
        

        
        # except:
        #     msg='invalid date'
        
    return render(request,'teacher_app/view_attendance.html')
        
    

