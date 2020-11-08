from django.shortcuts import render, redirect
from .models import *
from .forms import *


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

    kunden = Kunde.objects.all()

    context = {"kunden":kunden,

    }
    return render(request, 'crm/kundenliste.html', context)

def KundeAnlegen(request):

    form = KundeForm()
    if request.method == "POST":
        form = KundeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('kundenliste')
    context = {'form':form}


    return render(request, 'crm/kunde_form.html', context)

def KundeAktualisieren(request, pk):

    kunde = Kunde.objects.get(id=pk)
    form = KundeForm(instance=kunde)

    if request.method == "POST":
        form = KundeForm(request.POST, instance=kunde)
        if form.is_valid():
            form.save()
            return redirect('kundenliste')

    context = {'form': form}

    return render(request, "crm/kunde_form.html", context)

def KundeLoeschen(request, pk):

    kunde = Kunde.objects.get(id=pk)

    if request.method == "POST":
        kunde.delete()
        return redirect('kundenliste')

    context={"kunde":kunde}
    return render(request, 'crm/delete_kunde.html', context)