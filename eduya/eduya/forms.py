from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django import forms
from .models import Student

class registerForm(forms.Form):
	# Setting char fields
	email = forms.CharField(label='email', widget=forms.EmailInput, required=True)
	fname = forms.CharField(label='fname', widget=forms.TextInput, required=True)
	lname = forms.CharField(label='lname', widget=forms.TextInput, required=True)
	password = forms.CharField(label='password', widget=forms.PasswordInput, required=True)
	confirmpassword = forms.CharField(label='confirmpassword', widget=forms.PasswordInput, required=True)
	tutor = forms.CharField(label='tutor', widget=forms.CheckboxInput, required=False)
	
	# checks that passwords match/cleans them
	def clean_password(self): 
        password = self.cleaned_data.get("password")
        confirmpassword = self.cleaned_data.get("confirmpassword")
        if password and confirmpassword and password != confirmpassword:
            raise forms.ValidationError("Passwords don't match")
        return password
    # cleans email, checks that email hasn't been taken
    def clean_email(self): 
        email = self.cleaned_data.get("email")
        try:
            exists = MyUser.objects.get(email=email)
            raise forms.ValidationError("Sorry, this email has already been taken")
        except MyUser.DoesNotExist:
            return email
        except:
            raise forms.ValidationError("Sorry, an unexpected error occured")
