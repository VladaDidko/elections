from django.shortcuts import render
from django.urls import path
from django.conf.urls import url
from django.http import HttpResponse

def home(request):
	return HttpResponse("<h1>HI there</h1>")

def home1(request):
	return render(request, 'elections/home.html')