from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class BaseUser(AbstractUser):
      ADMIN = 'admin'
      TEACHER = 'teacher'
      STUDENT = 'student'
      ROLE_CHOICES = (
            (ADMIN, 'admin'),
            (TEACHER, 'teacher'),
            (STUDENT, 'student')
      )
      first_name = models.CharField(max_length=20, blank=False)
      last_name = models.CharField(max_length=20)
      email = models.EmailField(null= False, blank= False)
      phone_number = models.CharField(blank=False, null=True, max_length=10)
      role = models.CharField(max_length=20, choices=ROLE_CHOICES, blank=False, null=False)