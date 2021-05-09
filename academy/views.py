from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.urls import reverse, reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.status import HTTP_201_CREATED, HTTP_400_BAD_REQUEST, HTTP_404_NOT_FOUND, HTTP_204_NO_CONTENT, \
    HTTP_200_OK

from LMS.settings import GROUPS_PER_PAGE
from academy.forms import StudentForm, LecturerForm, GroupForm, MessageForm
from academy.models import Group, Lecturer, Student
from django.views.decorators.cache import cache_page


from django.shortcuts import render, get_object_or_404, redirect


# Create your views here.
from academy.serializers import StudentSerializer, LecturerSerializer, GroupSerializer
from exchanger.models import ExchangeRate
from logger.models import LogRecord


def index(request):
    exchange_rates = ExchangeRate.objects.all()
    context = {
        k: v for ex_rate in exchange_rates
        for k, v in ex_rate.to_dict().items()
    }
    print(context)
    return render(request, 'academy/main_page.html',  context)


# Create your views here.
def get_students(request):
    students = Student.objects.all().order_by('student_id')
    return render(request, 'academy/get_students.html', {'students': students})


def get_lecturers(request):
    lecturers = Lecturer.objects.all().order_by('lecturer_id')
    return render(request, 'academy/get_lecturers.html', {'lecturers': lecturers})


def get_groups(request):
    groups = Group.objects.all().order_by('-group_id').reverse()
    context = {}
    paginator = Paginator(groups, GROUPS_PER_PAGE)
    page = request.GET.get('page')
    try:
        groups = paginator.page(page)
    except PageNotAnInteger:
        groups = paginator.page(1)
    except EmptyPage:
        groups = paginator.page(paginator.num_pages)
    context['page'] = page
    context['groups'] = groups
    return render(request, 'academy/get_groups.html', context)


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


@login_required
def edit_student(request, student_id):
    student = get_object_or_404(Student, student_id=student_id)
    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            student.save()
            return redirect('get_students')

    form = StudentForm(instance=student)
    return render(request, 'academy/edit_student.html', {'form': form})


def delete_student(request, student_id):
    Student.objects.filter(student_id=student_id).delete()
    return redirect('get_students')


@login_required
def edit_lecturer(request, lecturer_id):
    lecturer = get_object_or_404(Lecturer, lecturer_id=lecturer_id)
    if request.method == 'POST':
        form = LecturerForm(request.POST, instance=lecturer)
        if form.is_valid():
            lecturer.save()
            return redirect('get_lecturers')

    form = LecturerForm(instance=lecturer)
    return render(request, 'academy/edit_lecturer.html', {'form': form})


def delete_lecturer(request, lecturer_id):
    Lecturer.objects.filter(lecturer_id=lecturer_id).delete()
    return redirect('get_lecturers')


@login_required
def edit_group(request, group_id):
    group = get_object_or_404(Group, group_id=group_id)
    if request.method == 'POST':
        form = GroupForm(request.POST, instance=group)
        if form.is_valid():
            group.save()
            return redirect('get_groups')

    form = GroupForm(instance=group)
    return render(request, 'academy/edit_group.html', {'form': form})


def delete_group(request, group_id):
    Group.objects.filter(group_id=group_id).delete()
    return redirect('get_groups')


@cache_page(60 * 5)
def send_message(request):
    new_message = None
    already_sent = False
    if request.method == 'POST':
        message_form = MessageForm(data=request.POST)
        if message_form.is_valid():
            sent = request.session.get('sent')
            if not sent:
                request.session['sent'] = True
                new_message = message_form.save(commit=False)
                new_message.save()
            else:
                already_sent = True
            request.session.modified = True

    context = {
        'message_form': MessageForm(),
        'new_message': new_message,
        'sent': already_sent
    }
    return render(request, 'academy/create_message.html', context)


class StudentCreate(LoginRequiredMixin, CreateView):
    model = Student
    template_name = 'academy/create_student.html'
    fields = ['first_name', 'last_name', 'email', 'photo']


class StudentEdit(LoginRequiredMixin, UpdateView):
    model = Student
    template_name = 'academy/edit_student.html'
    fields = ['first_name', 'last_name', 'email', 'photo']


class StudentDelete(LoginRequiredMixin, DeleteView):
    model = Student
    template_name = 'academy/delete_student.html'
    success_url = reverse_lazy('get_students')


class LecturerCreate(LoginRequiredMixin, CreateView):
    model = Lecturer
    template_name = 'academy/create_lecturer.html'
    fields = ['first_name', 'last_name', 'email', 'photo']


class LecturerEdit(LoginRequiredMixin, UpdateView):
    model = Lecturer
    template_name = 'academy/create_lecturer.html'
    fields = ['first_name', 'last_name', 'email', 'photo']


class LecturerDelete(LoginRequiredMixin, DeleteView):
    model = Lecturer
    template_name = 'academy/delete_lecturer.html'
    success_url = reverse_lazy('get_lecturers')


