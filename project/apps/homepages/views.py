# Create your views here.
from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.template import RequestContext
from django.contrib.auth.decorators import login_required

@login_required()
def rose(request, *args, **kwargs):
	"""
	Display the home page of my site.
	"""
	template = "base/home.html"
	return render_to_response(template, context_instance=RequestContext(request))