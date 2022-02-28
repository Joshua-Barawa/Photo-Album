from django.shortcuts import render
from .models import *


def photos(request):
    images = Image.objects.all()
    locations = Location.objects.all()
    return render(request, "album/photos.html", {"images": images, "locations": locations})


def get_image_by_id(request, id):
    image = Image.objects.get(pk=id)
    return render(request, "album/photo.html", {"image": image})


def filter_by_location(request, id):
    images = Image.objects.filter(location=id)
    locations = Location.objects.all()
    return render(request, "album/photos.html", {"images": images, "locations": locations})


def search_image(request):
    if request.method == "POST":
        search = request.POST["search"]
        images = Image.objects.filter(category=search)
        locations = Location.objects.all()
        return render(request, "album/photos.html", {"search": search, "images": images, "locations": locations})
    return render(request, "album/image_form.html", {})


