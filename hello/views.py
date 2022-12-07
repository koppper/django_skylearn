from django.shortcuts import render
from django.http import HttpResponse
from django.template.response import TemplateResponse


def index(request):
    return HttpResponse('<h1>Hello World!</h1>')


def hello(request, name, age):
    return HttpResponse(f"<h1>{name}, </h1> "
                        f"<h3>{age}</h3>")


def base(request):
    hobbies = {"tom": "swim", "bob": "football", "martin": "None"}
    animals = ["Monkey", "elephant", "cat", "dog"]
    data = {"hobbies": hobbies, "animals": animals}
    return TemplateResponse(request, "index.html", context=data)
