from django import forms
from .models import Order

class OrderCreateForm(forms.ModelForm):
	email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control','placeholder':'Email'}))
	first_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'First Name'}))
	last_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Last Name'}))
	class Meta:
		model = Order 
		fields = ['first_name', 'last_name', 'email']