from django.db import models

# Create your models here.

class Artistas(models.Model):

    nombre = models.CharField(max_length=50)
    genero = models.CharField(max_length=50)

class Canciones(models.Model):
    
    nombre = models.CharField(max_length=100)
    artista = models.CharField(max_length=50)
    genero = models.CharField(max_length=50)

class Albums(models.Model):
    
    nombre = models.CharField(max_length=100)
    artista = models.CharField(max_length=50)
    genero = models.CharField(max_length=50)
    axo_publicacion = models.IntegerField()
