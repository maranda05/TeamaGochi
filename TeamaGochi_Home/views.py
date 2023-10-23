from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.http import HttpResponse
from TeamaGochi_Home.models import Information

# Create your views here.
def index(request):
    return render(request, "TeamaGochi_Home/index.html")

def term_and_condition(request):
    return render(request, "TeamaGochi_Home/term_and_condition.html")

def creators(request):
    return render(request, "TeamaGochi_Home/Creators.html")

@login_required
def settings(request):
    return render(request, "TeamaGochi_Home/settings.html")

def info(request):
    return render(request, "TeamaGochi_Home/animals_info.html")

def exit(request):
    logout(request)
    return redirect('/')

def formulario(request):
    return render(request, "TeamaGochi_Home/formulario.html")

def buscar(request):
    if request.GET["code"]:
        #mensaje="Animal asociado al código: %r" %request.GET["code"]
        animalito=request.GET["code"]
        mascota=Information.objects.filter(idanimal__icontains=animalito)
        return render(request, "TeamaGochi_Home/recepcion_info.html", {"mascota":mascota, "query":animalito}) #####Posible error
    else:
        mensaje="Por favor ingrese un código"
    return HttpResponse(mensaje)