from django.urls import path, re_path
from .views import index, hello, base

urlpatterns = [
    re_path(r'^index/$', index,  name="index"),
    path("hello/", hello, kwargs={"name": "Tom", "age": 15}, name="hello"),
    path("base/", base)
]
