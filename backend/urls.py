from django.urls import path
from .views import *


app_name = 'backend'

urlpatterns = [
    path('', AcaraAPIView.as_view(), name="create_acara"),
]