from academy.models import Group, Lecturer, Student

from django.core.management.base import BaseCommand

from faker import Faker


class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        fake = Faker(['en_US'])
        number_of_students = 10
        number_of_groups = 2

        # Create new groups:
        for i in range(number_of_groups):

            # Create new lecturer:
            lecturer = Lecturer.objects.create(first_name=fake.unique.first_name(),
                                               last_name=fake.unique.last_name(),
                                               email=fake.email())
            lecturer.save()

            group = Group.objects.create(course=fake.job(), teacher=lecturer)

            # Create new students:
            for j in range(number_of_students):
                student = Student.objects.create(first_name=fake.unique.first_name(),
                                                 last_name=fake.unique.last_name(),
                                                 email=fake.email())
                student.save()
                group.students.add(student)

            group.save()
