from django import forms

from .models import Student, Lecturer, Group, Message


class StudentForm(forms.ModelForm):

    class Meta:
        model = Student
        fields = ('first_name', 'last_name', 'email')


class LecturerForm(forms.ModelForm):

    class Meta:
        model = Lecturer
        fields = ('first_name', 'last_name', 'email')


class GroupForm(forms.ModelForm):

    class Meta:
        model = Group
        fields = ('course', 'students', 'teacher')


class MessageForm(forms.ModelForm):

    class Meta:
        model = Message
        fields = ('name', 'email', 'message')
