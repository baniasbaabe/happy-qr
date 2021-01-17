from django.utils import timezone

from django.contrib import messages
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm

from crm.models import Auftrag, Rechnung
from menucard.forms import *
from menucard.models import Vorspeise, Hauptspeise, Nachspeise, Snacks, AlkoholfreieDrinks, AlkoholhaltigeDrinks

from crm.decoraters import *
from .filter import BesucherFilter
from .models import *
from .forms import *
from io import BytesIO
from django.template.loader import get_template
from django.views import View
from xhtml2pdf import pisa
import csv
from django.contrib import messages
from django.contrib.auth.models import Group, User

from reportlab.pdfgen import canvas
from django.http import HttpResponse
from reportlab.graphics.shapes import Drawing
from reportlab.graphics.barcode.qr import QrCodeWidget
from reportlab.graphics import renderPDF

# Create your views here.

def logout_view(request):
    '''
                Loggt den Kunden wieder aus und leitet ihn zur Login-Page weiter

                        Parameters:
                                request (HttpRequest): Ein Request-Objekt

                        Returns:
                                 redirect(): Methode, die ein HttpResponseRedirect
                                 Login-URL zurückgibt

    '''
    logout(request)
    messages.info(request, 'Sie haben sich erfolgreich ausgeloggt.')
    return redirect('login')


# DASHBOARD
@login_required(login_url='login')
@genehmigte_user(allowed_roles=['kunde'])
def dashboard(request):
    '''
             Gibt die Anzahl der Produkte in der jeweiligen Kategorie samt die Kategorie selber und die Option
             für den Template-Wechsel an das HTML-Template weiter

                    Parameters:
                            request (HttpRequest): Ein Request-Objekt

                    Returns:
                            render(): Methode, die das Dashboard-Template mit dem Context-Dict samt
                                        Kategorien + Anzahl der Produkte pro Kategorie und Template-Dropdownkombiniert
                                        und gibt ein HttpResponse zurück mit dem gerenderten Text
    '''
    kunde = Kunde.objects.get(email=request.user.email)
    auftrag = kunde.auftrag_set.first()

    # Template ändern
    form = TemplateForm(instance=kunde)
    if request.method == 'POST':
        form = TemplateForm(request.POST, instance=kunde)
        if form.is_valid():
            form.save()
            messages.success(request, 'Sie haben das Template erfolgreich geändert.')
        else:
            messages.info(request, 'Es ist ein Fehler aufgetreten. Versuchen Sie es nochmal.')

    count_vorspeisen = kunde.vorspeise_set.count()
    count_hauptspeisen = kunde.hauptspeise_set.count()
    count_nachspeisen = kunde.nachspeise_set.count()
    count_snacks = kunde.snacks_set.count()
    count_alkfreidrinks = kunde.alkoholfreiedrinks_set.count()
    count_alkdrinks = kunde.alkoholhaltigedrinks_set.count()
    template = kunde.template

    context = {
        'kunde': kunde,
        'form': form,
        'count_vorspeisen': count_vorspeisen,
        'count_hauptspeisen': count_hauptspeisen,
        'count_nachspeisen': count_nachspeisen,
        'count_snacks': count_snacks,
        'count_alkfreidrinks': count_alkfreidrinks,
        'count_alkdrinks': count_alkdrinks,
        'template': template,
        'auftrag': auftrag
    }
    return render(request, 'menucard/dashboard.html', context)


# VORSPEISEN CRUD
@login_required(login_url='login')
@genehmigte_user(allowed_roles=['kunde'])
def vorspeisen(request):
    '''
                 Gibt die Vorspeisedaten an das Template weiter zum Anzeigen der Vorspeisen

                        Parameters:
                                request (HttpRequest): Ein Request-Objekt

                        Returns:
                                render(): Methode, die das Vorspeisen-Template mit dem Context-Dict samt
                                            Vorspeisedaten kombiniert und gibt ein HttpResponse zurück mit dem
                                            gerenderten Text
    '''
    kunde = Kunde.objects.get(email=request.user.email)  # Vorspeise dem Kunden zuweisen
    vorspeise = kunde.vorspeise_set.all()  # QuerySet zur Ausgabe aller Vorspeisen
    context = {'vorspeise': vorspeise}  # Dictionary, die in der vorspeisen.html interiert werden soll
    return render(request, 'menucard/vorspeisen.html', context)  # Verknüpfung der Funktion mit der vorspeisen.html


