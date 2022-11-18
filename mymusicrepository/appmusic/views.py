from django.shortcuts import render
from appmusic.models import *
from appmusic.forms import *
# Create your views here.


def index(request):
    return render(request, "appmusic/index.html")

def artistas(request):
    return render(request, "appmusic/artistas.html")

def artistas_create(request):
    return render(request, "appmusic/artistas_form.html")

def canciones(request):
    return render(request, "appmusic/canciones.html")

def canciones_create(request):
    return render(request, "appmusic/canciones_form.html")

def albums(request):
    return render(request, "appmusic/albums.html")

def albums_create(request):
    return render(request, "appmusic/albums_form.html")

def search(request):
    return render(request, "appmusic/search.html")

def search_result(request):
    return render(request, "appmusic/search_result.html")


