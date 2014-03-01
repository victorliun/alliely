from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def site_home(request, *args, **kwargs):
	"""
	Display the home page of my site.
	"""

	return HttpResponse("<h1>Welcome to my site.</h1>")