@login_required(login_url='login')
@genehmigte_user(allowed_roles=['kunde'])
def vorspeisen_anlegen(request):
    '''
                 Gibt die Form zum Anlegen der Vorspeise an das Vorspeiseform-Template weiter

                        Parameters:
                                request (HttpRequest): Ein Request-Objekt

                        Returns:
                                render(): Methode, die das Vorspeiseform-Template mit der Form zum Anlegen
                                kombiniert und gibt ein HttpResponse zurück mit dem gerenderten Text
    '''
    kunde = Kunde.objects.get(email=request.user.email)
    form = VorspeiseForm(initial={'kundeId': kunde})

    if request.method == "POST":
        form = VorspeiseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('vorspeisen')
        # messages.success(request, 'Vorspeise erfolgreich hinzugefügt.')
        else:
            messages.info(request, 'Bitte überprüfen Sie Ihre Eingabe.')

    context = {'form': form}
    return render(request, "menucard/vorspeisen_anlegen.html", context)


@login_required(login_url='login')
@genehmigte_user(allowed_roles=['kunde'])
def vorspeisen_bearbeiten(request, pk):
    '''
                 Gibt die Vorspeisebearbeiten-Form an das Vorspeiseform-Template weiter

                        Parameters:
                                request (HttpRequest): Ein Request-Objekt
                                pk (int): Primärschlussel der Vorspeise

                        Returns:
                                render(): Methode, die das Vorspeiseform-Template mit der Form zum Aktualisieren
                                kombiniert und gibt ein HttpResponse zurück mit dem gerenderten Text
    '''
    vorspeise = Vorspeise.objects.get(id=pk)
    form = VorspeiseForm(instance=vorspeise)

    if request.method == 'POST':
        form = VorspeiseForm(request.POST, instance=vorspeise)
        if form.is_valid():
            form.save()
            return redirect('vorspeisen')
        else:
            messages.info(request, 'Überprüfen Sie Ihre Eingabe.')

    context = {
        'vorspeise': vorspeise,
        'form': form
    }
    return render(request, 'menucard/vorspeisen_bearbeiten.html', context)


@login_required(login_url='login')
@genehmigte_user(allowed_roles=['kunde'])
def vorspeisen_loeschen(request, pk):
    '''
                Gibt die Vorspeiselöschen-Form an das Vorspeiselöschen-Template weiter

                        Parameters:
                                request (HttpRequest): Ein Request-Objekt
                                pk (int): Primärschlussel der Vorspeise

                        Returns:
                                render(): Methode, die das Vorspeiselöschen-Template mit der Form zum Löschen
                                kombiniert und gibt ein HttpResponse zurück mit dem gerenderten Text
    '''
    vorspeise = Vorspeise.objects.get(id=pk)

    if request.method == "POST":
        vorspeise.delete()
        return redirect('vorspeisen')

    context = {"vorspeise": vorspeise}
    return render(request, 'menucard/vorspeise_loeschen.html', context)


# HAUPTSPEISEN CRUD
@login_required(login_url='login')
@genehmigte_user(allowed_roles=['kunde'])
def hauptspeisen(request):
    '''
                 Gibt die Hauptspeisedaten an das Template weiter zum Anzeigen der Hauptspeisen

                        Parameters:
                                request (HttpRequest): Ein Request-Objekt

                        Returns:
                                render(): Methode, die das Hauptspeisen-Template mit dem Context-Dict samt
                                            Hauptspeisen kombiniert und gibt ein HttpResponse zurück mit dem
                                            gerenderten Text
    '''
    kunde = Kunde.objects.get(email=request.user.email)
    hauptspeise = kunde.hauptspeise_set.all()

    context = {'hauptspeisen': hauptspeise}
    return render(request, 'menucard/hauptspeisen.html', context)


@login_required(login_url='login')
@genehmigte_user(allowed_roles=['kunde'])
def hauptspeisen_anlegen(request):
    '''
                 Gibt die Form zum Anlegen der Hauptspeise an das Hauptspeiseform-Template weiter

                        Parameters:
                                request (HttpRequest): Ein Request-Objekt

                        Returns:
                                render(): Methode, die das Hauptspeiseform-Template mit der Form zum Anlegen
                                kombiniert und gibt ein HttpResponse zurück mit dem gerenderten Text
    '''
    kunde = Kunde.objects.get(email=request.user.email)

    hauptspeise = Hauptspeise()
    form = HauptspeiseForm(initial={'kundeId': kunde})

    if request.method == "POST":
        form = HauptspeiseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('hauptspeisen')
        # messages.success(request, 'Hauptspeise erfolgreich hinzugefügt.')
        else:
            messages.info(request, 'Bitte überprüfen Sie Ihre Eingabe.')

    context = {'form': form}
    return render(request, "menucard/hauptspeisen_anlegen.html", context)


