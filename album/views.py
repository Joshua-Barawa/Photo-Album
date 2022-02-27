from django.shortcuts import render
from .models import *
from .forms import ImageForm
from django.http import HttpResponseRedirect, HttpResponse


# Create your views here.


def photos(request):
    images = Image.objects.all()
    locations = Location.objects.all()
    return render(request, "album/photos.html", {"images": images, "locations": locations})


def save_image(request):
    context ={}
    if request.method == "POST":
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            context['form'] = form
        return HttpResponseRedirect("/")
    else:
        form = ImageForm()
        context['form'] = form
        return render(request, "album/photo_form.html", context)
    return render(request, "album/photo_form.html",context)


def get_image_by_id(request, id):
    image = Image.objects.get(pk=id)
    return render(request, "album/photo.html", {"image": image})


def delete_image(request, id):
    Image.objects.filter(pk=id).delete()
    return HttpResponseRedirect("/")


def update_image(request, id):
    image = Image.objects.get(pk=id)
    form = ImageForm(request.POST or None, instance=image)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/")
    return render(request, "album/photo_update.html", {"image": image, "form": form})


def filter_by_location(request, id):
    images = Image.objects.filter(pk=id)
    locations = Location.objects.all()
    return render(request, "album/photos.html", {"images": images, "locations": locations})


def search_image(request):
    if request.method == "POST":
        search = request.POST["search"]
        images = Image.objects.filter(category=search)
        locations = Location.objects.all()
        return render(request, "album/photos.html", {"search": search, "images": images, "locations": locations})
    return render(request, "album/image_form.html", {})


