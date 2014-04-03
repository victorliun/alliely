# Create your views here.
from django.http import HttpResponseRedirect
from django.shortcuts import render,redirect
from django.template import RequestContext
from django.contrib.auth import authenticate, login, logout
from django.core.urlresolvers import reverse

def login_view(request):
    """this view has been replaced by django default view"""
    logout(request)
    username = password = ''
    if request.POST:
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                assert request.POST['next']
                redirect_url = request.POST.get("next", reverse("home"))
                return HttpResponseRedirect(redirect_url)
    return render(request, 'auth/login.html')

def logout_view(request):
    logout(request)
    # redirect to success url
    return HttpResponseRedirect(reverse("home"))