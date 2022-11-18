from django import forms

class ArtistasFormulacio(forms.Form):

    nombre = forms.CharField()
    genero = forms.CharField()

class CancionesFormulacio(forms.Form):

    nombre = forms.CharField()
    artista = forms.CharField()
    genero = forms.CharField()

class AlbumsFormulacio(forms.Form):

    nombre = forms.CharField()
    artista = forms.CharField()
    genero = forms.CharField()
    axo_publicacion = forms.CharField()



