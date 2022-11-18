from django.urls import path
from appmusic.views import *

urlpatterns = [
    path("index/", index, name = 'music-index'),
    path("artistas/", artistas, name = 'music-artistas'),
    path("artistas/form/", artistas_create, name = 'music-artistas-form'),
    path("canciones/", canciones, name = 'music-canciones'),
    path("canciones/form/", canciones_create, name = 'music-canciones-form'),
    path("albums/", albums, name = 'music-albums'),
    path("albums/form/", albums_create, name = 'music-albums-form'),
    path("search/", search, name = 'music-search'),
    path("search/result/", search_result, name = 'music-search-result')
]
