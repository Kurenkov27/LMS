import csv

from django.contrib import admin
from django.db import models
from django.http import HttpResponse
from djrichtextfield.widgets import RichTextWidget

from .models import Group, Lecturer, Student


# Register your models here.
# admin.site.register(Student)
# admin.site.register(Lecturer)
# admin.site.register(Group)


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.TextField: {'widget': RichTextWidget}
    }

    actions = ['export']

    def export(self, request, queryset):
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="students.csv"'
        writer = csv.writer(response)
        header = ['First name', 'Last name', 'Email']
        writer.writerow(header)
        for student in queryset:
            row = [student.first_name, student.last_name, student.email]
            writer.writerow(row)
        return response

    export.short_description = 'Export students'


@admin.register(Lecturer)
class LecturerAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.TextField: {'widget': RichTextWidget}
    }

    actions = ['export']

    def export(self, request, queryset):
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="lecturers.csv"'
        writer = csv.writer(response)
        header = ['First name', 'Last name', 'Email']
        writer.writerow(header)
        for lecturer in queryset:
            row = [lecturer.first_name, lecturer.last_name, lecturer.email]
            writer.writerow(row)
        return response

    export.short_description = 'Export lecturers'


@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.TextField: {'widget': RichTextWidget}
    }

    actions = ['export']

    def export(self, request, queryset):
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="groups.csv"'
        writer = csv.writer(response)
        header = ['Course name', 'Lecturer', 'Amount of students']
        writer.writerow(header)
        for group in queryset:
            row = [group.course, group.teacher.__str__(), group.students.count()]
            writer.writerow(row)
        return response

    export.short_description = 'Export groups'
