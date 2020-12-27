from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.dashboard, name='menucard_dashboard'),

    path('profil/', views.profil_bearbeiten, name="profil"),

    # Vorspeisen URLs
    path('vorspeisen/', views.vorspeisen, name='vorspeisen'),
    path('vorspeisen-add/', views.vorspeisen_anlegen, name='vorspeisen_anlegen'),
    path('vorspeisen-bearbeiten/<str:pk>/', views.vorspeisen_bearbeiten, name='vorspeisen_bearbeiten'),
    path('vorspeisen-loeschen/<str:pk>/', views.vorspeisen_loeschen, name='vorspeisen_loeschen'),

    # Hauptspeisen URLs
    path('hauptspeisen/', views.hauptspeisen, name='hauptspeisen'),
    path('hauptspeisen-add/', views.hauptspeisen_anlegen, name='hauptspeisen_anlegen'),
    path('hauptspeisen-bearbeiten/<str:pk>/', views.hauptspeisen_bearbeiten, name='hauptspeisen_bearbeiten'),
    path('hauptspeisen-loeschen/<str:pk>/', views.hauptspeise_loeschen, name='hauptspeise_loeschen'),

    # Nachspeisen URLs
    path('nachspeisen/', views.nachspeisen, name='nachspeisen'),
    path('nachspeisen-add/', views.nachspeisen_anlegen, name='nachspeisen_anlegen'),
    path('nachspeisen-bearbeiten/<str:pk>/', views.nachspeisen_bearbeiten, name='nachspeisen_bearbeiten'),
    path('nachspeisen-loeschen/<str:pk>/', views.nachspeisen_loeschen, name='nachspeisen_loeschen'),

    # Alkoholhaltige Drinks URLs
    path('alkoholhaltigedrinks/', views.alkoholhaltigedrinks, name='alkoholhaltigedrinks'),
    path('alkoholhaltigedrinks-add/', views.alkoholhaltigedrinks_anlegen, name='alkoholhaltigedrinks_anlegen'),
    path('alkoholhaltigedrinks-bearbeiten/<str:pk>/', views.alkoholhaltigedrinks_bearbeiten,
         name='alkoholhaltigedrinks_bearbeiten'),
    path('alkoholhaltigedrinks-loeschen/<str:pk>/', views.alkoholhaltigedrinks_loeschen,
         name='alkoholhaltigedrinks_loeschen'),

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
    path(r'menucard_view/<str:username>', views.menucard, name='menucard'),
    path('logout/', views.logout_view, name='logout'),

    # covidform URLs
    path(r'menucard_view/covidform/', views.besucher_anlegen, name='covidform'),
    path('besucher_daten/', views.besucher_daten, name='besucherdaten'),
    path('besucher_loeschen/<str:pk>/', views.besucher_loeschen, name='besucher_loeschen'),
    # covidfomr export urls
    path('besucherliste_pdf_view/', views.ViewBesucherListePDF.as_view(), name="besucherliste_pdf_view"),
    path('besucherliste_pdf_download/', views.DownloadBesucherlistePDF.as_view(), name="besucherliste_pdf_download"),
    path('besucherliste_csv_download/', views.csv_download_besucherliste, name="besucherliste_csv_download"),

    #QR Code url
    path("qr/", views.test_qr, name="test_qr"),

    # Datenschutz
    path('datenschutzerklaerung/', views.datenschutz, name='datenschutz'),
]