@login_required(login_url='login')
@genehmigte_user(allowed_roles=['kunde'])
def hauptspeisen_bearbeiten(request, pk):
    '''
                 Gibt die Hauptspeisebearbeiten-Form an das Hauptspeiseform-Template weiter

                        Parameters:
                                request (HttpRequest): Ein Request-Objekt
                                pk (int): Primärschlussel der Hauptspeise

                        Returns:
                                render(): Methode, die das Hauptspeiseform-Template mit der Form zum Aktualisieren
                                kombiniert und gibt ein HttpResponse zurück mit dem gerenderten Text
    '''
    hauptspeise = Hauptspeise.objects.get(id=pk)
    form = HauptspeiseForm(instance=hauptspeise)

    if request.method == 'POST':
        form = HauptspeiseForm(request.POST, instance=hauptspeise)
        if form.is_valid():
            form.save()
            return redirect('hauptspeisen')
        else:
            messages.info(request, 'Überprüfen Sie Ihre Eingabe.')

    context = {
        'hauptspeise': hauptspeise,
        'form': form
    }
    return render(request, 'menucard/hauptspeisen_bearbeiten.html', context)


@login_required(login_url='login')
@genehmigte_user(allowed_roles=['kunde'])
def hauptspeise_loeschen(request, pk):
    '''
                Gibt die Hauptspeiselöschen-Form an das Hauptspeiselöschen-Template weiter

                        Parameters:
                                request (HttpRequest): Ein Request-Objekt
                                pk (int): Primärschlussel der Hauptspeise

                        Returns:
                                render(): Methode, die das Hauptspeiselöschen-Template mit der Form zum Löschen
                                kombiniert und gibt ein HttpResponse zurück mit dem gerenderten Text
    '''
    hauptspeise = Hauptspeise.objects.get(id=pk)

    if request.method == "POST":
        hauptspeise.delete()
        return redirect('hauptspeisen')

    context = {"hauptspeise": hauptspeise}
    return render(request, 'menucard/hauptspeise_loeschen.html', context)


# NACHSPEISEN CRUD
@login_required(login_url='login')
@genehmigte_user(allowed_roles=['kunde'])
def nachspeisen(request):
    '''
                 Gibt die Nachspeisedaten an das Template weiter zum Anzeigen der Nachspeisen

                        Parameters:
                                request (HttpRequest): Ein Request-Objekt

                        Returns:
                                render(): Methode, die das Nachspeisen-Template mit dem Context-Dict samt
                                            Nachspeisen kombiniert und gibt ein HttpResponse zurück mit dem
                                            gerenderten Text
    '''
    kunde = Kunde.objects.get(email=request.user.email)
    nachspeise = kunde.nachspeise_set.all()

    context = {'nachspeisen': nachspeise}
    return render(request, 'menucard/nachspeisen.html', context)


@login_required(login_url='login')
@genehmigte_user(allowed_roles=['kunde'])
def nachspeisen_anlegen(request):
    '''
                 Gibt die Form zum Anlegen der Nachspeise an das Nachspeiseform-Template weiter

                        Parameters:
                                request (HttpRequest): Ein Request-Objekt

                        Returns:
                                render(): Methode, die das Nachspeiseform-Template mit der Form zum Anlegen
                                kombiniert und gibt ein HttpResponse zurück mit dem gerenderten Text
    '''
    kunde = Kunde.objects.get(email=request.user.email)

    form = NachspeiseForm(initial={'kundeId': kunde})

    nachspeise = Nachspeise()

    if request.method == "POST":
        form = NachspeiseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('nachspeisen')
        # messages.success(request, 'Nachspeise erfolgreich hinzugefügt.')
        else:
            messages.info(request, 'Bitte überprüfen Sie Ihre Eingabe.')

    context = {'form': form}
    return render(request, "menucard/nachspeisen_anlegen.html", context)


@login_required(login_url='login')
@genehmigte_user(allowed_roles=['kunde'])
def nachspeisen_bearbeiten(request, pk):
    '''
                 Gibt die Nachspeisebearbeiten-Form an das Nachspeiseform-Template weiter

                        Parameters:
                                request (HttpRequest): Ein Request-Objekt
                                pk (int): Primärschlussel der Nachspeise

                        Returns:
                                render(): Methode, die das Nachspeiseform-Template mit der Form zum Aktualisieren
                                kombiniert und gibt ein HttpResponse zurück mit dem gerenderten Text
    '''
    nachspeise = Nachspeise.objects.get(id=pk)
    form = NachspeiseForm(instance=nachspeise)

    if request.method == 'POST':
        form = NachspeiseForm(request.POST, instance=nachspeise)
        if form.is_valid():
            form.save()
            return redirect('nachspeisen')
        else:
            messages.info(request, 'Überprüfen Sie Ihre Eingabe.')

    context = {
        'nachspeise': nachspeise,
        'form': form
    }
    return render(request, 'menucard/nachspeisen_bearbeiten.html', context)


