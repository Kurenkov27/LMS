from django.core.exceptions import ValidationError
from django.test import TestCase

from academy.models import Student, Group, Lecturer, Message


class AcademyModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.first_name = 'name'
        cls.last_name = 'last name'
        cls.email = 'email@mail.ru'
        cls.course = "Testcourse"
        cls.message = 'message'
        cls.student = Student.objects.create(first_name='Harry', last_name='Potter', email="Harry@gmail.com")
        cls.lecturer = Lecturer.objects.create(first_name='Eddy', last_name='Doolittle', email="Doolittle@gmail.com")
        pass

    def setUp(self) -> None:
        # вызывается перед каждой тестовой функцией для настройки объектов,
        # которые могут изменяться во время тестов
        pass

    def tearDown(self) -> None:
        pass

    def test_successful_student_creation(self):
        student = Student(first_name=self.first_name, last_name=self.last_name, email=self.email)
        student.full_clean()

    def test_successful_lecturer_creation(self):
        lecturer = Lecturer(first_name="name", last_name="last_name", email='test@test.test')
        lecturer.full_clean()

    def test_successful_group_creation(self):
        group = Group(course=self.course, teacher=self.lecturer)
        group.save()
        group.students.set([self.student])
        group.full_clean()

    def test_failure_due_to_long_name_student(self):
        name = 'a' * 31
        student = Student(first_name=name, last_name=self.last_name, email=self.email)
        with self.assertRaises(ValidationError):
            student.full_clean()

    def test_failure_due_to_long_last_name_student(self):
        last_name = 'a' * 31
        student = Student(first_name=self.first_name, last_name=last_name, email=self.email)
        with self.assertRaises(ValidationError):
            student.full_clean()

    def test_failure_due_to_long_email_student(self):
        email = 'e' * 151
        student = Student(email=email, first_name=self.first_name, last_name=self.last_name)
        with self.assertRaises(ValidationError):
            student.full_clean()

    def test_failure_due_to_long_name_lecturer(self):
        name = 'a' * 31
        lecturer = Lecturer(first_name=name, last_name=self.last_name, email=self.email)
        with self.assertRaises(ValidationError):
            lecturer.full_clean()

    def test_failure_due_to_long_last_name_lecturer(self):
        last_name = 'a' * 31
        lecturer = Lecturer(first_name=self.first_name, last_name=last_name, email=self.email)
        with self.assertRaises(ValidationError):
            lecturer.full_clean()

    def test_failure_due_to_long_email_lecturer(self):
        email = 'e' * 151
        lecturer = Lecturer(email=email, first_name=self.first_name, last_name=self.last_name)
        with self.assertRaises(ValidationError):
            lecturer.full_clean()

    def test_failure_due_to_long_course_name_group(self):
        course = 'a' * 151
        group = Group(course=course, teacher=self.lecturer)
        group.save()
        group.students.set([self.student])
        with self.assertRaises(ValidationError):
            group.full_clean()

    def test_str_equals_expected_str_group(self):
        group = Group(course=self.course, teacher=self.lecturer)
        group.save()
        group.students.set([self.student])
        self.assertEquals(self.course, str(group))

    def test_str_equals_expected_str_student(self):
        student = Student(first_name=self.first_name, last_name=self.last_name, email=self.email)
        self.assertEquals(f'{self.first_name} {self.last_name}', str(student))

    def test_str_equals_expected_str_lecturer(self):
        lecturer = Lecturer(first_name=self.first_name, last_name=self.last_name, email=self.email)
        self.assertEquals(f'{self.first_name} {self.last_name}', str(lecturer))

    def test_to_dict_equals_to_short_representation_message(self):
        message = Message(name=self.first_name, email=self.email, message=self.message)
        expected = {
            'name': self.first_name,
            'email': self.email,
            'message': self.message
        }
        self.assertEquals(message.to_dict(), expected)