from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
from django.template.response import TemplateResponse
from .forms import UserForm
from .forms import AnimalForm
from .models import UserModel


def animals(request):
    forms = AnimalForm()
    price = 1515151515
    render(request, 'animals.html', context={"forms": forms, "price": price})


def index(request):
    return render(request, "index.html")


def base(request):
    forms = UserForm()
    if request.method == "POST":  # проверка метода
        forms = UserForm(request.POST)  # сохраняем нашу заполненную форму
        if forms.is_valid():  # проверка
            first_name = forms.cleaned_data["first_name"]   # вызов полей
            return HttpResponse(f"Все в порядке {first_name}")  # # отправку в клиентскую часть
        else:
            return HttpResponseNotFound("ERROR 404")
    return render(request, "base.html", context={"forms": forms})


def re_base(request):
    first_name = request.POST.get("first_name", "НЕТ ИМЕНИ")
    second_name = request.POST.get("second_name", "НЕТ ИМЕНИ")
    number = request.POST.get("number", 0)
    email = request.POST.get("email", "НЕТУ ЭМЕЙЛА")
    return render(request, "send.html", context={"first_name": first_name, "email": email})


# is_valid()
def product(request):
    return render(request, "product.html")


def user(request):
    user = UserModel.objects.all()
    return render(request, 'user.html', context={"user": user})
