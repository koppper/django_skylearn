from django.urls import path
from .views import animals, home, index


urlpatterns = [
    path("animals/", home),
    path("index/", index)
]
