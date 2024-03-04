from django.urls import path
from .views import *


app_name = 'backend'

urlpatterns = [
    # URLs for AcaraAPIView
    path('acara/', AcaraAPIView.as_view()),
    path('acara/<int:pk>/', AcaraUpdateDeleteAPIView.as_view()),

    # URLs for Sponsor
    path('sponsor/<int:acara_id>/', SponsorCreateReadAPIView.as_view()),
    path('sponsor/<int:pk>/', SponsorUpdateDeleteAPIView.as_view()),

    # URLs for Pembicara
    path('pembicara/<int:acara_id>/', PembicaraCreateReadAPIView.as_view()),
    path('pembicara/<int:pk>/', PembicaraUpdateDeleteAPIView.as_view()),

    # URLs for PengurusInti
    path('pengurusinti/', PengurusIntiListCreateAPIView.as_view()),
    path('pengurusinti/<int:pk>/', PengurusIntiRetrieveUpdateDestroyAPIView.as_view()),

    # URLs for Divisi
    path('divisi/', DivisiListAPIView.as_view()),
    path('divisi/create/', DivisiCreateAPIView.as_view()),

    # URLs for Rapat
    path('rapat/<str:divisi_name>/', RapatListCreateAPIView.as_view()),
    path('rapat/<int:pk>/', RapatRetrieveUpdateDestroyAPIView.as_view()),

    # URLs for BPH
    path('bph/<str:divisi_name>/', BPHListCreateAPIView.as_view()),
    path('bph/<int:pk>/', BPHRetrieveUpdateDestroyAPIView.as_view()),

    # URLs for Kelompok
    path('kelompok/', KelompokListAPIView.as_view()),
    path('kelompok/create/', KelompokCreateAPIView.as_view()),
    path('kelompok/<int:pk>/delete/', KelompokDeleteAPIView.as_view()),

    # URLs for Mentor
    path('mentor/<int:no_kelompok>/', MentorListCreateAPIView.as_view()),
    path('mentor/<int:pk>/', MentorRetrieveUpdateDestroyAPIView.as_view()),

    # URLs for Mentee
    path('mentee/', MenteeListCreateAPIView.as_view()),
    path('mentee/<int:pk>/', MenteeRetrieveUpdateDestroyAPIView.as_view()),

    # URLs for Mentoring
    path('mentoring/', MentoringListCreateAPIView.as_view()),
    path('mentoring/<int:pk>/', MentoringRetrieveUpdateDestroyAPIView.as_view()),

]