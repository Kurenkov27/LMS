from rest_framework import serializers

from academy.models import Student, Lecturer, Group


class StudentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Student
        fields = ('student_id', 'first_name', 'last_name', 'email')


class LecturerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Lecturer
        fields = ('lecturer_id', 'first_name', 'last_name', 'email')


class GroupSerializer(serializers.ModelSerializer):

    class Meta:
        model = Group
        fields = ('group_id', 'course', 'students', 'teacher')
