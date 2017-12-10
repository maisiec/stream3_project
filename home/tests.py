# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase
from home.views import get_index
from django.core.urlresolvers import resolve
from django.shortcuts import render_to_response
from accounts.models import User

# Create your tests here.
class HomePageTest(TestCase):
    def test_home_page_resolves(self):
        home_page = resolve('/')
        self.assertEqual(home_page.func, get_index)

    def test_check_content_is_correct(self):
        home_page = self.client.get('/')
        self.assertTemplateUsed(home_page, "index.html")
        home_page_template_output = render_to_response("index.html").content
        self.assertEqual(home_page.content, home_page_template_output)

    def test_home_page_uses_index_view(self):
        home_page = resolve('/')
        self.assertEqual(home_page.func, get_index)
 
    def test_home_page_uses_index_template(self):
        home_page = self.client.get('/')
        self.assertTemplateUsed(home_page, "index.html")