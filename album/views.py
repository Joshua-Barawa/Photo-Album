from django.shortcuts import render
from .models import  *
from django.http import HttpResponse

# Create your views here.


def photos(request):
    images = Image.objects.all()
    return render(request, "album/photos.html", {"images":images})