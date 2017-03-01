from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django import forms
from .models import Student

class registerForm(forms.Form):
	username = forms.CharField(label='username',widget=forms.TextInput, required=True)
	email = forms.CharField(label='email', widget=forms.EmailInput, required=True)
	password = forms.CharField(label='password', widget=forms.PasswordInput, required=True)
	tutor = forms.CharField(label='tutor', widget=forms.CheckboxInput, required=False) 
