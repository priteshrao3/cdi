from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('contact', views.contact, name="contact"),
    path('skill', views.skill, name="skill"),
    path('edu', views.services, name="services"),
]
