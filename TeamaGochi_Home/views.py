from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.http import HttpResponse, HttpResponseRedirect
from TeamaGochi_Home.models import information
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect, get_object_or_404


# Create your views here.
def inicio(request):
    return render(request, "TeamaGochi_Home/inicio.html")

def register(request):
    data = {
        "form": CustomUserCreationForm()
    }
    if request.method == "POST":
        formulario = CustomUserCreationForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()   
            user = authenticate(username=formulario.cleaned_data["username"], password=formulario.cleaned_data["password1"])
            login(request,user)
            return redirect("../index")
        data["form"] = formulario
    return render(request, "registration/register.html",data)

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

def formulario(request):
    return render(request, "TeamaGochi_Home/formulario.html")

def almacenar_informacion_animales(codigo):
    try:
        # Crea una instancia del modelo 'Animal' con el código proporcionado
        nuevo_animal = information(codigo=codigo)

        # Guarda el nuevo animal en la base de datos
        nuevo_animal.save()

        print(f"Se ha almacenado la información del animal con código {codigo} en 'animales'.")
    except Exception as e:
        print(f"Error al almacenar la información en 'animales': {e}")
        
def buscar(request):
    mensaje= ""
    animalito=request.GET["code"]

    if animalito:
        try:
            mascota=information.objects.filter(codigos=animalito)
            return render(request, "TeamaGochi_Home/recepcion_info.html", {"mascota":mascota, "query":animalito})
        except information.DoesNotExist:
            mensaje = "No hay animales con el código: %s" % animalito
    else:
            mensaje = "Por favor ingresa un código."

    almacenar_informacion_animales(animalito)
    return HttpResponse(mensaje)   


def quienes_somos(request):
    return render(request, "TeamaGochi_Home/who_we_are.html")

class CustomUserCreationForm(UserCreationForm):
    pass


