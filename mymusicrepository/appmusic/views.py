from django.shortcuts import render
from appmusic.models import *
from appmusic.forms import *
# Create your views here.


def index(request):
    return render(request, "appmusic/index.html")


def artistas(request):
    return render(request, "appmusic/artistas.html")


def artistas_create(request):

    if request.method == "POST":

        formulario = ArtistasFormulario(request.POST)

        if formulario.is_valid():

            data = formulario.cleaned_data

            artista = Artistas(nombre = data["nombre"], genero = data["genero"])
            artista.save()

    formulario = ArtistasFormulario()

    context = {"formulario": formulario}

    return render(request, "appmusic/artistas_form.html", context)


def canciones(request):
    return render(request, "appmusic/canciones.html")


def canciones_create(request):

    if request.method == "POST":

        formulario = CancionesFormulario(request.POST)

        if formulario.is_valid():

            data = formulario.cleaned_data

            cancion = Canciones(nombre = data["nombre"], artista = data["artista"], genero = data["genero"])
            cancion.save()

    formulario = CancionesFormulario()

    context = {"formulario": formulario}

    return render(request, "appmusic/canciones_form.html", context)


def albums(request):
    return render(request, "appmusic/albums.html")


def albums_create(request):

    if request.method == "POST":

        formulario = AlbumsFormulario(request.POST)

        if formulario.is_valid():

            data = formulario.cleaned_data

            album = Albums(nombre = data["nombre"], artista = data["artista"] , genero = data["genero"], axo_publicacion = data["axo_publicacion"])
            album.save()

    formulario = AlbumsFormulario()

    context = {"formulario": formulario}
    return render(request, "appmusic/albums_form.html", context)


def search(request):
    return render(request, "appmusic/search.html")


def search_result(request):
    return render(request, "appmusic/search_result.html")


