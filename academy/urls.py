from django.contrib import admin
from django.urls import path

from academy import views

urlpatterns = [
    path('courses',views.courses,name="courses"),
    path('add_courses',views.add_courses,name="add_courses"),
    path('view_course/<int:id>/',views.view_course,name="view_course"),
    path('edit_course/<int:id>/',views.edit_course,name="edit_course"),
    path('delete_course/<int:id>/',views.delete_course,name="delete_course"),
    path('trainers',views.trainers,name="trainers"),
    path('add_trainer',views.add_trainer,name="add_trainer"),
    path('view_trainer/<int:id>/',views.view_trainer,name="view_trainer"),
    path('edit_trainer/<int:id>/',views.edit_trainer,name="edit_trainer"),
    path('delete_trainer/<int:id>/',views.delete_trainer,name="delete_trainer"),
    path('students',views.students,name="students"),
    path('add_student',views.add_student,name="add_student"),
    path('view_student/<int:id>/',views.view_student,name="view_student"),
    path('edit_student/<int:id>/',views.edit_student,name="edit_student"),
    path('delete_student/<int:id>/',views.delete_student,name="delete_student"),
    path('register',views.register,name="register"),
    path('login',views.login,name="login"),
    path('logout',views.logout,name="logout"),
]