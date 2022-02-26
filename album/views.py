from django.shortcuts import render
from .models import *
from .forms import ImageForm
from django.http import HttpResponseRedirect


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

    return render(request, "album/photo_form.html",context)
