from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.utils import timezone
from django.contrib.auth.forms import UserCreationForm
from urllib3.filepost import writer

from .decoraters import nicht_authentifizierter_user, genehmigte_user
from .models import *
from .forms import *
from io import BytesIO
from django.template.loader import get_template
from django.views import View
from xhtml2pdf import pisa
import csv
from django.contrib import messages
from django.contrib.auth.models import Group
import sqlite3
from sqlite3 import Error




@nicht_authentifizierter_user
def register_view(request):
    form = CreateUserForm()

    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')

            group = Group.objects.get(name="kunde")
            user.groups.add(group)
            Kunde.objects.create(user=user, vorname=user.first_name, nachname=user.last_name, email=user.email)
            messages.success(request, "User wurde erfolgreich erstellt für " + username)
            return redirect('login')

    context = {"form": form}
    return render(request, 'crm/registrierung.html', context)


@nicht_authentifizierter_user
def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            if user.groups.filter(name__in=['mitarbeiter']):
                login(request, user)
                return redirect('crm_dashboard')
            elif user.groups.filter(name__in=['kunde']):
                login(request, user)
                return redirect('menucard_dashboard')

        else:
            messages.info(request, 'Username oder Passwort falsch.')
    context = {}
    return render(request, 'crm/login.html', context)


def logout_view(request):
    logout(request)
    messages.info(request, 'Sie haben sich erfolgreich ausgeloggt.')
    return redirect('login')


# Funktion um dashboard.html anzuzeigen mit sämtlichen Mitarbeitern
@login_required(login_url='login')
@genehmigte_user(allowed_roles=['mitarbeiter'])
def dashboard(request):
    # Objekt erstellen
    mitarbeiter = Mitarbeiter.objects.all()

    # Objekt in der HTML Datei zur Verfügung stellen
    context = {
        'mitarbeiter': mitarbeiter,
    }

    # Ausgabe der HTML Datei
    return render(request, 'crm/dashboard.html', context)


# Start Kunden CRUD-Methoden-----------------------------------------------------------------------------------------
@login_required(login_url='login')
@genehmigte_user(allowed_roles=['mitarbeiter'])
def kundenliste(request):  # hole alle kunden aus DB
    kunden = Kunde.objects.all()

    context = {"kunden": kunden}
    return render(request, 'crm/kundenliste.html', context)


@login_required(login_url='login')
@genehmigte_user(allowed_roles=['mitarbeiter'])
def KundeAnlegen(request):
    form = KundeForm()
    if request.method == "POST":
        form = KundeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('kundenliste')
    context = {'form': form}

    return render(request, 'crm/kunde_form.html', context)


@login_required(login_url='login')
@genehmigte_user(allowed_roles=['mitarbeiter'])
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


@login_required(login_url='login')
@genehmigte_user(allowed_roles=['mitarbeiter'])
def KundeLoeschen(request, pk):
    kunde = Kunde.objects.get(id=pk)

    if request.method == "POST":
        kunde.delete()
        return redirect('kundenliste')

    context = {"kunde": kunde}
    return render(request, 'crm/delete_kunde.html', context)


# Ende Kunden CRUD-Methoden-----------------------------------------------------------------------------------------

# Start Mitarbeiter CRUD-Methoden-----------------------------------------------------------------------------------------
@login_required(login_url='login')
@genehmigte_user(allowed_roles=['mitarbeiter'])
def mitarbeiterliste(request):  # hole alle Mitarbeiter aus DB
    mitarbeiter = Mitarbeiter.objects.all()

    context = {"mitarbeiter": mitarbeiter,

               }
    return render(request, 'crm/mitarbeiterliste.html', context)


@login_required(login_url='login')
@genehmigte_user(allowed_roles=['mitarbeiter'])
def mitarbeiterAnlegen(request):
    form = MitarbeiterForm()
    if request.method == "POST":
        form = MitarbeiterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('mitarbeiterliste')
    context = {'form': form}

    return render(request, 'crm/mitarbeiter_form.html', context)


