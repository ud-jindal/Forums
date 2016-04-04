from django.conf.urls import url, include
from django.contrib import admin

from . import views

app_name = 'Threads'
urlpatterns = [
	url(r'^$', views.Home, name='Home'),
	url(r'^(?P<id>[0-9])/', views.comment, name='Comment'),	
	url(r'^(?P<username>[a-zA-Z0-9]+)/create/', views.createThread, name='Create'),
    url(r'^(?P<username>[a-zA-Z0-9]+)/', views.Threads, name='Thread'),
]
