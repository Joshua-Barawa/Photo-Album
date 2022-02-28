
from django.urls import path
from .views import *


urlpatterns = [
  path('', photos, name="photos"),
  path('get-image/<int:id>/', get_image_by_id, name="get_image"),
  path('location/<int:id>/', filter_by_location, name="filter_by_location"),
  path("category/", search_image, name="search_image")

]