@login_required(login_url='login')
@genehmigte_user(allowed_roles=['kunde'])
def nachspeisen_loeschen(request, pk):
    '''
                Gibt die Nachspeiselöschen-Form an das Nachspeiselöschen-Template weiter

                        Parameters:
                                request (HttpRequest): Ein Request-Objekt
                                pk (int): Primärschlussel der Nachspeise

                        Returns:
                                render(): Methode, die das Nachspeiselöschen-Template mit der Form zum Löschen
                                kombiniert und gibt ein HttpResponse zurück mit dem gerenderten Text
    '''
    nachspeise = Nachspeise.objects.get(id=pk)

    if request.method == "POST":
        nachspeise.delete()
        return redirect('nachspeisen')

    context = {"nachspeise": nachspeise}
    return render(request, 'menucard/nachspeise_loeschen.html', context)


# SNACKS CRUD
@login_required(login_url='login')
@genehmigte_user(allowed_roles=['kunde'])
def snacks(request):
    '''
                 Gibt die Snacksdaten an das Template weiter zum Anzeigen der Snacks

                        Parameters:
                                request (HttpRequest): Ein Request-Objekt

                        Returns:
                                render(): Methode, die das Snacks-Template mit dem Context-Dict samt
                                            Snacksdaten kombiniert und gibt ein HttpResponse zurück mit dem
                                            gerenderten Text
    '''
    kunde = Kunde.objects.get(email=request.user.email)
    snacks = kunde.snacks_set.all()

    context = {'snack': snacks}
    return render(request, 'menucard/snacks.html', context)


@login_required(login_url='login')
@genehmigte_user(allowed_roles=['kunde'])
def snacks_anlegen(request):
    '''
                 Gibt die Form zum Anlegen der Snacks an das Snacksform-Template weiter

                        Parameters:
                                request (HttpRequest): Ein Request-Objekt

                        Returns:
                                render(): Methode, die das Snacksform-Template mit der Form zum Anlegen
                                kombiniert und gibt ein HttpResponse zurück mit dem gerenderten Text
    '''
    kunde = Kunde.objects.get(email=request.user.email)

    form = SnacksForm(initial={'kundeId': kunde})

    snack = Snacks()

    if request.method == "POST":
        form = SnacksForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('snacks')
        else:
            messages.info(request, 'Bitte überprüfen Sie Ihre Eingabe.')

    context = {'form': form}
    return render(request, "menucard/snacks_anlegen.html", context)


@login_required(login_url='login')
@genehmigte_user(allowed_roles=['kunde'])
def snacks_bearbeiten(request, pk):
    '''
                 Gibt die Snacksbearbeiten-Form an das Snacksform-Template weiter

                        Parameters:
                                request (HttpRequest): Ein Request-Objekt
                                pk (int): Primärschlussel des Snacks

                        Returns:
                                render(): Methode, die das Snacksform-Template mit der Form zum Aktualisieren
                                kombiniert und gibt ein HttpResponse zurück mit dem gerenderten Text
    '''
    snack = Snacks.objects.get(id=pk)
    form = SnacksForm(instance=snack)

    if request.method == 'POST':
        form = SnacksForm(request.POST, instance=snack)
        if form.is_valid():
            form.save()
            return redirect('snacks')
        else:
            messages.info(request, 'Überprüfen Sie Ihre Eingabe.')

    context = {
        'snack': snack,
        'form': form
    }
    return render(request, 'menucard/snacks_bearbeiten.html', context)


@login_required(login_url='login')
@genehmigte_user(allowed_roles=['kunde'])
def snacks_loeschen(request, pk):
    '''
                Gibt die Snackslöschen-Form an das Snackslöschen-Template weiter

                        Parameters:
                                request (HttpRequest): Ein Request-Objekt
                                pk (int): Primärschlussel des Snacks

                        Returns:
                                render(): Methode, die das Snackslöschen-Template mit der Form zum Löschen
                                kombiniert und gibt ein HttpResponse zurück mit dem gerenderten Text
    '''
    snack = Snacks.objects.get(id=pk)

    if request.method == "POST":
        snack.delete()
        return redirect('snacks')

    context = {"snack": snack}
    return render(request, 'menucard/snacks_loeschen.html', context)


# ALKOHOLHALTIGE GETRÄNKE CRUD
@login_required(login_url='login')
@genehmigte_user(allowed_roles=['kunde'])
def alkoholhaltigedrinks(request):
    '''
                 Gibt die Alkhaltigendrinksedaten an das Template weiter zum Anzeigen der Alkhaltigendrinks

                        Parameters:
                                request (HttpRequest): Ein Request-Objekt

                        Returns:
                                render(): Methode, die das Alkhaltigendrinks-Template mit dem Context-Dict samt
                                            Alkhaltigendrinksdaten kombiniert und gibt ein HttpResponse zurück mit dem
                                            gerenderten Text
    '''
    kunde = Kunde.objects.get(email=request.user.email)
    alkdrink = kunde.alkoholhaltigedrinks_set.all()

    context = {'alkdrink': alkdrink}
    return render(request, 'menucard/alkoholhaltigedrinks.html', context)


