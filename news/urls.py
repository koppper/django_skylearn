from django.urls import path, re_path
from .views import home, sport_news

urlpatterns = [
    re_path(r"^home$", home, kwargs={"address": "Nazarbayeva 123"}),
    re_path(r"^home/\w+/home|index/", sport_news, kwargs={"index": 123, "name": "SPORT NEWS"})
]
