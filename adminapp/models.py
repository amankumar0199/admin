from django.contrib.auth.models import AbstractUser
from django.db import models

from django.conf import settings


class CrudUser(models.Model):
    name = models.CharField(max_length=30, blank=True)
    address = models.CharField(max_length=100, blank=True)
    age = models.IntegerField(blank=True, null=True)

class CustomUser(AbstractUser):
    # add additional fields in here
    email = models.EmailField(unique = True)

    def __str__(self):
        return self.email

class type(models.Model):
    email = models.OneToOneField(CustomUser,related_name="type", on_delete = models.CASCADE)
    CHOICES = (
        ('C', 'Coaching Center'),
        ('T', 'Tutor'),
        ('S', 'Student'),
    )
    choice = models.CharField(max_length=1, choices=CHOICES)
    phone_no = models.PositiveIntegerField()
    pincode =  models.PositiveIntegerField()
class institude(models.Model):
    email = models.OneToOneField(CustomUser,related_name="institude", on_delete = models.CASCADE)
    institude_id = models.CharField(max_length = 7)
    choices = models.CharField(max_length = 1)
    institude_name = models.CharField(max_length = 30,null = True,blank = True)

class teacher(models.Model):
    email = models.OneToOneField(CustomUser,related_name="teacher", on_delete = models.CASCADE)
    teacher_id = models.CharField(max_length = 7)
    choices = models.CharField(max_length = 1)
    first_name = models.CharField(max_length = 30,null = True,blank = True)
    last_name = models.CharField(max_length = 30,null = True,blank = True)
    distance = models.CharField(max_length = 1000)
class Student(models.Model):
    email = models.OneToOneField(CustomUser,related_name="student", on_delete = models.CASCADE)
    student_id = models.CharField(max_length = 7)
    choices = models.CharField(max_length = 1)
    first_name = models.CharField(max_length = 30,null = True,blank = True)
    last_name = models.CharField(max_length = 30,null = True,blank = True)
    school_name = models.CharField(max_length = 1000,null = True,blank = True)
