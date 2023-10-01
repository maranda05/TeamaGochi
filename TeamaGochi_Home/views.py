from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "TeamaGochi_Home/index.html")

def term_and_condition(request):
    return render(request, "TeamaGochi_Home/term_and_condition.html")

def creators(request):
    return render(request, "TeamaGochi_Home/Creators.html")