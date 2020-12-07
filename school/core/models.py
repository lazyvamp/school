from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import Group, Permission


admin_group, created = Group.objects.get_or_create(name='Admin')
techer_group, created = Group.objects.get_or_create(name='Teacher')
student_group, created = Group.objects.get_or_create(name='Student')



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
      FACULTY_ROLES = [ADMIN, TEACHER]
      first_name = models.CharField(max_length=20, blank=False)
      last_name = models.CharField(max_length=20)
      email = models.EmailField(null= False, blank= False)
      phone_number = models.CharField(blank=False, null=True, max_length=10)
      role = models.CharField(max_length=20, choices=ROLE_CHOICES, blank=False, null=False)

      class Meta:
        permissions = (

           ("can_add_teacher", "can add teacher"),
           ("can_add_student", "can add student"),
      )

std = Permission.objects.get(codename='can_add_student')
tchr = Permission.objects.get(codename='can_add_teacher')

admin_group.permissions.add(tchr, std)
techer_group.permissions.add(std)