@login_required(login_url='login')
@genehmigte_user(allowed_roles=['kunde'])
def alkoholhaltigedrinks_anlegen(request):
    '''
                 Gibt die Form zum Anlegen der Alkhaltigendrinks an das Alkhaltigendrinksform-Template weiter

                        Parameters:
                                request (HttpRequest): Ein Request-Objekt

                        Returns:
                                render(): Methode, die das Alkhaltigendrinksform-Template mit der Form zum Anlegen
                                kombiniert und gibt ein HttpResponse zurück mit dem gerenderten Text
    '''
    kunde = Kunde.objects.get(email=request.user.email)
    form = AlkhaltigeDrinksForm(initial={'kundeId': kunde})

    alkdrink = AlkoholhaltigeDrinks()

    if request.method == "POST":
        form = AlkhaltigeDrinksForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('alkoholhaltigedrinks')
        # messages.success(request, 'Alkoholhaltige Drinks erfolgreich hinzugefügt.')
        else:
            messages.info(request, 'Bitte überprüfen Sie Ihre Eingabe.')

    context = {'form': form}
    return render(request, "menucard/alkoholhaltigedrinks_anlegen.html", context)


@login_required(login_url='login')
@genehmigte_user(allowed_roles=['kunde'])
def alkoholhaltigedrinks_bearbeiten(request, pk):
    '''
                 Gibt die Alkhaltigedrinksbearbeiten-Form an das ALkhaltigedrinksform-Template weiter

                        Parameters:
                                request (HttpRequest): Ein Request-Objekt
                                pk (int): Primärschlussel des Alkhaltigendrinks

                        Returns:
                                render(): Methode, die das Alkhaltigedrinksform-Template mit der Form zum
                                Aktualisieren kombiniert und gibt ein HttpResponse zurück mit dem gerenderten Text
    '''
    alkdrink = AlkoholhaltigeDrinks.objects.get(id=pk)
    form = AlkhaltigeDrinksForm(instance=alkdrink)

    if request.method == 'POST':
        form = AlkhaltigeDrinksForm(request.POST, instance=alkdrink)
        if form.is_valid():
            form.save()
            return redirect('alkoholhaltigedrinks')
        else:
            messages.info(request, 'Überprüfen Sie Ihre Eingabe.')

    context = {
        'alkdrink': alkdrink,
        'form': form
    }
    return render(request, 'menucard/alkoholhaltigedrinks_bearbeiten.html', context)


@login_required(login_url='login')
@genehmigte_user(allowed_roles=['kunde'])
def alkoholhaltigedrinks_loeschen(request, pk):
    '''
                Gibt die Alkhaltigedrinkslöschen-Form an das Alkhaltigedrinkslöschen-Template weiter

                        Parameters:
                                request (HttpRequest): Ein Request-Objekt
                                pk (int): Primärschlussel des Alkhaltigendrinks

                        Returns:
                                render(): Methode, die das ALkhaltigedrinkslöschen-Template mit der Form zum Löschen
                                kombiniert und gibt ein HttpResponse zurück mit dem gerenderten Text
    '''
    alkdrink = AlkoholhaltigeDrinks.objects.get(id=pk)

    if request.method == "POST":
        alkdrink.delete()
        return redirect('alkoholhaltigedrinks')

    context = {"alkdrink": alkdrink}
    return render(request, 'menucard/alkoholhaltigedrinks_loeschen.html', context)


# ALKOHOLFREIE GETRÄNKE CRUD
@login_required(login_url='login')
@genehmigte_user(allowed_roles=['kunde'])
def alkfreiedrinks(request):
    '''
                 Gibt die Alkfreiendrinksedaten an das Template weiter zum Anzeigen der Alkfreiendrinks

                        Parameters:
                                request (HttpRequest): Ein Request-Objekt

                        Returns:
                                render(): Methode, die das Alkfreiendrinks-Template mit dem Context-Dict samt
                                            Alkfreiendrinksdaten kombiniert und gibt ein HttpResponse zurück mit dem
                                            gerenderten Text
    '''
    kunde = Kunde.objects.get(email=request.user.email)
    softdrink = kunde.alkoholfreiedrinks_set.all()

    context = {'softdrink': softdrink}
    return render(request, 'menucard/alkfreiedrinks.html', context)


