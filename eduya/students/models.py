from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

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
        if is_tutor is None:
            raise ValueError('Is tutor must be set')
        
        user = self.model(
            email=self.normalize_email(email),
            password=password,
            first_name=first_name,
            last_name=last_name,
            is_tutor=is_tutor)
            
        user.is_admin = True
        user.save(using=self._db)
        return user
            
        
# Custom Student model, an extension of AbstractBaseUser
class Student(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True, null=True, blank=False)
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

    