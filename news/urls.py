from django.urls import path, re_path, include
from .views import home, sport_news

urlpatterns = [
    path("home/", home),  # 1 берет по умолчанию
    path("home/<str:address>/", home),
    path("home/<str:address>/<int:age>/", home),  # 2 возвращает адрес
    path("sport/<str:index>/<name>/", sport_news),
]
