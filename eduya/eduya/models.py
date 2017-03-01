from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

class StudentManager(BaseUserManager):
    def _create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError('Email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)
        
    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_superuser', True)
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')
        return self._create_user(email, password, **extra_fields)

# Create your models here.
class Student(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True, blank=False)
    password = models.CharField(blank=False)
    first_name = models.CharField(blank=False)
    last_name = models.CharField(blank=False)
    is_tutor = models.BooleanField(default=False)
    
    objects = StudentManager()
    
    REQUIRED_FIELDS = ['first_name', 'last_name', 'is_tutor']
    USERNAME_FIELD = 'email'
    
    def get_short_name(self):
        return self.first_name
    
    def get_long_name(self):
        return str(self.first_name + self.last_name)
    
    def __str__(self):
        return '<Student %s>' % self.email 
