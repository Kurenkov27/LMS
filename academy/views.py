from academy.forms import StudentForm, LecturerForm, GroupForm
from academy.models import Group, Lecturer, Student

from django.http import HttpResponse

from django.shortcuts import render, get_object_or_404, redirect


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


def get_student(request):
    new_student = None

    if request.method == 'POST':
        student_form = StudentForm(data=request.POST)
        if student_form.is_valid():
            new_student = student_form.save(commit=False)
            new_student.save()

    context = {
        'student_form': StudentForm(),
        'new_student': new_student
    }

    return render(request, 'academy/create_student.html', context)


def get_lecturer(request):
    new_lecturer = None

    if request.method == 'POST':
        lecturer_form = LecturerForm(data=request.POST)
        if lecturer_form.is_valid():
            new_lecturer = lecturer_form.save(commit=False)
            new_lecturer.save()

    context = {
        'lecturer_form': LecturerForm(),
        'new_lecturer': new_lecturer
    }

    return render(request, 'academy/create_lecturer.html', context)


def get_group(request):
    new_group = None

    if request.method == 'POST':
        group_form = GroupForm(data=request.POST)
        if group_form.is_valid():
            new_group = group_form.save(commit=False)
            new_group.save()

    context = {
        'group_form': GroupForm(),
        'new_group': new_group
    }

    return render(request, 'academy/create_group.html', context)


def edit_student(request, student_id):
    student = get_object_or_404(Student, student_id=student_id)
    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            student.save()
            return redirect('get_students')
        else:
            print(form.errors)

    form = StudentForm(instance=student)
    return render(request, 'academy/edit_student.html', {'form': form})


def delete_student(request, student_id):
    Student.objects.filter(student_id=student_id).delete()
    return redirect('get_students')


def edit_lecturer(request, lecturer_id):
    lecturer = get_object_or_404(Lecturer, lecturer_id=lecturer_id)
    if request.method == 'POST':
        form = LecturerForm(request.POST, instance=lecturer)
        if form.is_valid():
            lecturer.save()
            return redirect('get_lecturers')
        else:
            print(form.errors)

    form = LecturerForm(instance=lecturer)
    return render(request, 'academy/edit_lecturer.html', {'form': form})


def delete_lecturer(request, lecturer_id):
    Lecturer.objects.filter(lecturer_id=lecturer_id).delete()
    return redirect('get_lecturers')


def edit_group(request, group_id):
    group = get_object_or_404(Group, group_id=group_id)
    if request.method == 'POST':
        form = GroupForm(request.POST, instance=group)
        if form.is_valid():
            group.save()
            return redirect('get_groups')
        else:
            print(form.errors)

    form = GroupForm(instance=group)
    return render(request, 'academy/edit_group.html', {'form': form})


def delete_group(request, group_id):
    Group.objects.filter(group_id=group_id).delete()
    return redirect('get_groups')
