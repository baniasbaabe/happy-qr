from django.shortcuts import render
from .models import *


# Funktion um dashboard.html anzuzeigen mit sämtlichen Mitarbeitern
def dashboard(request):
    # Objekt erstellen
    mitarbeiter = Mitarbeiter.objects.all()

    # Objekt in der HTML Datei zur Verfügung stellen
    context = {
        'mitarbeiter': mitarbeiter,
    }

    # Ausgabe der HTML Datei
    return render(request, 'crm/dashboard.html', context)


def kundenliste(request):
    context = {

    }
    return render(request, 'crm/kundenliste.html', context)
