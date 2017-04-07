from django import forms
from .models import Student

class registerForm(forms.Form):
    # Setting char fields

    email = forms.CharField(label='email', widget=forms.EmailInput, required=True)
    first_name = forms.CharField(label='first_name', widget=forms.TextInput, required=True)
    last_name = forms.CharField(label='last_name', widget=forms.TextInput, required=True)
    password = forms.CharField(label='password', widget=forms.PasswordInput, required=True)
    confirmpassword = forms.CharField(label='confirmpassword', widget=forms.PasswordInput, required=True)
    is_tutor = forms.BooleanField(label='is_tutor', widget=forms.CheckboxInput, required=False)	
    

    def clean_password2(self): 
        password = self.cleaned_data.get("password")
        confirmpassword = self.cleaned_data.get("confirmpassword")
        if password and confirmpassword and password != confirmpassword:
            raise forms.ValidationError("Passwords don't match")
        return password


    # cleans email, checks that email hasn't been taken
    def clean_email(self): 
        email = self.cleaned_data.get("email")
        try:
            exists = Student.objects.get(email=email)
            raise forms.ValidationError("Sorry, this email has already been taken")
        except Student.DoesNotExist:
            return email
        except:
            raise forms.ValidationError("Sorry, an unexpected error occured")
           
            
class loginForm(forms.Form):
    email = forms.CharField(label='email', widget=forms.EmailInput, required=True)
    password = forms.CharField(label='password', widget=forms.PasswordInput, required=True)

   
class reviewForm(forms.Form):
    mOne= 1
    mTwo = 2
    mThree = 3
    mFour = 4
    mFive = 5
    SKILLCHOICES = (
        (mOne,'$'), 
        (mTwo,'$$'), 
        (mThree,'$$$'),
    )
    MONEYCHOICES = (
        (mOne), 
        (mTwo), 
        (mThree), 
        (mFour), 
        (mFive),
    )
    skills = forms.ChoiceField(label='skills', widget=forms.RadioSelect, choices=SKILLCHOICES, required=False)
    money = forms.ChoiceField(label='money', widget=forms.RadioSelect, choices=MONEYCHOICES, required=False)
    notes = forms.CharField(label='notes', widget=forms.TextInput, required=False)
    
"""
class updateForm(forms.ModelForm):
    email = forms.CharField(label='email', widget=forms.EmailInput, required=True)
    first_name = forms.CharField(label='first_name', widget=forms.TextInput, required=True)
    last_name = forms.CharField(label='last_name', widget=forms.TextInput, required=True)
    password = forms.CharField(label='password', widget=forms.PasswordInput, required=True)
    confirmpassword = forms.CharField(label='confirmpassword', widget=forms.PasswordInput, required=True)
    
    class Meta:
        model = Student
        fields = ('email', 'password', 'first_name', 'last_name')
    
    def clean_password2(self): 
        password = self.cleaned_data.get("password")
        confirmpassword = self.cleaned_data.get("confirmpassword")
        if password and confirmpassword and password != confirmpassword:
            raise forms.ValidationError("Passwords don't match")
        return password


    # cleans email, checks that email hasn't been taken
    def clean_email(self): 
        email = self.cleaned_data.get("email")
        try:
            exists = Student.objects.get(email=email)
            raise forms.ValidationError("Sorry, this email has already been taken")
        except Student.DoesNotExist:
            return email
        except:
            raise forms.ValidationError("Sorry, an unexpected error occured")
"""