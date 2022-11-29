from django.contrib.auth.models import User
from django.db import models


class Students(models.Model):
    id = models.CharField(max_length=18, primary_key=True, unique=True, editable=False)
    student = models.OneToOneField(User, on_delete=models.CASCADE, editable=False)
    gender = models.CharField(max_length=7, blank=False)
    phone_number = models.CharField(max_length=13, blank=False)
    course = models.CharField(max_length=100, blank=False)
    school = models.CharField(max_length=70, blank=False)
    year = models.CharField(max_length=12, blank=False)
    semester = models.CharField(max_length=1, blank=False)
    profile_pic = models.ImageField(upload_to='Students-Dps/', default='default.png')
    is_student = models.BooleanField(default=False, editable=False)
    is_prefect = models.BooleanField(default=False, editable=False)
    created = models.DateTimeField(auto_now_add=True)
    edited = models.DateTimeField(auto_now=True)

class Assignments(models.Model):
    name = models.ForeignKey(Students, on_delete=models.CASCADE, editable=False)
    unit = models.CharField(max_length=70, blank=False)
    