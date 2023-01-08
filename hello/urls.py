from django.urls import path, re_path
from .views import index, base, product, re_base, user

urlpatterns = [
    path("index/", index),
    path("base/", base, name="base"),
    path("submit/", re_base, name="submit"),
    path("product/", product),
    path("user/", user)
]
