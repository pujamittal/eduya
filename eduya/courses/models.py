from __future__ import unicode_literals

from django.db import models
from django.conf import settings

class Subject(models.Model):
    name = models.CharField(blank=False, max_length=50, primary_key=True)
    
class Course(models.Model):
    subject = models.ForeignKey(Subject)
    title = models.CharField(blank=False, max_length=100)
    course_id = models.CharField(blank=False, max_length=50, primary_key=True)
    
class CourseSection(models.Model):
    course = models.ForeignKey(Course)
    rooms =  models.CharField(blank=False, max_length=250)
    times =  models.CharField(blank=False, max_length=250)

class TeachingAssistant(models.Model):
    name = models.CharField(blank=False, max_length=250)
    email = models.EmailField()
    office = models.CharField(max_length=250)
    office_hours = models.CharField(max_length=250)

class Professor(models.Model):
    name = models.CharField(blank=False, max_length=250)
    email = models.EmailField()
    office = models.CharField(max_length=250)
    office_hours = models.CharField(max_length=250)
    website = models.CharField(max_length=250)

class Review(models.Model):
    course_section = models.ForeignKey(CourseSection)
    author = models.ForeignKey(settings.AUTH_USER_MODEL)
    datetime = models.DateTimeField(blank=False)
    rating = models.SmallIntegerField(blank=False)
    text = models.TextField(null=True, max_length=300)