from django.urls import path
from appmusic.views import *

urlpatterns = [
    path("index/", index, name = 'music-index')
]