@login_required(login_url='login')
@genehmigte_user(allowed_roles=['kunde'])
def alkfreiedrinks_anlegen(request):
    '''
                 Gibt die Form zum Anlegen der Alkfreiendrinks an das Alkfreiendrinksform-Template weiter

                        Parameters:
                                request (HttpRequest): Ein Request-Objekt

                        Returns:
                                render(): Methode, die das Alkfreiendrinksform-Template mit der Form zum Anlegen
                                kombiniert und gibt ein HttpResponse zurück mit dem gerenderten Text
    '''
    kunde = Kunde.objects.get(email=request.user.email)

    form = AlkfreieDrinksForm(initial={'kundeId': kunde})

    softdrink = AlkoholfreieDrinks()

    if request.method == "POST":
        form = AlkfreieDrinksForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('alkfreiedrinks')
        # messages.success(request, 'Vorspeise erfolgreich hinzugefügt.')
        else:
            messages.info(request, 'Bitte überprüfen Sie Ihre Eingabe.')

    context = {'form': form}
    return render(request, "menucard/alkfreiedrinks_anlegen.html", context)


@login_required(login_url='login')
@genehmigte_user(allowed_roles=['kunde'])
def alkfreiedrinks_bearbeiten(request, pk):
    '''
                 Gibt die Alkfreiedrinksbearbeiten-Form an das Alkfreiedrinksform-Template weiter

                        Parameters:
                                request (HttpRequest): Ein Request-Objekt
                                pk (int): Primärschlussel des Alkfreiendrinks

                        Returns:
                                render(): Methode, die das Akfreiedrinksform-Template mit der Form zum Aktualisieren
                                kombiniert und gibt ein HttpResponse zurück mit dem gerenderten Text
    '''
    softdrink = AlkoholfreieDrinks.objects.get(id=pk)
    form = AlkfreieDrinksForm(instance=softdrink)

    if request.method == 'POST':
        form = AlkfreieDrinksForm(request.POST, instance=softdrink)
        if form.is_valid():
            form.save()
            return redirect('alkfreiedrinks')
        else:
            messages.info(request, 'Überprüfen Sie Ihre Eingabe.')

    context = {
        'softdrink': softdrink,
        'form': form
    }
    return render(request, 'menucard/alkfreiedrinks_bearbeiten.html', context)


@login_required(login_url='login')
@genehmigte_user(allowed_roles=['kunde'])
def alkfreiedrinks_loeschen(request, pk):
    '''
                Gibt die Alkfreiedrinkslöschen-Form an das Alkfreiedrinkslöschen-Template weiter

                        Parameters:
                                request (HttpRequest): Ein Request-Objekt
                                pk (int): Primärschlussel des Alkfreiendrinks

                        Returns:
                                render(): Methode, die das ALkfreiedrinkslöschen-Template mit der Form zum Löschen
                                kombiniert und gibt ein HttpResponse zurück mit dem gerenderten Text
    '''
    softdrink = AlkoholfreieDrinks.objects.get(id=pk)

    if request.method == "POST":
        softdrink.delete()
        return redirect('alkfreiedrinks')

    context = {"softdrink": softdrink}
    return render(request, 'menucard/alkfreiedrinks_loeschen.html', context)


def menucard(request, username):
    '''
                 Gibt die gescannte Menükarte aus, basierend auf den Username von dem man es gescannt hat

                        Parameters:
                                request (HttpRequest): Ein Request-Objekt
                                username (String): Name des Users

                        Returns:
                                render(): Methode, die das Menükarten-Template mit dem Context-Dict samt
                                            Produkten aller Kategorien und dem ausgewählten Template kombiniert und
                                            gibt ein HttpResponse zurück mit dem gerenderten Text
    '''
    # Änderung mit url
    print(request.get_full_path())
    url = request.get_full_path().split('/')
    aktueller_user = User.objects.get(username=url[-1])
    kunde = Kunde.objects.get(email=aktueller_user.email)
    vorspeisen = kunde.vorspeise_set.all()
    hauptspeise = kunde.hauptspeise_set.all()
    nachspeise = kunde.nachspeise_set.all()
    snacks = kunde.snacks_set.all()
    softdrink = kunde.alkoholfreiedrinks_set.all()
    alkdrinks = kunde.alkoholhaltigedrinks_set.all()
    template = kunde.template

    context = {
        'vorspeisen': vorspeisen,
        'hauptspeise': hauptspeise,
        'nachspeise': nachspeise,
        'snacks': snacks,
        'softdrink': softdrink,
        'alkdrinks': alkdrinks,
        'template': template,
        'kunde': kunde.user.username
    }
    return render(request, 'menucard/menucard.html', context)


@login_required(login_url='login')
@genehmigte_user(allowed_roles=['kunde'])
def profil_bearbeiten(request):
    '''
                 Gibt die Profil-Form und die Passwortvergessenform an das Profil-Template weiter

                        Parameters:
                                request (HttpRequest): Ein Request-Objekt

                        Returns:
                                render(): Methode, die das Profil-Template mit der Form zum Aktualisieren des Profils
                                und des PW-Vergessen kombiniert und gibt ein HttpResponse zurück mit dem gerenderten
                                Text
    '''
    # PROFIL BEARBEITEN
    kunde = Kunde.objects.get(email=request.user.email)
    form = ProfilForm(instance=kunde)
    if request.method == 'POST':
        form = ProfilForm(request.POST, instance=kunde)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profil aktualisiert')

    # PASSWORT ÄNDERN
    pwform = PasswordChangeForm(request.user)
    if request.method == 'POST':
        pwform = PasswordChangeForm(request.user, request.POST)
        if pwform.is_valid():
            user = pwform.save()
            update_session_auth_hash(request, user)
            messages.success(request, 'Passwort erfolgreich geändert.')
        else:
            pwform = PasswordChangeForm(request.user)

    context = {
        'form': form,
        'pwform': pwform
    }

    return render(request, 'menucard/profil.html', context)


