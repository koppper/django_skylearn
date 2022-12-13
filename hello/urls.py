from django.urls import path, re_path
from .views import index, base, product

urlpatterns = [
    path("index/", index),
    path("base/", base),
    path("product/", product)
]
