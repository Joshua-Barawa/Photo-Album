from django.shortcuts import render
from .models import *
from .forms import ImageForm
from django.http import HttpResponseRedirect, HttpResponse


# Create your views here.


def photos(request):
    images = Image.objects.all()
    return render(request, "album/photos.html", {"images": images})


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


def search_image(request, category):
    images = Image.objects.filter(category=category)
    return render(request, "album/image_form.html", {"images": images})


def filter_by_location(request, location):
    images = Image.objects.filter(location=location)
    return render(request, "album/photo_form.html", {"images" : images})