# Covid Datenerfassung
def besucher_anlegen(request, username):
    '''
                 Gibt die Form zum Anlegen des Besuchers an das Alkfreiendrinksform-Template weiter

                        Parameters:
                                request (HttpRequest): Ein Request-Objekt
                                username (str): Name des Users (des jeweiligen Lokalbesitzers)

                        Returns:
                                render(): Methode, die das Covidform-Template mit der Form zum Anlegen des Besuchers
                                kombiniert und gibt ein HttpResponse zurück mit dem gerenderten Text
    '''
    print(request.get_full_path())
    url = request.get_full_path().split('/')
    aktueller_user = User.objects.get(username=url[-1])
    kunde = Kunde.objects.get(email=aktueller_user.email)

    form = CovidForm(initial={'kundeId': kunde})
    if request.method == "POST":
        form = CovidForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('menucard', kunde.user.username)

    context = {
        'kunde': kunde,
        'form': form,
    }
    return render(request, "menucard/covidform.html", context)


@login_required(login_url='login')
@genehmigte_user(allowed_roles=['kunde'])
def besucher_daten(request):  # hole alle besucher aus DB
    '''
                 Gibt die Besucherdaten und die Besucher-Filterform an das Template weiter zum Anzeigen der
                 Besucherliste des Lokalbesitzers

                        Parameters:
                                request (HttpRequest): Ein Request-Objekt

                        Returns:
                                render(): Methode, die das Besucherdaten-Template mit dem Context-Dict samt
                                            Besucherliste und Besucher-Filterform kombiniert und gibt ein
                                            HttpResponse zurück mit dem gerenderten Text
    '''
    kunde = Kunde.objects.get(email=request.user.email)
    besucher = kunde.besucher_set.all()
    besucher_filter = BesucherFilter(request.GET, queryset=besucher)
    besucher_singular = besucher_filter.qs

    context = {"besucher": besucher_singular, 'besucher_filter': besucher_filter}
    return render(request, 'menucard/besucher_daten.html', context)


@login_required(login_url='login')
@genehmigte_user(allowed_roles=['kunde'])
def besucher_loeschen(request, pk):
    '''
                Gibt die Besucherlöschen-Form an das Besucherlöschen-Template weiter

                        Parameters:
                                request (HttpRequest): Ein Request-Objekt
                                pk (int): Primärschlussel des Besuchers

                        Returns:
                                render(): Methode, die das Besucherlöschen-Template mit der Form zum Löschen
                                kombiniert und gibt ein HttpResponse zurück mit dem gerenderten Text
    '''
    besucher = Besucher.objects.get(id=pk)

    if request.method == "POST":
        besucher.delete()
        return redirect('besucherdaten')

    context = {"besucher": besucher}
    return render(request, 'menucard/besucher_loeschen.html', context)


def render_to_pdf(template_src, context_dict):
    '''
                Rendert den Inhalt in ein PDF
                        Parameters:
                                template_src (str): Pfad zur HTML-Datei
                                context_dict (dict): Dictionary mit dem Inhalt für HTML-Datei

                        Returns:
                                HttpResponse(): Methode, um eine HTTP-Response zu erstellen mit der PDF
    '''
    template = get_template(template_src)
    html = template.render(context_dict)
    result = BytesIO()
    pdf = pisa.pisaDocument(BytesIO(html.encode("UTF-8")), result)
    if not pdf.err:
        return HttpResponse(result.getvalue(), content_type='application/pdf')
    return None


def csv_download_besucherliste(request):
    '''
                Schreibt den Inhalt der Besucherliste in eine CSV-Datei und lädt sie runter
                        Parameters:
                                request (HttpRequest): Ein Request-Objekt

                        Returns:
                                response: CSV-Datei mit Inhalt der Besucherliste als Download
    '''
    kunde = Kunde.objects.get(email=request.user.email)
    besucher_liste = kunde.besucher_set.all()

    response = HttpResponse(content_type='text/csv')
    filename = "Besucherliste.csv"
    content = "attachment; filename='%s'" % (filename)
    response['Content-Disposition'] = content

    writer = csv.writer(response, delimiter="\t")
    writer.writerow(["Vorname", "Nachname", "E-Mail", "Telefon", "Strasse", "Hausnummer", "PLZ", "Stadt", "besucht_am"])

    for row in besucher_liste:
        rowobj = [row.nachname, row.vorname, row.email, row.telefon, row.strasse, row.hausnummer, row.plz, row.stadt,
                  row.besucht_am]
        writer.writerow(rowobj)

    return response


