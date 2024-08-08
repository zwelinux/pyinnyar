from django.contrib import admin
from .models import Student, Instructor, Subject

admin.site.site_header = 'QAMS'

class StudentAdmin(admin.ModelAdmin):
    list_display = ['student_name', 'student_email', 'student_role']

admin.site.register(Student, StudentAdmin)

class InstructorAdmin(admin.ModelAdmin):
    list_display = ['instructor_name', 'instructor_email', 'instructor_rank']

admin.site.register(Instructor, InstructorAdmin)

class SubjectAdmin(admin.ModelAdmin):
    list_display = ['subject_name', 'instructor', 'subject_qrcode']

admin.site.register(Subject, SubjectAdmin)