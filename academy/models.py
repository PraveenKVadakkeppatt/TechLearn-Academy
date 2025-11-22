from django.db import models

# Create your models here.
class Course(models.Model):
    Course_name = models.CharField(max_length=50)
    Description = models.TextField(max_length=250)
    Duration = models.PositiveIntegerField(help_text="Duration in weeks")
    Course_image = models.ImageField(upload_to='Course_image')

    def __str__(self):
        return self.Course_name

class Trainer(models.Model):
    First_name = models.CharField(max_length=50)
    Last_name = models.CharField(max_length=50)
    Email = models.EmailField(unique=True) 
    Expertise = models.CharField(max_length=100)
    Trainer_photo = models.ImageField(upload_to="Trainer_photo")

    def __str__(self):
        return f"{self.First_name} {self.Last_name}"

class Student(models.Model):
    First_name = models.CharField(max_length=50)
    Last_name = models.CharField(max_length=50)
    Email = models.EmailField(unique=True) 
    Is_active = models.BooleanField()
    Enrolled_course = models.ForeignKey(Course,on_delete=models.SET_NULL,null=True)
    Trainer = models.ForeignKey(Trainer,on_delete=models.SET_NULL,null=True)

    def __str__(self):
        return f"{self.First_name} {self.Last_name}"