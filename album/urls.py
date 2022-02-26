
from django.urls import path
from .views import *


urlpatterns = [
  path('', photos, name="photos"),
  path('save-image/', save_image, name="save_image"),
  path('delete-image/<integer pk>/', delete_image, name="delete_image"),

]