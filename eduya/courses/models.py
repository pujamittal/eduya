from __future__ import unicode_literals

from django.db import models
from django.conf import settings

class Subject(models.Model):
    name = models.CharField(blank=False, max_length=50)
    abbreviation = models.CharField(primary_key=True, blank=False, max_length=50, unique=True)
    
    def __repr__ (self):
        return '<Subject %s>' % self.abbreviation

    def __str__ (self):
        return self.abbreviation

class Course(models.Model):
    subject = models.ForeignKey(Subject)
    title = models.CharField(blank=False, max_length=100)
    number = models.CharField(blank=False, max_length=50)
    
    def __repr__ (self):
        return '<Course %s>' % (self.subject.abbreviation + self.number)
        
    def __str__ (self):
        return str((self.subject.abbreviation + self.number))

class CourseSection(models.Model):
    course = models.ForeignKey(Course)
    crn = models.CharField(blank=False, max_length=250)
    section_type = models.CharField(blank=False, max_length=250)
    meetings = models.TextField()

class TeachingAssistant(models.Model):
    name = models.CharField(blank=False, max_length=250)
    email = models.EmailField()
    office = models.CharField(max_length=250)
    office_hours = models.CharField(max_length=250)
    
    def __repr__ (self):
        return '<TeachingAssistant %s>' % (self.email)
        
    def __str__ (self):
        return self.email

class Professor(models.Model):
    name = models.CharField(blank=False, max_length=250)
    email = models.EmailField()
    office = models.CharField(max_length=250)
    office_hours = models.CharField(max_length=250)
    website = models.CharField(max_length=250)
    
    def __repr__ (self):
        return '<Professor %s>' % (self.email)
        
    def __str__ (self):
        return self.email

class TeachingAssistantCourse(models.Model):
    course = models.ForeignKey(Course)
    teaching_assistant = models.ForeignKey(TeachingAssistant)

class ProfessorCourse(models.Model):
    course = models.ForeignKey(Course)
    professor = models.ForeignKey(Professor)
    
class ProfessorComment(models.Model):
    professor = models.ForeignKey(Professor)
    student = models.ForeignKey(settings.AUTH_USER_MODEL)
    text = models.TextField(null=True, max_length=250)
    
class CourseComment(models.Model):
    course = models.ForeignKey(Course)
    student = models.ForeignKey(settings.AUTH_USER_MODEL)
    text = models.TextField(null=True, max_length=250)    
    
class FileLinker(models.Model):
    typeOfInfo = models.CharField(max_length=20)
    infoLink = models.URLField()
    description = models.TextField(blank=True, null=True, max_length=250)

# class Review(models.Model):
#     course_section = models.ForeignKey(CourseSection)
#     author = models.ForeignKey(settings.AUTH_USER_MODEL)
#     datetime = models.DateTimeField(blank=False)
#     rating = models.SmallIntegerField(blank=False)
#     text = models.TextField(null=True, max_length=300)