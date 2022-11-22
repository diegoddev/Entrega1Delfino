from django.db import models

# Create your models here.

class Artistas(models.Model):

    nombre = models.CharField(max_length=50)
    genero = models.CharField(max_length=50)

    def __str__(self):
        nom = self.nombre
        nom_list = nom.split()
        nom_yt = ""
        for i in nom_list:
              nom_yt =  nom_yt + i + "+"
        return nom_yt

class Canciones(models.Model):
    
    nombre = models.CharField(max_length=100)
    artista = models.CharField(max_length=50)
    genero = models.CharField(max_length=50)

    def __str__(self):
        nom = f"{self.artista} {self.nombre}"
        nom_list = nom.split()
        nom_yt = ""
        for i in nom_list:
            nom_yt = nom_yt + i + "+"
        return nom_yt


class Albums(models.Model):
    
    nombre = models.CharField(max_length=100)
    artista = models.CharField(max_length=50)
    genero = models.CharField(max_length=50)
    axo_publicacion = models.IntegerField()
