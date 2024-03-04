from django.urls import path
from .views import *


app_name = 'backend'

urlpatterns = [
    path("", test),
    path("api-call/", api_call),
    path("api-list/", api_list)
]