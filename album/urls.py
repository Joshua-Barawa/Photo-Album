
from django.urls import path
from .views import *


urlpatterns = [
  path('', photos, name="photos" )

]