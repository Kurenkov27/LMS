from django.db import models
# Create your models here.
from django.urls import reverse


class Student(models.Model):
    student_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=30, blank=True, null=True)
    last_name = models.CharField(max_length=30, blank=True, null=True)
    email = models.EmailField(max_length=150)
    photo = models.ImageField(upload_to='photos/', default='photos/default.png')

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    def get_absolute_url(self):
        return '/students'


class Lecturer(models.Model):
    lecturer_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=30, blank=True, null=True)
    last_name = models.CharField(max_length=30, blank=True, null=True)
    email = models.EmailField(max_length=150)
    photo = models.ImageField(upload_to='photos/', default='photos/default.png')

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    def get_absolute_url(self):
        return '/lecturers'


class Group(models.Model):
    group_id = models.AutoField(primary_key=True)
    course = models.CharField(max_length=150)
    students = models.ManyToManyField(Student)
    teacher = models.OneToOneField(Lecturer, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.course}'


class Message(models.Model):
    message_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30, blank=True, null=True)
    email = models.EmailField(max_length=250)
    message = models.TextField(max_length=1000)

    def __str__(self):
        return f'Message from {self.email}'

    def to_dict(self):
        return {
            'name': self.name,
            'email': self.email,
            'message': self.message
        }
