import pytest
from django.urls import reverse

from academy.models import Lecturer, Student, Group
from academy.tests.factory import StudentFactory, LecturerFactory


@pytest.mark.django_db
def test_view_url_exists_at_desired_location_students(client):
    resp = client.get('/students/')
    assert resp.status_code == 200


@pytest.mark.django_db
def test_view_url_accessible_by_name_students(client):
    resp = client.get(reverse('get_students'))
    assert resp.status_code == 200


@pytest.mark.django_db
def test_view_uses_correct_template_students(client):
    resp = client.get(reverse('get_students'))
    assert resp.status_code == 200
    expected_link = 'academy/get_students.html'
    assert expected_link.encode() not in resp.content


@pytest.fixture(name="create_persons")
def create_persons(django_user_model):
    def make_person(**kwargs):
        number_of_persons = kwargs['number_of_persons']
        type_of_person = kwargs['type_of_person']
        persons = []
        for person_num in range(number_of_persons):
            if type_of_person == "student":
                #person = Student.objects.create(first_name=f'Alex{person_num}', last_name=f'Mitts{person_num}', email=f'{person_num}@mail.ru')
                person = StudentFactory.create()
            elif type_of_person == "lecturer":
                #person = Lecturer.objects.create(first_name=f'Henry{person_num}', last_name=f'Ford{person_num}', email=f'{person_num}@yahoo.com')
                person = LecturerFactory.create()
            if person:
                persons.append(person)
        return persons
    return make_person


@pytest.mark.django_db
def test_lists_all_students(client, create_persons):
    number_of_students = 5
    create_persons(number_of_persons=number_of_students, type_of_person='student')
    resp = client.get(reverse('get_students'))
    students = resp.context['students']
    assert len(students) == number_of_students


@pytest.mark.django_db
def test_view_url_exists_at_desired_location_lecturers(client):
    resp = client.get('/lecturers/')
    assert resp.status_code == 200


@pytest.mark.django_db
def test_view_url_accessible_by_name_lecturers(client):
    resp = client.get(reverse('get_lecturers'))
    assert resp.status_code == 200


@pytest.mark.django_db
def test_view_uses_correct_template_lecturers(client):
    resp = client.get(reverse('get_lecturers'))
    assert resp.status_code == 200
    expected_link = 'academy/get_lecturers.html'
    assert expected_link.encode() not in resp.content


@pytest.mark.django_db
def test_lists_all_lecturers(client, create_persons):
    number_of_lecturers = 6
    create_persons(number_of_persons=number_of_lecturers, type_of_person='lecturer')
    resp = client.get(reverse('get_lecturers'))
    students = resp.context['lecturers']
    assert len(students) == number_of_lecturers


@pytest.mark.django_db
def test_view_url_exists_at_desired_location_groups(client):
    resp = client.get('/groups/')
    assert resp.status_code == 200


@pytest.mark.django_db
def test_view_url_accessible_by_name_groups(client):
    resp = client.get(reverse('get_groups'))
    assert resp.status_code == 200


@pytest.mark.django_db
def test_view_uses_correct_template_groups(client):
    resp = client.get(reverse('get_groups'))
    assert resp.status_code == 200
    expected_link = 'academy/get_groups.html'
    assert expected_link.encode() not in resp.content
