from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from django.views.generic.base import TemplateView


# Create your views here.
class HomeView(TemplateView):
	template_name = "login.html"
		