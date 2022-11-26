from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse('<h1>Hello World!</h1>')


def hello(request, name, age):
    return HttpResponse(f"<h1>{name}, </h1> "
                        f"<h3>{age}</h3>")
