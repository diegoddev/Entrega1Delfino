from django.shortcuts import render
from appmusic.models import *
from appmusic.forms import *
# Create your views here.


def index(request):
    return render(request, "appmusic/index.html")


def artistas(request):

    artistas_buscar = Artistas.objects.all()
    return render(request, "appmusic/artistas/artistas.html", {"artistas_buscar": artistas_buscar})


def artistas_create(request):

    if request.method == "POST":

        formulario = ArtistasFormulario(request.POST)

        if formulario.is_valid():

            data = formulario.cleaned_data

            artista = Artistas(nombre = data["nombre"], genero = data["genero"])
            artista.save()

    formulario = ArtistasFormulario()

    context = {"formulario": formulario}

    return render(request, "appmusic/artistas/artistas_form.html", context)


def canciones(request):

    canciones_buscar = Canciones.objects.all()
    return render(request, "appmusic/canciones/canciones.html", {"canciones_buscar": canciones_buscar})


def canciones_create(request):

    if request.method == "POST":

        formulario = CancionesFormulario(request.POST)

        if formulario.is_valid():

            data = formulario.cleaned_data

            cancion = Canciones(nombre = data["nombre"], artista = data["artista"], genero = data["genero"])
            cancion.save()

    formulario = CancionesFormulario()

    context = {"formulario": formulario}

    return render(request, "appmusic/canciones/canciones_form.html", context)


def albums(request):

    albums_buscar = Albums.objects.all()
    return render(request, "appmusic/albums/albums.html", {"albums_buscar": albums_buscar})


def albums_create(request):

    if request.method == "POST":

        formulario = AlbumsFormulario(request.POST)

        if formulario.is_valid():

            data = formulario.cleaned_data

            album = Albums(nombre = data["nombre"], artista = data["artista"] , genero = data["genero"], axo_publicacion = data["axo_publicacion"])
            album.save()

    formulario = AlbumsFormulario()

    context = {"formulario": formulario}
    return render(request, "appmusic/albums/albums_form.html", context)


def search(request):
    return render(request, "appmusic/search/search.html")


def search_result(request):

    artista_canciones = request.GET["artista_canciones"]
    canciones = Canciones.objects.filter(artista__icontains = artista_canciones)

    return render(request, "appmusic/search/search_result.html", {"canciones": canciones})


