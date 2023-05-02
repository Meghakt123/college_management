from django import forms
from django.contrib.auth.forms import UserCreationForm

from homeapp.models import Course, Teacher, CustomUser
from django.forms import ModelForm
from.models import Course

class CourseForm(forms.ModelForm):
    class Meta:
        model= Course
        fields= '__all__'


class TeacherForm(forms.ModelForm):
    class Meta:
        model= Teacher
        fields= ('Name','Contact_Number','address')

class UserForm(UserCreationForm):
    class Meta:
        model= CustomUser
        fields= ('email','username','password1','password2')


