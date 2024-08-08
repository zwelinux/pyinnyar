from django.db import models
import qrcode 
from django.utils.html import format_html
from io import BytesIO
from django.core.files import File

class Instructor(models.Model):
    instructor_name = models.CharField(max_length=255)
    instructor_url = models.SlugField(max_length=255, unique=True)
    instructor_email = models.EmailField()
    instructor_rank = models.CharField(max_length=255)


    def __str__(self):
        return self.instructor_name

class Student(models.Model):
    student_name = models.CharField(max_length=255)
    student_url = models.SlugField(max_length=255, unique=True)
    student_email = models.EmailField()
    student_role = models.CharField(max_length=255)

    def __str__(self):
        return self.student_name
    
class Subject(models.Model):
    subject_name = models.CharField(max_length=255)
    subject_url = models.SlugField(max_length=255, unique=True)
    instructor = models.ForeignKey(Instructor, on_delete=models.CASCADE)
    subject_qrcode = models.ImageField(upload_to='Subject QRs', blank=True)

    def __str__(self):
        return self.subject_name