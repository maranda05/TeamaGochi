from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

# Create your views here.
@login_required
def index(request):
    return render(request, "TeamaGochi_Home/index.html")

def term_and_condition(request):
    return render(request, "TeamaGochi_Home/term_and_condition.html")

def creators(request):
    return render(request, "TeamaGochi_Home/Creators.html")

def settings(request):
    return render(request, "TeamaGochi_Home/settings.html")

def info(request):
    return render(request, "TeamaGochi_Home/animals_info.html")

def exit(request):
    logout(request)
    return redirect('/')
