from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("textToJson",views.textToJson,name="textToJson")
]