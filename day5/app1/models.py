from django.db import models


# Create your models here.
class Teacher(models.Model):
    teacher_id = models.CharField(max_length=11, primary_key=True)
    course_id = models.CharField(max_length=6)
