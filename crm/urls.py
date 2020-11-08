from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.dashboard, name='crm_dashboard'),
    path('kundenliste', views.kundenliste, name='kundenliste'),
    path("kunde_anlegen/", views.KundeAnlegen, name='kunde_anlegen'),
    path("kunde_loeschen/<str:pk>/", views.KundeLoeschen, name='kunde_loeschen'),
    path("kunde_aktualisieren/<str:pk>/", views.KundeAktualisieren, name='kunde_aktualisieren'),
]
