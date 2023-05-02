from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class CustomUser(AbstractUser):
    is_teacher = models.BooleanField(default=False)
    is_student = models.BooleanField(default=False)

class Course(models.Model):
    Name=models.CharField(max_length=25)
    Description=models.TextField()
    Duration=models.CharField(max_length=25, null=True)
    Fee=models.CharField(max_length=25,null=True)

    def __str__(self):
        return self.Name

class Student(models.Model):
    student = models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    Name=models.CharField(max_length=25)
    Roll_no=models.IntegerField()
    Course=models.ForeignKey(Course,on_delete=models.CASCADE)
    Age=models.IntegerField()
    Contact_Number=models.CharField(max_length=10)
    # Email_id =models.EmailField()

    def __str__(self):
        return self.Name

class Teacher(models.Model):
    teacher = models.ForeignKey(CustomUser,on_delete=models.CASCADE,null=True)
    Name =models.CharField(max_length=25)
    # Email_id =models.EmailField()
    Contact_Number =models.IntegerField(max_length=10)
    address=models.TextField(null=True)


