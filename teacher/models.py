from django.db import models
from admn.models import Teacher

# Create your models here.
class Student(models.Model):
    teacher = models.ForeignKey(Teacher,on_delete = models.CASCADE)
    name = models.CharField(max_length = 200)
    clas = models.BigIntegerField()
    division = models.CharField(max_length = 20)
    roll_no = models.BigIntegerField()
    enrolment_no = models.CharField(max_length = 100)
    address = models.CharField(max_length = 500)
    gender = models.CharField(max_length = 50)
    dob = models.DateField()
    father_name = models.CharField(max_length = 200)
    mother_name = models.CharField(max_length = 200)
    mobile = models.BigIntegerField()
    email = models.CharField(max_length = 200)
    image = models.ImageField(upload_to = 'students_images/')
    username = models.CharField(max_length = 200)
    password = models.CharField(max_length = 200)

class Meta:
    db_table = 'student_tbl'

class Result(models.Model):
    student = models.ForeignKey(Student,on_delete = models.CASCADE)
    teacher = models.ForeignKey(Teacher,on_delete = models.CASCADE)
    result = models.FileField(upload_to = 'results/')

class Meta:
    db_table = 'result_tbl'

class Attendance(models.Model):
    student = models.ForeignKey(Student, on_delete = models.CASCADE)
    date = models.DateField()
    status = models.CharField(max_length = 100)

class Meta:
    db_table = 'attendance_tbl'
