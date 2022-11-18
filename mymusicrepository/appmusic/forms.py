from django import forms

class ArtistasFormulario(forms.Form):

    nombre = forms.CharField()
    genero = forms.CharField(label="Género")

class CancionesFormulario(forms.Form):

    nombre = forms.CharField()
    artista = forms.CharField()
    genero = forms.CharField(label="Género")

class AlbumsFormulario(forms.Form):

    nombre = forms.CharField()
    artista = forms.CharField()
    genero = forms.CharField(label="Género")
    axo_publicacion = forms.CharField(label="Año de Publicación")



