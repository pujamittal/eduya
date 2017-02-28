from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class Student(AbstractUser):
    email = models.EmailField(blank=False)
    canTutor = models.BooleanField(default=False)
