
from django.forms import forms
from .models import Image


class ImageForm(forms.Form):
    class Meta:
        model = Image
        fields = '__all__'
