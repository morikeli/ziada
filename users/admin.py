from django.contrib import admin
from .models import Students, Assignments, Lecturers


@admin.register(Students)
class StudentsTable(admin.ModelAdmin):
    list_display = ['student', 'reg_no', 'school', 'is_prefect', 'created']
    readonly_fields = ['gender', 'phone_number', 'course', 'reg_no', 'school', 'year', 'semester', 'profile_pic']
    fields = ['gender', 'phone_number', 'course', 'reg_no', 'school', 'year', 'semester', 'profile_pic']

@admin.register(Assignments)
class AssignmentsTable(admin.ModelAdmin):
    list_display = ['name', 'unit', 'uploaded']
    readonly_fields = ['unit', 'document']
    fields = ['name', 'unit', 'document']

@admin.register(Lecturers)
class LecturersTable(admin.ModelAdmin):
    list_display = ['lec', 'unit', 'is_lecturer', 'created']
    readonly_fields = ['title', 'gender', 'phone_number', 'unit']
    fields = ['profile_pic', 'title', 'gender', 'phone_number', 'unit']
