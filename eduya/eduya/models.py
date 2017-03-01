from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

class StudentManager(BaseUserManager):
    
    def create_user(self, email, password, fname, lname, is_tutor):
        if email is None:
            raise ValueError('Email must be set')
        if password is None:
            raise ValueError('Password must be set')
        if fname is None:
            raise ValueError('First name must be set')
        if lname is None:
            raise ValueError('Last name must be set')
        if is_tutor is None:
            raise ValueError('is_tutor must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, fname=fname, lname=lname, is_tutor=is_tutor)
        user.set_password(password)
        user.save(using=self._db)
        return user
        
    def create_superuser(self, email, password, fname, lname, is_tutor):
        if email is None:
            raise ValueError('Email must be set')
        if password is None:
            raise ValueError('Password must be set')
        if fname is None:
            raise ValueError('First name must be set')
        if lname is None:
            raise ValueError('Last name must be set')
        if is_tutor is None:
            raise ValueError('is_tutor must be set')
        if is_superuser is None:
            raise ValueError('is_superuser must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, fname=fname, lname=lname, is_tutor=is_tutor)
        user.is_superuser = True
        user.set_password(password)
        user.save(using=self._db)
        return user
        

# Create your models here.
class Student(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True, blank=False)
    password = models.CharField(blank=False)
    fname = models.CharField(blank=False)
    lname = models.CharField(blank=False)
    is_tutor = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    
    objects = StudentManager()
    
    REQUIRED_FIELDS = ['fname', 'lname', 'is_tutor', "is_superuser"]
    USERNAME_FIELD = 'email'
    
    def get_short_name(self):
        return self.fname
    
    def get_long_name(self):
        return str(self.fname + self.lname)
    
    def __str__(self):
        return '<Student %s>' % self.email 
