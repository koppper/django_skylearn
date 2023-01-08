from django.urls import path

from crud.views import read, create

urlpatterns = [
    path('read/', read),
    path('create/', create),
    # path('edit/<int:id>/', edit),
    # path('delete/<int:id>', delete),
]
