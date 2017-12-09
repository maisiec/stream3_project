from django.shortcuts import render, redirect
from contact.forms import ContactForm
from django.core.mail import EmailMessage
from django.template import Context
from django.template.loader import get_template
# Create your views here.
def contact(request):
		contactForm= ContactForm

		if request.method == 'POST':
			form = contactForm(request.POST)
			if form.is_valid():
				full_name = request.POST.get('full_name', '')
			email = request.POST.get('email','')
			form_content = request.POST.get('content','')

			#Email profile with contact information 
        		template = get_template('contact/contact_template.txt')
        		context = Context({
        			'full_name': full_name,
        			'email': email,
        			'form_content' : form_content,
        			})
        		content = template.render(context)

        		email = EmailMessage(
	        		"New contact form submission",
	        		content, 
	        		"Your website" + '',
	        		['maaisiexx@gmail.com'],
	        		headers = {'Reply_To': email }
        		)
        		email.send()
        		return redirect('contact')  

		return render(request, 'contact/contact.html', {
        'form': contactForm,
    })
        	