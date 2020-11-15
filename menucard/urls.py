from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.dashboard, name='menucard_dashboard'),

    # Vorspeisen URLs
    path('vorspeisen/', views.vorspeisen, name='vorspeisen'),
    path('vorspeisen-add/', views.vorspeisen_anlegen, name='vorspeisen_anlegen'),
    path('vorspeisen-bearbeiten/<str:pk>/', views.vorspeisen_bearbeiten, name='vorspeisen_bearbeiten'),
    path('vorspeisen-loeschen/<str:pk>/', views.vorspeisen_loeschen, name='vorspeisen_loeschen'),
]
