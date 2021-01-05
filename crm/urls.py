from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    # Startseite-URL-------------------------------------------------------------
    path('', views.dashboard, name='crm_dashboard'),
    # Kunden-URLs-------------------------------------------------------------
    path('kundenliste/', views.kundenliste, name='kundenliste'),
    path("kunde_anlegen/", views.KundeAnlegen, name='kunde_anlegen'),
    path("kunde_loeschen/<str:pk>/", views.KundeLoeschen, name='kunde_loeschen'),
    path('pdf_view_kundenliste/', views.ViewKundenListePDF.as_view(), name="pdf_view_kundenliste"),
    path('pdf_download_kundenliste/', views.DownloadKundenlistePDF.as_view(), name="pdf_download_kundenliste"),
    path("kunde_aktualisieren/<str:pk>/", views.KundeAktualisieren, name='kunde_aktualisieren'),
    path('csv_download_kundenliste/', views.csv_download_kundenliste, name="csv_download_kundenliste"),
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
    path('pdf_download/auftragsliste/', views.DownloadAuftragslistePDF.as_view(), name="auftragsliste_pdf_download"),
    path('csv_download/auftragsliste/', views.csv_download_auftragsliste, name="csv_auftragsliste_download"),
    # Rechnungs-URLs-------------------------------------------------------------
    path("rechnungsliste/", views.rechnungsliste, name="rechnungsliste"),
    path("rechnung_anlegen", views.rechnungAnlegen, name="rechnung_anlegen"),
    path("rechnung_aktualisieren/<str:pk>/", views.rechnungAktualisieren, name='rechnung_aktualisieren'),
    path("rechnung_loeschen/<str:pk>/", views.rechnungLoeschen, name='rechnung_loeschen'),
    path('pdf_view/<str:pk>', views.ViewPDF.as_view(), name="pdf_view"),
    path('pdf_download/<str:pk>', views.DownloadPDF.as_view(), name="pdf_download"),
    path('csv_download/<str:pk>', views.csv_download, name="csv_download"),
    # Login-URLs-------------------------------------------------------------
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.register_view, name='register'),
    # Passwort zurücksetzen URLs
    path('passwort_zuruecksetzen/', auth_views.PasswordResetView.as_view(template_name='crm/passwort_zuruecksetzen.html'), name='reset_password'),
    path('passwort_zuruecksetzen/email_gesendet/', auth_views.PasswordResetDoneView.as_view(template_name='crm/passwort_zuruecksetzen_email.html'), name='password_reset_done'),
    path('passwort_zuruecksetzen/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='crm/passwort_zuruecksetzen_formular.html'), name='password_reset_confirm'),
    path('passwort_erfolgreich_zuruecksetzen/', auth_views.PasswordResetCompleteView.as_view(template_name='crm/passwort_erfolgreich_zurueckgesetzt.html'), name='password_reset_complete'),
]
