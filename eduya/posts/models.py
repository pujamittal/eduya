from __future__ import unicode_literals

from django.db import models
from django.conf import settings

class Post(models.Model):
    student = models.ForeignKey(settings.AUTH_USER_MODEL)
    student_name = models.CharField(blank=False, max_length = 256, default="John Doe");
    subject = models.CharField(blank=False, max_length=50)
    course = models.CharField(blank=False, max_length=50)
    location = models.CharField(blank=False, max_length=50)
    datetime = models.DateTimeField(blank=False)
    price = models.DecimalField(default=7.25, max_digits=5, decimal_places=2)
    notes = models.TextField(null=True, max_length=250)