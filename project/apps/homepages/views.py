from django.shortcuts import render_to_response
from django.http import HttpResponse

# Create your views here.
def rose(request, *args, **kwargs):
	"""
	Display the home page of my site.
	"""
	template = "base/rose.html"
	return render_to_response(template)