@login_required(login_url='login')
@genehmigte_user(allowed_roles=['mitarbeiter'])
def mitarbeiterAktualisieren(request, pk):
    mitarbeiter = Mitarbeiter.objects.get(id=pk)
    form = MitarbeiterForm(instance=mitarbeiter)

    if request.method == "POST":
        form = MitarbeiterForm(request.POST, instance=mitarbeiter)
        if form.is_valid():
            form.save()
            return redirect('mitarbeiterliste')

    context = {'form': form}

    return render(request, "crm/mitarbeiter_form.html", context)


@login_required(login_url='login')
@genehmigte_user(allowed_roles=['mitarbeiter'])
def mitarbeiterLoeschen(request, pk):
    mitarbeiter = Mitarbeiter.objects.get(id=pk)

    if request.method == "POST":
        mitarbeiter.delete()
        return redirect('mitarbeiterliste')

    context = {"mitarbeiter": mitarbeiter}
    return render(request, 'crm/delete_mitarbeiter.html', context)


# Ende Mitarbeiter CRUD-Methoden----------------------------------------------------------------------------------------
@login_required(login_url='login')
@genehmigte_user(allowed_roles=['mitarbeiter'])
def auftragsliste(request):  # hole alle Aufträge aus DB
    auftraege = Auftrag.objects.all()

    context = {"auftraege": auftraege,

               }
    return render(request, 'crm/auftragsliste.html', context)


@login_required(login_url='login')
@genehmigte_user(allowed_roles=['mitarbeiter'])
def auftragAnlegen(request):
    form = AuftragForm()

    if request.method == "POST":
        form = AuftragForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('auftragsliste')

    context = {'form': form}

    return render(request, "crm/auftrag_form.html", context)


@login_required(login_url='login')
@genehmigte_user(allowed_roles=['mitarbeiter'])
def auftragAktualisieren(request, pk):
    auftrag = Auftrag.objects.get(id=pk)
    form = AuftragForm(instance=auftrag)

    if request.method == "POST":
        form = AuftragForm(request.POST, instance=auftrag)
        if form.is_valid():
            form.save()
            return redirect('auftragsliste')

    context = {'form': form}

    return render(request, "crm/auftrag_form.html", context)


@login_required(login_url='login')
@genehmigte_user(allowed_roles=['mitarbeiter'])
def auftragLoeschen(request, pk):
    auftrag = Auftrag.objects.get(id=pk)

    if request.method == "POST":
        auftrag.delete()
        return redirect('auftragsliste')

    context = {"auftrag": auftrag}
    return render(request, 'crm/delete_auftrag.html', context)


@login_required(login_url='login')
@genehmigte_user(allowed_roles=['mitarbeiter'])
def rechnungsliste(request):  # hole alle Rechnungen aus DB
    rechnungen = Rechnung.objects.all()

    context = {"rechnungen": rechnungen,

               }
    return render(request, 'crm/rechnungsliste.html', context)


@login_required(login_url='login')
@genehmigte_user(allowed_roles=['mitarbeiter'])
def rechnungAnlegen(request):
    form = RechnungForm()

    if request.method == "POST":
        form = RechnungForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('rechnungsliste')

    context = {'form': form}

    return render(request, "crm/rechnung_form.html", context)


@login_required(login_url='login')
@genehmigte_user(allowed_roles=['mitarbeiter'])
def rechnungAktualisieren(request, pk):
    auftrag = Rechnung.objects.get(id=pk)
    form = RechnungForm(instance=auftrag)

    if request.method == "POST":
        form = AuftragForm(request.POST, instance=auftrag)
        if form.is_valid():
            form.save()
            return redirect('rechnungsliste')

    context = {'form': form}

    return render(request, "crm/rechnung_form.html", context)


@login_required(login_url='login')
@genehmigte_user(allowed_roles=['mitarbeiter'])
def rechnungLoeschen(request, pk):
    rechnung = Rechnung.objects.get(id=pk)

    if request.method == "POST":
        rechnung.delete()
        return redirect('rechnungsliste')

    context = {"rechnung": rechnung}
    return render(request, 'crm/delete_rechnung.html', context)


# Lassen
def render_to_pdf(template_src, context_dict):
    template = get_template(template_src)
    html = template.render(context_dict)
    result = BytesIO()
    pdf = pisa.pisaDocument(BytesIO(html.encode("ISO-8859-1")), result)
    if not pdf.err:
        return HttpResponse(result.getvalue(), content_type='application/pdf')
    return None


