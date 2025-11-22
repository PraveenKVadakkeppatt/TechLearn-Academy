from django.shortcuts import render

from academy.models import Course, Student, Trainer

# Create your views here.


def home(request):
    return render(request,'home.html')


def courses(request):
    course = Course.objects.all()
    context={
        'course':course,
        
    }
    return render(request,'courses.html',context)


def trainers(request):
    trainer = Trainer.objects.all()
    context={
        'trainer':trainer,
    }
    return render(request,'trainers.html',context)


def students(request):
    student = Student.objects.all()
    context = {
        'student':student,
    }
    return render(request,'students.html',context)