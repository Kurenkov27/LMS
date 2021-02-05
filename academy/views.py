from academy.models import Group, Lecturer, Student

from django.http import HttpResponse

from django.shortcuts import render

# Create your views here.


def index(request):
    return HttpResponse("Hello, World!")


# Create your views here.
def get_students(request):
    students = Student.objects.all().order_by('student_id')
    return render(request, 'academy/get_students.html', {'students': students})


def get_lecturers(request):
    lecturers = Lecturer.objects.all().order_by('lecturer_id')
    return render(request, 'academy/get_lecturers.html', {'lecturers': lecturers})


def get_groups(request):
    groups = Group.objects.all().order_by('-group_id')
    return render(request, 'academy/get_groups.html', {'groups': groups})
