from django.db import models
# Create your models here.


class Student(models.Model):
    student_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=30, blank=True, null=True)
    last_name = models.CharField(max_length=30, blank=True, null=True)
    email = models.EmailField(max_length=250)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Lecturer(models.Model):
    lecturer_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=30, blank=True, null=True)
    last_name = models.CharField(max_length=30, blank=True, null=True)
    email = models.EmailField(max_length=150)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


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
