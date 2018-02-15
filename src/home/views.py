# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.http import Http404
from .forms import RegistrationForm
from django.contrib import messages
from django.http import HttpResponseRedirect

# Create your views here.
def index(request):
	return render(request, 'home/home.html')


# Create your views here.
def land(request):
	return render(request, 'home/home.html')

# Create your views here.
def team(request):
	return render(request, 'home/team.html')


def events(request):
	return render(request, 'home/events.html')


def gallery(request):
	return render(request, 'home/gallery.html')

def about(request):
	return render(request, 'home/about.html')

def contact(request):
	return render(request, 'home/contact.html')

def thanks(request):
	return render(request, 'home/thanks.html')

def register(request):
	form = RegistrationForm(request.POST or None)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.save()
		messages.success(request, "Thank you for Rgistration, Your Registration has been successfully submitted. We'll contact you soon. :)" )
		return HttpResponseRedirect("/register")
	context = {'form' : form}
	return render(request, 'home/register.html',context)

