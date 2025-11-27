from django.shortcuts import get_object_or_404, redirect, render
from django.contrib import messages
from .forms import CourseForm, StudentForm, TrainerForm
from academy.models import Course, Student, Trainer
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.decorators import permission_required,login_required
from django.contrib import auth
# Create your views here.


def home(request):
    return render(request,'home.html')

@login_required
@permission_required('acedemy.add_Student',raise_exception=True)
def add_courses(request):
    if request.method == 'POST':
        form = CourseForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('courses')
    else:
        form = CourseForm()
    context = {
        'form':form,
    }
    return render(request,'add_course.html',context)

@login_required
def courses(request):
    course = Course.objects.all()
    context={
        'course':course,
        
    }
    return render(request,'courses.html',context)

@login_required
def view_course(request,id):
    course = get_object_or_404(Course, id = id)
    context = {
        'course':course,
    }
    return render(request,'view_course.html',context)


@login_required
@permission_required('acedemy.add_Course',raise_exception=True)
def edit_course(request,id):
    course = get_object_or_404(Course, id = id)
    if request.method == 'POST':
        form = CourseForm(request.POST, request.FILES ,instance=course)
        if form.is_valid():
            form.save()
            return redirect('courses')
    else:
        form = CourseForm(instance=course)
    context = {
        'form':form,
        'course':course,
    }
    return render(request,'edit_course.html',context)

@login_required
@permission_required('acedemy.add_Course',raise_exception=True)
def delete_course(request,id):
    course = get_object_or_404(Course, id=id)
    course.delete()
    return redirect('courses')
    

@login_required
def trainers(request):
    trainer = Trainer.objects.all()
    context={
        'trainer':trainer,
    }
    return render(request,'trainers.html',context)

@login_required
@permission_required('acedemy.add_Student',raise_exception=True)
def add_trainer(request):
    if request.method == 'POST':
        form = TrainerForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('trainers')
    else:
        form = TrainerForm()
    context = {
        'form':form,
    }
    return render(request,'add_trainer.html',context)

@login_required
def view_trainer(request,id):
    trainer = get_object_or_404(Trainer,id=id)
    context = {
        'trainer':trainer,
    }
    return render(request,'view_trainer.html',context)


@login_required
@permission_required('acedemy.add_Student',raise_exception=True)
def edit_trainer(request,id):
    trainer = get_object_or_404(Trainer,id=id)
    if request.method == 'POST':
        form = TrainerForm(request.POST,request.FILES,instance=trainer)
        if form.is_valid():
            form.save()
            return redirect('trainers')
    else:
        form = TrainerForm(instance=trainer)
    context = {
        'form':form,
         'trainer':trainer,
       }
    return render(request,'edit_trainer.html',context)

@login_required
@permission_required('acedemy.add_Student',raise_exception=True)
def delete_trainer(request,id):
    trainer = get_object_or_404(Trainer,id=id)
    trainer.delete()
    return redirect('trainers')

@login_required
def students(request):
    student = Student.objects.all()
    context = {
        'student':student,
    }
    return render(request,'students.html',context)

@login_required
@permission_required('acedemy.add_Student',raise_exception=True)
def add_student(request):
    if request.method=='POST':
        form = StudentForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('students')
    else:
        form = StudentForm()
    context = {
        'form':form,
    }
    return render(request,'add_student.html',context)


@login_required
@permission_required('acedemy.add_Course',raise_exception=True)
def view_student(request,id):
    student = get_object_or_404(Student,id=id)
    context = {
        'student':student,
    }
    return render(request,'view_student.html',context)


@login_required
@permission_required('acedemy.add_Student',raise_exception=True)
def edit_student(request,id):
    student = get_object_or_404(Student,id=id)
    if request.method == 'POST':
        form = StudentForm(request.POST,request.FILES,instance=student)
        if form.is_valid():
            form.save()
            return redirect('students')
    else:
        form = StudentForm(instance=student)
    context = {
        'form':form,
        'student':student,
    }
    return render(request,'edit_student.html',context)



@login_required
@permission_required('acedemy.add_Student',raise_exception=True)
def delete_student(request,id):
    student= get_object_or_404(Student,id=id)
    student.delete()
    return redirect('students')


def register(request):
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            return render(request, 'accounts/register.html', {'form': form})

    else:
        form = UserCreationForm()

    return render(request, 'accounts/register.html', {'form': form})



def login(request):
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == 'POST':
        form = AuthenticationForm(request,request.POST)
        if form.is_valid():
            user = form.get_user()
            auth.login(request, user)
            return redirect('home')
    else:
        form = AuthenticationForm()
    context = {
        'form':form,
    }
    return render(request,'accounts/login.html',context)

@login_required
def logout(request):
    auth.logout(request)
    return redirect('login')