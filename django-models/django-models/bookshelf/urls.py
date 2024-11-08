from django.urls import path

from . import views

urlpatterns = [
    path("",views.lounge, name="lounge")
]