class ViewBesucherListePDF(View):

    def get(self, request, *args, **kwargs):
        '''
                    Rendert die Besucherliste in eine PDF-Datei und öffnet sie im Browser
                            Parameters:
                                    self (object): Objekt
                                    request (HttpRequest): Ein Request-Objekt

                            Returns:
                                    HttpResponse(): Methode, um eine HTTP-Response zu erstellen mit der PDF und
                                    sie im Browser zu öffnen
        '''
        kunde = Kunde.objects.get(email=request.user.email)
        besucher_liste = kunde.besucher_set.all()
        data = {"besucher_liste": besucher_liste, "datum": timezone.now()}
        pdf = render_to_pdf('menucard/besucherliste_pdf.html', data)
        return HttpResponse(pdf, content_type='application/pdf')


class DownloadBesucherlistePDF(View):

    def get(self, request, *args, **kwargs):
        '''
                    Rendert die Besucherliste in eine PDF-Datei und öffnet sie im Browser
                            Parameters:
                                    self (object): Objekt
                                    request (HttpRequest): Ein Request-Objekt

                            Returns:
                                    HttpResponse(): Methode, um eine HTTP-Response zu erstellen mit der PDF und
                                    sie im Browser zu öffnen
        '''
        kunde = Kunde.objects.get(email=request.user.email)
        besucher_liste = kunde.besucher_set.all()
        data = {"besucher_liste": besucher_liste, "datum": timezone.now()}
        pdf = render_to_pdf('menucard/besucherliste_pdf.html', data)

        response = HttpResponse(pdf, content_type='application/pdf')
        filename = "Besucherliste.pdf"
        content = "attachment; filename='%s'" % (filename)
        response['Content-Disposition'] = content

        return response

class DownloadPDF_Rechnung(View):

    def get(self, request, *args, **kwargs):
        '''
                    Rendert die Rechnung in eine PDF-Datei und lädt sie herunter
                            Parameters:
                                    self (object): Objekt
                                    request (HttpRequest): Ein Request-Objekt

                            Returns:
                                    HttpResponse(): Methode, um eine HTTP-Response zu erstellen mit der PDF und
                                    sie herunterzuladen
        '''
        reg_kunde = Kunde.objects.get(email=request.user.email)
        rechnung = reg_kunde.rechnung_set.order_by('-datum')[0]
        data = {"rechnung": rechnung, "datum": timezone.now()}
        pdf = render_to_pdf('menucard/menucard_rechnung_pdf.html', data)
        
        response = HttpResponse(pdf, content_type='application/pdf')
        filename = "Rechnung_%s.pdf" % (reg_kunde.vorname + reg_kunde.nachname)
        content = "attachment; filename='%s'" % (filename)
        response['Content-Disposition'] = content
        return response


def test_qr(request):
    '''
                Erstellt einen QR-Code für die Menükarte des Lokalbesitzers, rendert ihn in eine PDF
                und lädt sie runter Inhalt in ein PDF
                        Parameters:
                                request (Http-Request): Ein Request-Objekt

                        Returns:
                                response: PDF-Datei mit QR-Code heruntergeladen
    '''
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="QRCode.pdf"'

    p = canvas.Canvas(response)
    p.setPageSize((500, 500))
    p.setTitle('Dein QR-Code')
    p.drawCentredString(x=250, y=460, text='SCAN FOR MENUCARD')
    qrw = QrCodeWidget(f"happy-qr.herokuapp.com/menucard/menucard_view/{request.user.username}")
    b = qrw.getBounds()

    w = b[2] - b[0]
    h = b[3] - b[1]

    d = Drawing(490, 490, transform=[490. / w, 0, 0, 490. / h, 0, 0])

    d.add(qrw)

    renderPDF.draw(d, p, 1, 1)

    p.showPage()
    p.save()
    return response


def datenschutz(request):
    '''
                    Gibt HTML-Template mit der Datenschutz-Info zurück

                            Parameters:
                                    request (HttpRequest): Ein Request-Objekt

                            Returns:
                                    render(): Gibt das Datenschutz-HTML-Template zurück
    '''
    return render(request, 'menucard/datenerfassung_info.html')


def kunden_handbuch(request):
    '''
                    Gibt HTML-Template mit dem Benutzerhandbuch für den Kunden zurück

                            Parameters:
                                    request (HttpRequest): Ein Request-Objekt

                            Returns:
                                    render(): Gibt das Handbuch-HTML-Template zurück
    '''
    return render(request, 'menucard/handbuch.html')
