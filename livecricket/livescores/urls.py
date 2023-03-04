from operator import index
from django.shortcuts import render
from django.contrib import admin
from django.urls import path
# from numpy import place, r_
from django.conf.urls import include
from django.contrib.auth import views as auth_views
from livescores import views
app_name = 'livescores'

urlpatterns = [
    path('',views.home.as_view(),name='home'),
    path('trial/',views.trial,name='trial')
]
