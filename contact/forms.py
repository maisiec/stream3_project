from django import forms

class ContactForm(forms.Form):
	full_name = forms.CharField(required=True, widget=forms.TextInput(attrs={'id':'full_name','placeholder':'Full Name'}))
	email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={'id':'email','placeholder':'Email'}))
	content = forms.CharField(
		required=True,
		widget=forms.Textarea
	(attrs={'id':'text_area','placeholder':'Enter your message here'}))

	def __init__(self, *args, **kwargs):
		super(ContactForm, self).__init__(*args, **kwargs)
		self.fields['full_name'].label = "Your name:"
		self.fields['email'].label = "Your email:"
		self.fields['content'].label = "Say Hello"