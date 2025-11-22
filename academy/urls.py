from django.contrib import admin
from django.urls import path

from academy import views

urlpatterns = [
    path('courses',views.courses,name="courses"),
    path('trainers',views.trainers,name="trainers"),
    path('students',views.students,name="students"),
]