# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
def get_index(request):
   return render(request, 'index.html')

def about(request):
	return render(request, 'about/about.html')