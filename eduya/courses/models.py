from __future__ import unicode_literals

from django.db import models
from django.conf import settings

class Subject(models.Model):
    name = models.CharField(blank=False, max_length=50)
    abbreviation = models.CharField(primary_key=True, blank=False, max_length=50, unique=True)

class Course(models.Model):
    subject = models.ForeignKey(Subject)
    title = models.CharField(blank=False, max_length=100)
    number = models.CharField(blank=False, max_length=50)

class CourseSection(models.Model):
    course = models.ForeignKey(Course)
    crn = models.CharField(blank=False, max_length=250)
    section_type = models.CharField(blank=False, max_length=250)
    meetings = models.TextField()

# class TeachingAssistant(models.Model):
#     name = models.CharField(blank=False, max_length=250)
#     email = models.EmailField()
#     office = models.CharField(max_length=250)
#     office_hours = models.CharField(max_length=250)

# class Professor(models.Model):
#     name = models.CharField(blank=False, max_length=250)
#     email = models.EmailField()
#     office = models.CharField(max_length=250)
#     office_hours = models.CharField(max_length=250)
#     website = models.CharField(max_length=250)

# class Review(models.Model):
#     course_section = models.ForeignKey(CourseSection)
#     author = models.ForeignKey(settings.AUTH_USER_MODEL)
#     datetime = models.DateTimeField(blank=False)
#     rating = models.SmallIntegerField(blank=False)
#     text = models.TextField(null=True, max_length=300)