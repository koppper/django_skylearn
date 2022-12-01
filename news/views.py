from django.shortcuts import render
from django.http import HttpResponse


def home(request, address=None, age=0):
    return HttpResponse(f"My home: {address}"
                        f" My age: {age}")


def sport_news(request, index, name):
    host = request.META["HTTP_HOST"]
    len = request.META["SERVER_PORT"]
    leng = request.scheme
    # end = request.endcoding

    return HttpResponse(f"<h2>Главные новости про Спорт</h2>"
                        f"<h3>{index}: {name}</h3>"
                        f"Последние новости спорта на сегодня:"
                        f" спортивная аналитика, видео, фото,эксклюзивные интервью, опросы."
                        f"<p>{host}</p>"
                        f"<p>{len}</p>"
                        f"<p>{leng}</p>"
                        f"<p></p>")
