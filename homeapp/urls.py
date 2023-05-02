from django.urls import path

from homeapp import views

urlpatterns = [
    path('',views.skydash,name='skydash'),
    path('Course',views.course,name='Course'),
    path('Student',views.Student,name='Student'),
    path('teacher',views.Teachers,name='teacher'),
    path('add_course',views.add_course,name='add_course'),
    path('course_update/<int:id>',views.course_update,name='course_update'),
    path('course_delete/<int:id>',views.course_delete,name='course_delete'),
    path('teacher_registration',views.teacher_registration,name='teacher_registration'),
]