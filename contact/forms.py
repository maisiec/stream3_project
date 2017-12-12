from django import forms

class ContactForm(forms.Form):
	full_name = forms.CharField(required=True, widget=forms.TextInput(attrs={'class':'form-style','placeholder':'Full Name'}))
	email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={'class':'form-style','placeholder':'Email'}))
	content = forms.CharField(
		required=True,
		widget=forms.Textarea
	(attrs={'class':'form-style','placeholder':'Enter your message here'}))

	def __init__(self, *args, **kwargs):
		super(ContactForm, self).__init__(*args, **kwargs)
		self.fields['full_name'].label = "Your name:"
		self.fields['email'].label = "Your email:"
		self.fields['content'].label = "Say Hello"