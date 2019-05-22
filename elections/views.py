from django.shortcuts import render
from django.urls import path
from django.conf.urls import url
from django.http import HttpResponse
from django.template import loader


def home(request):
	return render(request, 'elections/home.html')