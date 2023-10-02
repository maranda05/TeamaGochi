from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    return render(request, "TeamaGochi_Home/index.html")

def term_and_condition(request):
    return render(request, "TeamaGochi_Home/term_and_condition.html")

@login_required
def creators(request):
    return render(request, "TeamaGochi_Home/Creators.html")
