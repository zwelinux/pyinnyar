from django.shortcuts import render
from .models import Instructor, Student, Subject

# Create your views here.
def index(request):
    subjects = Subject.objects.all()
    return render(request, 'app/index.html', {'subjects':subjects})