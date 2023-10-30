from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.http import HttpResponse
from TeamaGochi_Home.models import information

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
    mensaje= ""
    animalito=request.GET["code"]
    print(animalito)

    if animalito:
        try:
            mascota=information.objects.filter(idanimal=animalito)
            return render(request, "TeamaGochi_Home/recepcion_info.html", {"mascota":mascota, "query":animalito})
        except information.DoesNotExist:
            mensaje = "No hay animales con el código: %s" % animalito
    else:
            mensaje = "Por favor ingresa un código."

    return HttpResponse(mensaje)      