from django.urls import path
from .views import *


app_name = 'backend'

urlpatterns = [
    path("", test),
    path("acara/", acara)
]