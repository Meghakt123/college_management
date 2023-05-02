from django.shortcuts import render, redirect

from homeapp.forms import CourseForm, TeacherForm, UserForm
from homeapp.models import Course, Teacher


# Create your views here.
def skydash(request):
    return render(request,'skydash.html')

def course(request):
    data = Course.objects.all()
    return render(request,'Course.html',{'data':data})

def Student(request):
    return render(request,'Student.html')


def Teachers(request):
    data =Teacher.objects.all()
    return render(request,'Teacher.html',{'data':data})

def add_course(request):
    form = CourseForm
    if request.method == 'POST':
        form = CourseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('Course')
    return render(request,'add_course.html',{'form':form})

def course_update(request,id):
    data =Course.objects.get(id=id)
    form = CourseForm(instance=data)
    if request.method == 'POST':
        form= CourseForm(request.POST or None,instance=data or None)
        if form.is_valid():
            form.save()
            return redirect('Course')
    return render(request,'add_course.html',{'form':form})

def course_delete(request,id):
    data =Course.objects.get(id=id)
    data.delete()
    return redirect('Course')

def teacher_registration(request):
    login_form=UserForm()
    form = TeacherForm()
    if request.method == 'POST':
        form = TeacherForm(request.POST)
        login_form =UserForm(request.POST)
        if login_form.is_valid() and form.is_valid():
            user=login_form.save(commit=False)
            user.is_teacher=True
            user.save()
            data=form.save(commit=False)
            data.user=user
            data.save()
            return redirect('Teacher')
    return render(request,'teacher_registration.html', {'form': form,'login_form':login_form})