@api_view(['GET', 'POST'])
@authentication_classes([SessionAuthentication, BasicAuthentication])
@permission_classes([IsAuthenticated])
def students(request):
    if request.method == 'GET':
        articles = Student.objects.all()
        serializer = StudentSerializer(articles, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        rdata = request.data
        data = {
            'first_name': rdata.get('first_name'),
            'last_name': rdata.get('last_name'),
            'email': rdata.get('email'),
        }
        serializer = StudentSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=HTTP_201_CREATED)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)


@api_view(['GET', 'DELETE', 'PUT'])
@authentication_classes([SessionAuthentication, BasicAuthentication])
@permission_classes([IsAuthenticated])
def student(request, pk):
    try:
        student = Student.objects.get(pk=pk)
    except Student.DoesNotExist:
        return Response(status=HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = StudentSerializer(student)
        return Response(serializer.data)

    if request.method == 'DELETE':
        student.delete()
        return Response(status=HTTP_204_NO_CONTENT)

    if request.method == 'PUT':
        first_name = request.data.get('first_name')
        if first_name:
            student.first_name = first_name
        last_name = request.data.get('last_name')
        if last_name:
            student.last_name = last_name
        email = request.data.get('email')
        if email:
            student.email = email
        student.save()
        serializer = StudentSerializer(student)
        return Response(serializer.data, status=HTTP_200_OK)


@api_view(['GET', 'POST'])
@authentication_classes([SessionAuthentication, BasicAuthentication])
@permission_classes([IsAuthenticated])
def lecturers(request):
    if request.method == 'GET':
        lecturers = Lecturer.objects.all()
        serializer = LecturerSerializer(lecturers, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        rdata = request.data
        data = {
            'first_name': rdata.get('first_name'),
            'last_name': rdata.get('last_name'),
            'email': rdata.get('email'),
        }
        serializer = LecturerSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=HTTP_201_CREATED)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)


@api_view(['GET', 'DELETE', 'PUT'])
@authentication_classes([SessionAuthentication, BasicAuthentication])
@permission_classes([IsAuthenticated])
def lecturer(request, pk):
    try:
        lecturer = Lecturer.objects.get(pk=pk)
    except Lecturer.DoesNotExist:
        return Response(status=HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = LecturerSerializer(lecturer)
        return Response(serializer.data)

    if request.method == 'DELETE':
        lecturer.delete()
        return Response(status=HTTP_204_NO_CONTENT)

    if request.method == 'PUT':
        first_name = request.data.get('first_name')
        if first_name:
            lecturer.first_name = first_name
        last_name = request.data.get('last_name')
        if last_name:
            lecturer.last_name = last_name
        email = request.data.get('email')
        if email:
            lecturer.email = email
        lecturer.save()
        serializer = LecturerSerializer(lecturer)
        return Response(serializer.data, status=HTTP_200_OK)


@api_view(['GET', 'POST'])
@authentication_classes([SessionAuthentication, BasicAuthentication])
@permission_classes([IsAuthenticated])
def groups(request):
    if request.method == 'GET':
        groups = Group.objects.all()
        serializer = GroupSerializer(groups, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        rdata = request.data
        data = {
            'course': rdata.get('course'),
            'teacher': rdata.get('teacher'),
            'students': rdata.get('students'),
        }
        try:
            lecturer = Lecturer.objects.get(pk=data['teacher'])
        except Lecturer.DoesNotExist:
            return Response({"message": 'Lecturer does not exist'}, status=HTTP_404_NOT_FOUND)
        for student_key in data['students']:
            try:
                student = Student.objects.get(pk=student_key)
            except Student.DoesNotExist:
                return Response({"message": f'Student {student_key} does not exist'}, status=HTTP_404_NOT_FOUND)
        group.teacher = lecturer
        serializer = GroupSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=HTTP_201_CREATED)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)


@api_view(['GET', 'DELETE', 'PUT'])
@authentication_classes([SessionAuthentication, BasicAuthentication])
@permission_classes([IsAuthenticated])
def group(request, pk):
    try:
        group = Group.objects.get(pk=pk)
    except Group.DoesNotExist:
        return Response(status=HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = GroupSerializer(group)
        return Response(serializer.data)

    if request.method == 'DELETE':
        group.delete()
        return Response(status=HTTP_204_NO_CONTENT)

    if request.method == 'PUT':
        course = request.data.get('course')
        if course:
            group.course = course
        lecturer_key = request.data.get('teacher')
        if lecturer_key:
            try:
                lecturer = Lecturer.objects.get(pk=lecturer_key)
            except Lecturer.DoesNotExist:
                return Response({"message": 'Lecturer does not exist'}, status=HTTP_404_NOT_FOUND)
            group.teacher = lecturer
        student_keys = request.data.get('students')
        if student_keys or student_keys == []:
            stud_list = []
            for student_key in student_keys:
                try:
                    student = Student.objects.get(pk=student_key)
                    print('aaa', student)
                except Student.DoesNotExist:
                    return Response({"message": 'Student does not exist'}, status=HTTP_404_NOT_FOUND)
                stud_list.append(student)
            print("end")
            group.students.set(stud_list)
        group.save()
        serializer = GroupSerializer(group)
        return Response(serializer.data, status=HTTP_200_OK)

