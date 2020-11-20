from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.dashboard, name='menucard_dashboard'),

    # Vorspeisen URLs
    path('vorspeisen/', views.vorspeisen, name='vorspeisen'),
    path('vorspeisen-add/', views.vorspeisen_anlegen, name='vorspeisen_anlegen'),
    path('vorspeisen-bearbeiten/<str:pk>/', views.vorspeisen_bearbeiten, name='vorspeisen_bearbeiten'),
    path('vorspeisen-loeschen/<str:pk>/', views.vorspeisen_loeschen, name='vorspeisen_loeschen'),

    # Alkoholfreie Drinks URLs
    path('alkoholfreiedrinks/', views.alkfreiedrinks, name='alkfreiedrinks'),
    path('alkoholfreiedrinks-add/', views.alkfreiedrinks_anlegen, name='alkfreiedrinks_anlegen'),
    path('alkoholfreiedrinks-bearbeiten/<str:pk>/', views.alkfreiedrinks_bearbeiten, name='alkfreiedrinks_bearbeiten'),
    path('alkoholfreiedrinks-loeschen/<str:pk>/', views.alkfreiedrinks_loeschen, name='alkfreiedrinks_loeschen'),

    # Snacks URLs
    path('snacks/', views.snacks, name='snacks'),
    path('snacks-add/', views.snacks_anlegen, name='snacks_anlegen'),
    path('snacks-bearbeiten/<str:pk>/', views.snacks_bearbeiten, name='snacks_bearbeiten'),
    path('snacks-loeschen/<str:pk>/', views.snacks_loeschen, name='snacks_loeschen'),

    # Menucard URL
    path('menucard/', views.menucard, name='menucard')
]
