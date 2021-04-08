from django.urls import path
from django.views.decorators.cache import cache_page

from . import views


urlpatterns = [
    path('', views.index, name="home"),
    path('students/', views.get_students, name='get_students'),
    path('lecturers/', views.get_lecturers, name='get_lecturers'),
    path('groups/', views.get_groups, name='get_groups'),
    path('students/create_student/', views.get_student, name='create_student'),
    path('lecturers/create_lecturer/', views.get_lecturer, name='create_lecturer'),
    path('groups/create_group/', views.get_group, name='create_group'),
    path('students/<int:student_id>/edit/', cache_page(60 * 10)(views.edit_student), name='edit_student'),
    path('students/<int:student_id>/delete', views.delete_student, name='delete_student'),
    path('lecturers/<int:lecturer_id>/edit/', cache_page(60 * 10)(views.edit_lecturer), name='edit_lecturer'),
    path('lecturers/<int:lecturer_id>/delete', views.delete_lecturer, name='delete_lecturer'),
    path('groups/<int:group_id>/edit/', cache_page(60 * 10)(views.edit_group), name='edit_group'),
    path('groups/<int:group_id>/delete', views.delete_group, name='delete_group'),
    path('contact/', views.send_message, name='create_message'),
    path('accounts/login', views.index, name='login'),
    path('accounts/logout', views.index, name='logout')
]
