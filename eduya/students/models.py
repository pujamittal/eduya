from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin, User
from django.db.models import Avg
from django.contrib.auth.admin import UserAdmin
from django.contrib import admin
from courses.models import Course

# Custom Manager for Student model
class StudentManager(BaseUserManager):
    def create_user(self, email, password, first_name, last_name, is_tutor):
        
        # Check if all fields are set
        if email is None:
            raise ValueError('Email must be set')
        if password is None:
            raise ValueError('Password must be set')
        if first_name is None:
            raise ValueError('First name must be set')
        if last_name is None:
            raise ValueError('Last name must be set')
        if is_tutor is None:
            raise ValueError('Is tutor must be set')
       
        user = self.model(
            email=self.normalize_email(email),
            first_name=first_name,
            last_name=last_name,
            is_tutor=is_tutor)
        user.set_password(password)
        user.save(using=self._db)
        if is_tutor == True:
            Tutor.objects.create(studentLink = user, tutor_name = str(first_name + " " + last_name))
        return user
        
    def create_superuser(self, email, password, first_name, last_name, is_tutor):
        
        # Check if all fields are set
        if email is None:
            raise ValueError('Email must be set')
        if password is None:
            raise ValueError('Password must be set')
        if first_name is None:
            raise ValueError('First name must be set')
        if last_name is None:
            raise ValueError('Last name must be set')
        
        
        user = self.create_user(
            email=self.normalize_email(email),
            password=password,
            first_name=first_name,
            last_name=last_name,
            is_tutor=is_tutor)
            
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
            
        user.save(using=self._db)
        return user
            
        
# Custom Student model, an extension of AbstractBaseUser
class Student(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True, null=True, blank=False)
    password = models.CharField(blank=False, max_length=256)
    first_name = models.CharField(blank=False, max_length=30)
    last_name = models.CharField(blank=False, max_length=30)
    is_tutor = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    objects = StudentManager()
    
    REQUIRED_FIELDS = ['first_name', 'last_name', 'is_tutor']
    USERNAME_FIELD = 'email'
    
    def get_short_name(self):
        return self.first_name
    
    def get_long_name(self):
        return str(self.first_name + " " + self.last_name)

    def __str__(self):
        return '<Student %s>' % self.email 
        
class StudentAdmin(UserAdmin):
    pass

class Tutor(models.Model):
    studentLink = models.OneToOneField( Student, on_delete=models.CASCADE, primary_key = True,)
    tutor_name = models.CharField(blank=False, max_length = 256, default="John Doe");
    skillRating = models.FloatField(default=0)
    moneyRating = models.FloatField(default=0)
    numRatings = models.PositiveSmallIntegerField(default=0)

    def __str__(self):
        return self.studentLink.email

class TutorCourse(models.Model):
    tutor = models.ForeignKey(Tutor)
    course = models.ForeignKey(Course)        
        
class Review(models.Model):
    tutor = models.ForeignKey(Tutor, on_delete=models.CASCADE, related_name='tutorReview')
    reviewer_name = models.CharField(blank=True, max_length = 256, default="Anonymous");
    skillRating = models.PositiveSmallIntegerField(default=0)
    moneyRating = models.PositiveSmallIntegerField(default=0)
    notes = models.TextField(null=False, max_length=500)
