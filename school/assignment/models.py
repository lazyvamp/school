from django.db import models

# Create your models here.

class Assignment(models.Model):
    question = models.CharField(max_length=40, null=False, blank=False)
    answer = models.CharField(max_length=400, null=False, blank=False)