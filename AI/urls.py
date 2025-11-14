from django.urls import path
from . import views

urlpatterns = [
    path("", views.index),
    path("offline-translate/", views.offline_translate),
    path("online-translate/", views.online_translate),
]
