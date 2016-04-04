from django.conf.urls import url, include
from django.contrib import admin

from . import views

app_name = 'Login'
urlpatterns = [
	url(r'^$', views.Home, name='Login'),
    url(r'^(?P<username>[a-zA-Z0-9]+)', views.Threads, name='Threads'),    
    url(r'^(?P<username>[a-zA-Z0-9]+)/create', views.createThread, name='create'),
]
