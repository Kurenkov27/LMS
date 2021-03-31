from django.contrib.auth.models import User
from factory.django import DjangoModelFactory
from factory.fuzzy import FuzzyText

from academy.models import Student, Lecturer


class StudentFactory(DjangoModelFactory):
    class Meta:
        model = Student

    first_name = FuzzyText(prefix='first_name_')
    last_name = FuzzyText(prefix='last_name_')
    email = FuzzyText(prefix='email_')


class LecturerFactory(DjangoModelFactory):
    class Meta:
        model = Lecturer

    first_name = FuzzyText(prefix='first_name_')
    last_name = FuzzyText(prefix='last_name_')
    email = FuzzyText(prefix='email_')