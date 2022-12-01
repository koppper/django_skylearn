from django.urls import path
from .views import animals, home, index


urlpatterns = [
    path("home/", home),
    path("index/", index)
]
