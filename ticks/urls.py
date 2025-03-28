# ticks/urls.py
from django.urls import path

from . import views

urlpatterns = [
    path('', views.home_page, name='home'),
    path('about', views.about_page, name='about'),
    path('browser-check', views.browser_check, name='browser-check'),
    path('<str:room_code>', views.learner_view, name='learner'),
]
