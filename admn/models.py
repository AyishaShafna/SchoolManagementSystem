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