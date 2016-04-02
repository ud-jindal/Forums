from django.conf.urls import url, include
from django.contrib import admin

from . import views

app_name = 'Login'
urlpatterns = [
    url(r'^$', views.Login, name='Login'),
 	url(r'^register/', views.Register, name='Register'),
 	url(r'^logout/', views.Logout, name='Logout'),
]
