from django.urls import path

from . import views


urlpatterns = [
    path('', views.index),
    path('students', views.get_students),
    path('lecturers', views.get_lecturers),
    path('groups', views.get_groups),
    path('students/create_student/', views.get_student),
    path('lecturers/create_lecturer/', views.get_lecturer),
    path('groups/create_group/', views.get_group)
]
