from django import forms
from .models import Order

class OrderCreateForm(forms.ModelForm):
	email = forms.EmailField(widget=forms.EmailInput(attrs={'id':'order_email','placeholder':'Email'}))
	first_name = forms.CharField(widget=forms.TextInput(attrs={'id':'first_name','placeholder':'First Name'}))
	last_name = forms.CharField(widget=forms.TextInput(attrs={'id':'last_name','placeholder':'Last Name'}))
	class Meta:
		model = Order 
		fields = ['first_name', 'last_name', 'email']