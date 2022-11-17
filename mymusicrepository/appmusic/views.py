from django.shortcuts import render
from appmusic.models import *
from appmusic.forms import *
# Create your views here.


def index(request):
    return render(request, "appmusic/index.html")