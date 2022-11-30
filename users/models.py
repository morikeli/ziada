from django.contrib.auth.models import User
from django.db import models
from PIL import Image

class Students(models.Model):
    id = models.CharField(max_length=18, primary_key=True, unique=True, editable=False)
    student = models.OneToOneField(User, on_delete=models.CASCADE, editable=False)
    gender = models.CharField(max_length=7, blank=False)
    phone_number = models.CharField(max_length=13, blank=False)
    course = models.CharField(max_length=100, blank=False)
    school = models.CharField(max_length=70, blank=False)
    reg_no = models.CharField(max_length=14, blank=False)
    year = models.CharField(max_length=12, blank=False)
    semester = models.CharField(max_length=1, blank=False)
    profile_pic = models.ImageField(upload_to='Students-Dps/', default='default.png')
    is_student = models.BooleanField(default=False, editable=False)
    is_prefect = models.BooleanField(default=False, editable=False)
    created = models.DateTimeField(auto_now_add=True)
    edited = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.student}'

    def save(self, *args, **kwargs):
        super(Students, self).save(*args, **kwargs)

        student_dp = Image.open(self.profile_pic.path)

        if student_dp.height > 400 and student_dp.width > 400:
            output_size = (400, 400)
            student_dp.thumbnail = output_size
            student_dp.save(self.profile_pic.path)


    class Meta:
        verbose_name_plural = 'Students'
        ordering = ['reg_no']


class Assignments(models.Model):
    id = models.CharField(max_length=18, primary_key=True, unique=True, editable=False)
    name = models.ForeignKey(Students, on_delete=models.CASCADE, editable=False)
    unit = models.CharField(max_length=70, blank=False)
    document = models.FileField(upload_to='Assignments/', null=False)
    uploaded = models.DateTimeField(auto_now_add=True)
    edited = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name_plural = 'Assignments'
        ordering = ['-uploaded']


class Lecturers(models.Model):
    id = models.CharField(max_length=18, primary_key=True, unique=True, editable=False)
    lec = models.OneToOneField(User, on_delete=models.CASCADE, editable=False)
    title = models.CharField(max_length=5)
    gender = models.CharField(max_length=7, blank=False)
    phone_number = models.CharField(max_length=14, blank=False)
    profile_pic = models.ImageField(upload_to='Lecturer-Dps/', default='default.png')
    is_lecturer = models.BooleanField(default=False, editable=False)
    unit = models.CharField(max_length=70, blank=False)
    created = models.DateTimeField(auto_now_add=True)
    edited = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.lec}'

    def save(self, *args, **kwargs):
        super(Lecturers, self).save(*args, **kwargs)

        lec_dp = Image.open(self.profile_pic.path)

        if lec_dp.height > 400 and lec_dp.width > 400:
            output_size = (400, 400)
            lec_dp.thumbnail = output_size
            lec_dp.save(self.profile_pic.path)
        

    class Meta:
        verbose_name_plural = 'Lecturers'
        ordering = ['lec']

