from django.contrib import admin
from django.urls import include, path
from Banana import views


# Django admin header customization

admin.site.site_header = "Login to Developer Mike"
admin.site.site_title = "Welcome to the Dashboard!"
admin.site.index_title = "Welcome to this Portal!"
urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('projects/', views.projects, name='projects'),
    path('contact/', views.contact, name='contact'),
    path('leaguespy/', views.leaguespy, name='leagueSpy'),
    path('championlookup/', views.championlookup, name='championlookup'),
    path('W3/', views.W3, name='W3')
]
