from django.contrib import admin

from academy.models import Course, Student, Trainer

# Register your models here.

class CourseForm(admin.ModelAdmin):
    list_display = ('Course_image','Course_name','Description','Duration',)

class TrainerForm(admin.ModelAdmin):
    list_display = ('Trainer_photo','First_name','Last_name','Email','Expertise',)


class StudentForm(admin.ModelAdmin):
    list_display = ('First_name','Last_name','Email','Is_active','Enrolled_course','Trainer')




admin.site.register(Course,CourseForm)
admin.site.register(Trainer,TrainerForm)
admin.site.register(Student,StudentForm )