def csv_download(request, pk):
    rechnung = Rechnung.objects.get(id=pk)

    response = HttpResponse(content_type='text/csv')
    filename = "Rechnung_%s.csv" % (rechnung.id)
    content = "attachment; filename='%s'" % (filename)
    response['Content-Disposition'] = content

    writer = csv.writer(response, delimiter=";")
    writer.writerow(["Vorname", "Nachname", "EMail", "Telefon", "Web", "Produkt", "Preis"])

    writer.writerow([rechnung.kunde.vorname, rechnung.kunde.nachname, rechnung.kunde.email,
                     rechnung.kunde.telefon, rechnung.kunde.web, rechnung.auftrag.produkt,
                     rechnung.auftrag.preis])

    return response


# Opens up page as PDF


class ViewPDF(View):
    from .models import Kunde, Rechnung, Auftrag

    def get(self, request, pk, *args, **kwargs):
        rechnung = Rechnung.objects.get(id=pk)
        data = {"rechnung": rechnung, "datum": timezone.now()}
        pdf = render_to_pdf('crm/rechnung_pdf.html', data)
        return HttpResponse(pdf, content_type='application/pdf')


class DownloadPDF(View):

    def get(self, request, pk, *args, **kwargs):
        rechnung = Rechnung.objects.get(id=pk)
        data = {"rechnung": rechnung, "datum": timezone.now()}
        pdf = render_to_pdf('crm/rechnung_pdf.html', data)

        response = HttpResponse(pdf, content_type='application/pdf')
        filename = "Rechnung_%s.pdf" % (rechnung.id)
        content = "attachment; filename='%s'" % (filename)
        response['Content-Disposition'] = content
        return response


# Kundenliste PDF/CSV


def csv_download_kundenliste(request):
    kunden_liste = Kunde.objects.all()

    response = HttpResponse(content_type='text/csv')
    filename = "Kundenliste.csv"
    content = "attachment; filename='%s'" % (filename)
    response['Content-Disposition'] = content

    writer = csv.writer(response, delimiter="\t")
    writer.writerow(["Vorname", "Nachname", "E-Mail", "Telefon", "Web", "Notiz"])

    for row in kunden_liste:
        rowobj = [row.nachname, row.vorname, row.email, row.telefon, row.web, row.notiz]
        writer.writerow(rowobj)

    return response


class ViewKundenListePDF(View):
    from .models import Kunde

    def get(self, request, *args, **kwargs):
        kunden_liste = Kunde.objects.all()
        data = {"kunden_liste": kunden_liste, "datum": timezone.now()}
        pdf = render_to_pdf('crm/kundenliste_pdf.html', data)
        return HttpResponse(pdf, content_type='application/pdf')


class DownloadKundenlistePDF(View):

    def get(self, request, *args, **kwargs):
        kunden_liste = Kunde.objects.all()
        data = {"kunden_liste": kunden_liste, "datum": timezone.now()}
        pdf = render_to_pdf('crm/kundenliste_pdf.html', data)

        response = HttpResponse(pdf, content_type='application/pdf')
        filename = "Kundenliste.pdf"
        content = "attachment; filename='%s'" % (filename)
        response['Content-Disposition'] = content

        return response


class DownloadAuftragslistePDF(View):

    def get(self, request, *args, **kwargs):
        auftrags_liste = Auftrag.objects.all()
        data = {"auftrags_liste": auftrags_liste, "datum": timezone.now()}
        pdf = render_to_pdf('crm/auftragsliste_pdf.html', data)

        response = HttpResponse(pdf, content_type='application/pdf')
        filename = 'Auftragsliste.pdf'
        content = "attachment; filename='%s'" % (filename)
        response['Content-Disposition'] = content

        return response


def csv_download_auftragsliste(request):
    auftrags_liste = Auftrag.objects.all()

    response = HttpResponse(content_type='text/csv')
    filename = "Auftragsliste.csv"
    content = "attachment; filename='%s'" % (filename)
    response['Content-Disposition'] = content

    writer = csv.writer(response, delimiter="\t")
    writer.writerow(["ID", "Kunde", "Datum", "Preis", "Notiz"])

    for row in auftrags_liste:
        rowobj = [row.id, row.kunde, row.auftrag_vom, row.preis, row.notiz]
        writer.writerow(rowobj)

    return response
