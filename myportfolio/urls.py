from django.urls import re_path as url , include,path
from django.contrib import admin
from . import views

urlpatterns = [
    path('', views.index, name = 'index'),
    path('projects', views.projects, name= 'projects'),
    path('aboutme/', views.aboutme, name= 'aboutme'),
    path('contact/', views.contact, name= 'contact'),

]


