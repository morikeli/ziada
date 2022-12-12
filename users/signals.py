from django.db.models.signals import pre_save, post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Students, Assignments, Lecturers
import uuid


@receiver(pre_save, sender=Students)
def generate_StudentId(sender, instance, **kwargs):
    if instance.id == "":
        instance.id = str(uuid.uuid4()).replace('-', '')[:18]

@receiver(pre_save, sender=Assignments)
def generate_StudentId(sender, instance, **kwargs):
    if instance.id == "":
        instance.id = str(uuid.uuid4()).replace('-', '')[:18]

@receiver(pre_save, sender=Lecturers)
def generate_StudentId(sender, instance, **kwargs):
    if instance.id == "":
        instance.id = str(uuid.uuid4()).replace('-', '')[:18]


@receiver(post_save, sender=User)
def create_student_profile(sender, instance, created, **kwargs):
    if created:
        if instance.is_staff is False and instance.is_superuser is False:
            # if instance.is_student is False and instance.is_prefect is False:
            Students.objects.create(student=instance)


