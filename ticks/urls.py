# ticks/urls.py
from django.urls import path

from . import views

urlpatterns = [
    path('', views.choice_view, name='choice_form'),
    path('intro', views.introPage, name='intro'),
    path('about', views.aboutPage, name='about'),
    path('browser-check', views.browserCheck, name='browser-check'),
    path('r/<str:room_code>', views.learnerView, name='learner'),
]
