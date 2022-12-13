from django.shortcuts import render
from django.http import HttpResponse
from django.template.response import TemplateResponse


def index(request):
    return render(request, "index.html")


def base(request):
    hobbies = {"tom": "swim", "bob": "football", "martin": "None"}
    animals = ["Monkey", "elephant", "cat", "dog"]
    data = {"hobbies": hobbies, "animals": animals, "auto": "<h3> AUTOESCAPE </h3>", "sum": 100}

    return TemplateResponse(request, "base.html", context=data)


def product(request):
    return render(request, "product.html")
