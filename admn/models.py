from django.db import models

# Create your models here.
class Admin(models.Model):
    username = models.CharField(max_length = 100)
    password = models.CharField(max_length = 100)

class Meta:
    db_table = 'admin_tbl'

class Teacher(models.Model):
    name = models.CharField(max_length = 200)
    address = models.CharField(max_length = 500)
    gender = models.CharField(max_length = 50)
    dob = models.DateField()
    mobile = models.BigIntegerField()
    email = models.CharField(max_length = 200)
    department = models.CharField(max_length = 100)
    subject = models.CharField(max_length = 200)
    salary = models.FloatField()
    image = models.ImageField(upload_to = 'teacher_images/')
    clas = models.BigIntegerField()
    username = models.CharField(max_length = 200)
    password = models.CharField(max_length = 200)

class Meta:
    db_table = 'teacher_tbl'

class Salary_Table(models.Model):
    teacher = models.ForeignKey(Teacher,on_delete = models.CASCADE)
    salary_paid = models.FloatField()
    salary_pending = models.FloatField()

class Meta:
    db_table = 'salary_tbl'
 

class Notification(models.Model):
    message = models.CharField(max_length = 1000)
    notification = models.FileField(upload_to = 'notifications/')
    date = models.DateField()

class Meta:
    db_table = 'notification_tbl'
