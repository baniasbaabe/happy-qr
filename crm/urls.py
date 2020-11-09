from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.dashboard, name='crm_dashboard'),

    # Kunden-URLs-------------------------------------------------------------
    path('kundenliste/', views.kundenliste, name='kundenliste'),
    path("kunde_anlegen/", views.KundeAnlegen, name='kunde_anlegen'),
    path("kunde_loeschen/<str:pk>/", views.KundeLoeschen, name='kunde_loeschen'),
    path("kunde_aktualisieren/<str:pk>/", views.KundeAktualisieren, name='kunde_aktualisieren'),
    # Mitarbeiter-URLs-------------------------------------------------------------
    path('mitarbeiterliste/', views.mitarbeiterliste, name='mitarbeiterliste'),
    path("mitarbeiter_anlegen/", views.mitarbeiterAnlegen, name='mitarbeiter_anlegen'),
    path("mitarbeiter_loeschen/<str:pk>/", views.mitarbeiterLoeschen, name='mitarbeiter_loeschen'),
    path("mitarbeiter_aktualisieren/<str:pk>/", views.mitarbeiterAktualisieren, name='mitarbeiter_aktualisieren'),
    # Auftrags-URLs-------------------------------------------------------------
    path("auftragsliste/", views.auftragsliste, name="auftragsliste"),
    path("auftrag_anlegen", views.auftragAnlegen, name="auftrag_anlegen"),
    path("auftrag_aktualisieren/<str:pk>/", views.auftragAktualisieren, name='auftrag_aktualisieren'),
    path("auftrag_loeschen/<str:pk>/", views.auftragLoeschen, name='auftrag_loeschen'),
]
