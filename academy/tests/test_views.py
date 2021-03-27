from django.test import TestCase
from django.urls import reverse

from academy.models import Lecturer, Student, Group


class ArticleListViewTest(TestCase):
    number_of_students = 10
    number_of_lecturers = 5

    @classmethod
    def setUpTestData(cls):
        for student_num in range(cls.number_of_students):
            Student.objects.create(
                first_name=f'Barack_{student_num}',
                last_name=f'Obama_{student_num}',
                email=f'Obama{student_num}@email.com'
            )

        for lecturer_num in range(cls.number_of_lecturers):
            Lecturer.objects.create(
                first_name=f'John_{lecturer_num}',
                last_name=f'Doe_{lecturer_num}',
                email=f'Doe{lecturer_num}@email.com'
            )

        lecturer = Lecturer(
            first_name='John',
            last_name='Doe',
            email='Doe@email.com')
        lecturer.save()
        Group.objects.create(
            course="CourseName",
            teacher=lecturer
        )

    def test_view_url_exists_at_desired_location_students(self):
        resp = self.client.get('/students/')
        self.assertEqual(resp.status_code, 200)

    def test_view_url_accessible_by_name_students(self):
        resp = self.client.get(reverse('get_students'))
        self.assertEqual(resp.status_code, 200)

    def test_view_uses_correct_template_students(self):
        resp = self.client.get(reverse('get_students'))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'academy/get_students.html')

    def test_lists_all_students(self):
        resp = self.client.get(reverse('get_students'))
        self.assertEqual(resp.status_code, 200)
        self.assertTrue(len(resp.context['students']) == 10)

    def test_view_url_exists_at_desired_location_lecturers(self):
        resp = self.client.get('/lecturers/')
        self.assertEqual(resp.status_code, 200)

    def test_view_url_accessible_by_name_lecturers(self):
        resp = self.client.get(reverse('get_lecturers'))
        self.assertEqual(resp.status_code, 200)

    def test_view_uses_correct_template_lecturers(self):
        resp = self.client.get(reverse('get_lecturers'))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'academy/get_lecturers.html')

    def test_lists_all_lecturers(self):
        resp = self.client.get(reverse('get_lecturers'))
        self.assertEqual(resp.status_code, 200)
        self.assertTrue(len(resp.context['lecturers']) == 6)

    def test_view_url_exists_at_desired_location_groups(self):
        resp = self.client.get('/groups/')
        self.assertEqual(resp.status_code, 200)

    def test_view_url_accessible_by_name_groups(self):
        resp = self.client.get(reverse('get_groups'))
        self.assertEqual(resp.status_code, 200)

    def test_view_uses_correct_template_groups(self):
        resp = self.client.get(reverse('get_groups'))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'academy/get_groups.html')

    def test_lists_all_groups(self):
        resp = self.client.get(reverse('get_groups'))
        self.assertEqual(resp.status_code, 200)
        self.assertTrue(len(resp.context['groups']) == 1)
