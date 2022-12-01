from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseForbidden, HttpResponseGone


def animals(request):
    name = request.GET.get("name", "НИКАК")
    sound = request.GET.get("sound", "НИКАКОЙ")
    return HttpResponse(f"Мое животное: <h3>{name}</h3>, Оно говорит <h3>{sound}</h3>")


def home(request):
    return HttpResponseGone("410 ERROR")


def index(request):
    name = request.GET.get("name", "ПОЛЬЗОВАТЕЛЯ НЕТУ")
    # return HttpResponse(f"{name[0]}")
    if name[0].isupper() and 20 > len(name) > 3:
        return HttpResponseRedirect("/animals/home")
    elif name.isdigit():
        return HttpResponse(f"ЦИФРЫ {name}")
    else:
        return HttpResponse("что то не верно")

