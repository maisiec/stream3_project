
from django.test import TestCase
from .forms import ContactForm
from django import forms
from django.conf import settings

class ContactTest(TestCase):

    def test_contact_form(self):
        form = ContactForm({
            'full_name': 'Test Name',
            'email': 'test@test.com',
            'content': 'test test test test test',
        })
 
        self.assertTrue(form.is_valid())

    def test_contact_form_with_missing_email(self):
        form = ContactForm({
            'full_name': 'Test Name',
            'content': 'test test test test test',
        })
        self.assertFalse(form.is_valid())
        self.assertRaisesMessage(forms.ValidationError,
                                 "Please enter your email address",
                                 form.full_clean())

    def test_contact_form_with_missing_full_name(self):
        form = ContactForm({
            'email': 'test@test.com',
            'content': 'test test test test test',
        })
        self.assertFalse(form.is_valid())
        self.assertRaisesMessage(forms.ValidationError,
                                 "Please enter your full name",
                                 form.full_clean())

    def test_contact_form_with_missing_full_name(self):
        form = ContactForm({
            'full_name': 'Test Name',
            'email': 'test@test.com',
        })
        self.assertFalse(form.is_valid())
        self.assertRaisesMessage(forms.ValidationError,
                                 "You need to enter a message",
                                 form.full_clean())