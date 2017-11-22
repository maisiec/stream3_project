# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from django.conf import settings
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.template import RequestContext
from django.contrib import messages, auth
from django.core.urlresolvers import reverse
from django.shortcuts import render, render_to_response, redirect, get_object_or_404
from django.template.context_processors import csrf
from django.contrib.auth.decorators import login_required
from accounts.forms import UserRegistrationForm, UserLoginForm
from orders.models import Purchase

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
 
            user = auth.authenticate(email=request.POST.get('email'),
                                     password=request.POST.get('password1'))
 
            if user:
                messages.success(request, "You have successfully registered")
                return redirect(reverse('account'))
 
            else:
                messages.error(request, "unable to log you in at this time!")
 
    else:
        form = UserRegistrationForm()
 
    args = {'form': form}
    args.update(csrf(request))
 
    return render(request, 'register.html', args)

@login_required(login_url='/login/')
def account(request):
    return render_to_response('account.html', {'list': orders.models.Purchase.objects.filter( purchaser=request.user)} )

def login(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            user = auth.authenticate(email=request.POST.get('email'),
                                    password=request.POST.get('password'))
 
            if user is not None:
                auth.login(request, user)
                messages.error(request, "You have successfully logged in")
                return redirect(reverse('account'))
            else:
                form.add_error(None, "Your email or password was not recognised")
 
    else:
        form = UserLoginForm()
 
    args = {'form':form}
    args.update(csrf(request))
    return render(request, 'login.html', args)

def logout(request):
    auth.logout(request)
    messages.success(request, 'You have successfully logged out')
    return render(request, 'index.html')