from django import forms

class ContactForm(forms.Form):
	full_name = forms.CharField(required=True, widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Full Name'}))
	email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={'class':'form-control','placeholder':'Email'}))
	content = forms.CharField(
		required=True,
		widget=forms.Textarea
	)

	def __init__(self, *args, **kwargs):
		super(ContactForm, self).__init__(*args, **kwargs)
		self.fields['full_name'].label = "Your name:"
		self.fields['email'].label = "Your email:"
		self.fields['content'].label = "Say Hello"