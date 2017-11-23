from django import forms
from django.contrib.auth.forms import UserCreationForm
from accounts.models import User
from django.core.exceptions import ValidationError 
 
class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control','placeholder':'Email'}))
    password1 = forms.CharField(
        label='Password',
        widget=forms.PasswordInput
    (attrs={'class':'form-control','placeholder':'Password'}))
 
    password2 = forms.CharField(
        label='Confirm Password',
        widget=forms.PasswordInput
    (attrs={'class':'form-control','placeholder':'Confirm Password'}))
 
    class Meta:
        model = User
        fields = ['email', 'password1', 'password2']
        exclude = ['username']
 
    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
 
        if password1 and password2 and password1 != password2:
            message = "Passwords do not match"
            raise ValidationError(message)
 
        return password2
 
    def save(self, commit=True):
        instance = super(UserRegistrationForm, self).save(commit=False)
 
        # automatically set to email address to create a unique identifier
        instance.username = instance.email
 
        if commit:
            instance.save()
 
        return instance

class UserLoginForm(forms.Form):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control','placeholder':'Email'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Password'}))