from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404
from .forms import forms
from django.template import loader
import datetime, time

# Create your views here.
def home(request):
	context = {}
	template = loader.get_template('home.html')
	return HttpResponse(template.render(context,request))
def contact(request):
        context = {}
        template = loader.get_template('contact.html')
        return HttpResponse(template.render(context,request))
def about(request):
        context = {}
        template = loader.get_template('about.html')
        return HttpResponse(template.render(context,request))
