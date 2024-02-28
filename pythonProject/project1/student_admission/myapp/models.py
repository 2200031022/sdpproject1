from django.db import models

# Create your models here.
from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    # Define other fields as per your requirements

class Course(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    # Define other fields as per your requirements

class Admission(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    admission_date = models.DateField(auto_now_add=True)
    # Define other fields as per your requirements
