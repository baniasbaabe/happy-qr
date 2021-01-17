from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.utils import timezone

from .decoraters import nicht_authentifizierter_user, genehmigte_user
from .filter import *
from .forms import *
from io import BytesIO
from django.template.loader import get_template
from django.views import View
from xhtml2pdf import pisa
import csv
from django.contrib import messages
from django.contrib.auth.models import Group


@nicht_authentifizierter_user
def register_view(request):
    '''
        Erstellt einen User, gibt das HTML-Template der Registrierung mit der Form zurück

                Parameters:
                        request (HttpRequest): Ein Request-Objekt

                Returns:
                         redirect(): Methode, die ein HttpResponseRedirect der Login URL zurückgibt
                         render(): Methode, die das Registrierungs-Template mit dem Context-Dict kombiniert
                                    und gibt ein HttpResponse zurück mit dem gerenderten Text
    '''
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
    '''
            Gleicht die Eingabedaten ab und je nach Gruppe des Users wird er zu seinem
            Template weitergeleitet

                    Parameters:
                            request (HttpRequest): Ein Request-Objekt

                    Returns:
                             redirect(): Methode, die ein HttpResponseRedirect der CRM oder Menucard URL zurückgibt
                             render(): Methode, die das Login-Template mit dem Context-Dict kombiniert
                                        und gibt ein HttpResponse zurück mit dem gerenderten Text
    '''
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
    '''
                Loggt den User wieder aus und leitet ihn zur Login-Page weiter

                        Parameters:
                                request (HttpRequest): Ein Request-Objekt

                        Returns:
                                 redirect(): Methode, die ein HttpResponseRedirect
                                 Login-URL zurückgibt

    '''
    logout(request)
    messages.info(request, 'Sie haben sich erfolgreich ausgeloggt.')
    return redirect('login')


# Funktion um dashboard.html anzuzeigen
@login_required(login_url='login')
@genehmigte_user(allowed_roles=['mitarbeiter'])
def dashboard(request):
    '''
             Gibt die Auftragsdaten an das Template weiter zum Anzeigen des Dashboards für den
             Mitarbeiter

                    Parameters:
                            request (HttpRequest): Ein Request-Objekt

                    Returns:
                            render(): Methode, die das Dashboard-Template mit dem Context-Dict samt
                                        Auftragsdaten kombiniert und gibt ein HttpResponse zurück mit dem gerenderten
                                        Text
    '''
    auftraege = Auftrag.objects.all()
    total_auftraege = auftraege.count()
    in_bearbeitung = auftraege.filter(status='In Bearbeitung').count()
    eingegangen = auftraege.filter(status='Eingegangen').count()
    letzte_fuenf_auftraege = Auftrag.objects.all().order_by('-auftrag_vom')[:5]

    context = {
        'auftraege': letzte_fuenf_auftraege,
        'total_auftraege': total_auftraege,
        'in_bearbeitung': in_bearbeitung,
        'eingegangen': eingegangen
    }

    return render(request, 'crm/dashboard.html', context)


# Start Kunden CRUD-Methoden-----------------------------------------------------------------------------------------
@login_required(login_url='login')
@genehmigte_user(allowed_roles=['mitarbeiter'])
def kundenliste(request):
    '''
                 Gibt die Kundendaten und den Kundenfilter an das Template weiter zum Anzeigen der Kundenliste

                        Parameters:
                                request (HttpRequest): Ein Request-Objekt

                        Returns:
                                render(): Methode, die das Kundenlisten-Template mit dem Context-Dict samt
                                            Kundendaten und Kundenfilter kombiniert und gibt
                                            ein HttpResponse zurück mit dem gerenderten Text
    '''
    kunden = Kunde.objects.all()  # In der Variable 'kunden' werden nun sämtliche Kunden aus der DB gespeichert
    kunden_filter = KundenFilter(request.GET, queryset=kunden)
    kunde = kunden_filter.qs
    context = {'kunden': kunde, 'kunden_filter': kunden_filter}  # Übergebe 'kunden' an den Render-Parameter
    return render(request, 'crm/kundenliste.html',
                  context)  # kundenliste.html kann nun auf die Variable 'kunden' zugreifen


@login_required(login_url='login')
@genehmigte_user(allowed_roles=['mitarbeiter'])
def KundeAnlegen(request):
    '''
                 Gibt die Form zum Anlegen des Kunden an das Kundenform-Template weiter

                        Parameters:
                                request (HttpRequest): Ein Request-Objekt

                        Returns:
                                render(): Methode, die das Kundenform-Template mit der Form zum Anlegen
                                kombiniert und gibt ein HttpResponse zurück mit dem gerenderten Text
    '''
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
    '''
                 Gibt die Kundeaktualisieren-Form an das Kundenform-Template weiter

                        Parameters:
                                request (HttpRequest): Ein Request-Objekt
                                pk (int): Primärschlussel des Kunden

                        Returns:
                                render(): Methode, die das Kundenform-Template mit der Form zum Aktualisieren
                                kombiniert und gibt ein HttpResponse zurück mit dem gerenderten Text
    '''
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
    '''
                Gibt die Kundelöschen-Form an das Kundelöschen-Template weiter

                        Parameters:
                                request (HttpRequest): Ein Request-Objekt
                                pk (int): Primärschlussel des Kunden

                        Returns:
                                render(): Methode, die das Kundelöschen-Template mit der Form zum Löschen
                                kombiniert und gibt ein HttpResponse zurück mit dem gerenderten Text
    '''
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
    '''
                 Gibt die Mitarbeiterdaten und den Mitarbeiterfilter an das Template weiter zum Anzeigen der Mitarbeiter
                 liste

                        Parameters:
                                request (HttpRequest): Ein Request-Objekt

                        Returns:
                                render(): Methode, die das Mitarbeiterlisten-Template mit dem Context-Dict samt
                                            Mitarbeiterdaten und Mitarbeiterfilter kombiniert und gibt
                                            ein HttpResponse zurück mit dem gerenderten Text
    '''
    mitarbeiter = Mitarbeiter.objects.all()
    mitarbeiter_filter = MitarbeiterFilter(request.GET, queryset=mitarbeiter)
    mitarbeiter_singular = mitarbeiter_filter.qs

    context = {'mitarbeiter': mitarbeiter_singular, 'mitarbeiter_filter': mitarbeiter_filter}
    return render(request, 'crm/mitarbeiterliste.html', context)


@login_required(login_url='login')
@genehmigte_user(allowed_roles=['mitarbeiter'])
def mitarbeiterAnlegen(request):
    '''
                     Gibt die Form zum Anlegen des Mitarbeiters an das Mitarbeiterform-Template weiter

                            Parameters:
                                    request (HttpRequest): Ein Request-Objekt

                            Returns:
                                    render(): Methode, die das Mitarbeiterform-Template mit der Form zum Anlegen
                                    kombiniert und gibt ein HttpResponse zurück mit dem gerenderten Text
    '''
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
    '''
                Gibt die Mitarbeiteraktualisieren-Form an das Mitarbeiterform-Template weiter

                        Parameters:
                                request (HttpRequest): Ein Request-Objekt
                                pk (int): Primärschlussel des Mitarbeiters

                        Returns:
                                render(): Methode, die das Mitarbeiterform-Template mit der Form zum Aktualisieren
                                kombiniert und gibt ein HttpResponse zurück mit dem gerenderten Text
    '''
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
    '''
                Gibt die Mitarbeiterlöschen-Form an das Mitarbeiterlöschen-Template weiter

                        Parameters:
                                request (HttpRequest): Ein Request-Objekt
                                pk (int): Primärschlussel des Mitarbeiters

                        Returns:
                                render(): Methode, die das Mitarbeiterlöschen-Template mit der Form zum Löschen
                                kombiniert und gibt ein HttpResponse zurück mit dem gerenderten Text
    '''
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
    '''
                Gibt die Auftragsdaten und den Auftragsfilter an das Template weiter zum Anzeigen der Auftragsliste

                        Parameters:
                                request (HttpRequest): Ein Request-Objekt

                        Returns:
                                render(): Methode, die das Auftragslisten-Template mit dem Context-Dict samt
                                            Auftragsdaten und Auftragsfilter kombiniert und gibt ein HttpResponse zurück
                                            mit dem gerenderten Text
    '''
    auftraege = Auftrag.objects.all()
    auftrag_filter = AuftragsFilter(request.GET, queryset=auftraege)
    auftrag = auftrag_filter.qs

    context = {'auftraege': auftrag, 'auftrag_filter': auftrag_filter}
    return render(request, 'crm/auftragsliste.html', context)


@login_required(login_url='login')
@genehmigte_user(allowed_roles=['mitarbeiter'])
def auftragAnlegen(request):
    '''
                    Gibt die Form zum Anlegen des Auftrags an das Auftragsform-Template weiter

                            Parameters:
                                    request (HttpRequest): Ein Request-Objekt

                            Returns:
                                    render(): Methode, die das Auftragsform-Template mit der Form zum Anlegen
                                    kombiniert und gibt ein HttpResponse zurück mit dem gerenderten Text
    '''
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
    '''
                Gibt die Auftragaktualisieren-Form an das Auftragform-Template weiter

                        Parameters:
                                request (HttpRequest): Ein Request-Objekt
                                pk (int): Primärschlussel des Auftrags

                        Returns:
                                render(): Methode, die das Auftragform-Template mit der Form zum Aktualisieren
                                kombiniert und gibt ein HttpResponse zurück mit dem gerenderten Text
    '''
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
    '''
                Gibt die Auftraglöschen-Form an das Auftraglöschen-Template weiter

                        Parameters:
                                request (HttpRequest): Ein Request-Objekt
                                pk (int): Primärschlussel des Auftrags

                        Returns:
                                render(): Methode, die das Auftraglöschen-Template mit der Form zum Löschen
                                kombiniert und gibt ein HttpResponse zurück mit dem gerenderten Text
    '''
    auftrag = Auftrag.objects.get(id=pk)

    if request.method == "POST":
        auftrag.delete()
        return redirect('auftragsliste')

    context = {"auftrag": auftrag}
    return render(request, 'crm/delete_auftrag.html', context)


@login_required(login_url='login')
@genehmigte_user(allowed_roles=['mitarbeiter'])
def rechnungsliste(request):  # hole alle Rechnungen aus DB
    '''
                Gibt die Rechnungsdaten und den Rechnungsfilter an das Template weiter zum Anzeigen der Rechnungsliste

                        Parameters:
                                request (HttpRequest): Ein Request-Objekt

                        Returns:
                                render(): Methode, die das Rechnungslisten-Template mit dem Context-Dict samt
                                            Rechnungsdaten und Rechnungsfilter kombiniert und gibt ein HttpResponse zurück
                                            mit dem gerenderten Text
    '''
    rechnungen = Rechnung.objects.all()
    rechnung_filter = RechnungenFilter(request.GET, queryset=rechnungen)
    rechnung = rechnung_filter.qs

    context = {"rechnungen": rechnung, 'rechnung_filter': rechnung_filter}
    return render(request, 'crm/rechnungsliste.html', context)


@login_required(login_url='login')
@genehmigte_user(allowed_roles=['mitarbeiter'])
def rechnungAnlegen(request):
    '''
                    Gibt die Form zum Anlegen des Rechnung an das Rechnungsform-Template weiter

                            Parameters:
                                    request (HttpRequest): Ein Request-Objekt

                            Returns:
                                    render(): Methode, die das Rechnungsform-Template mit der Form zum Anlegen
                                    kombiniert und gibt ein HttpResponse zurück mit dem gerenderten Text
    '''
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
    '''
                Gibt die Rechnungaktualisieren-Form an das Rechnungform-Template weiter

                        Parameters:
                                request (HttpRequest): Ein Request-Objekt
                                pk (int): Primärschlussel der Rechnung

                        Returns:
                                render(): Methode, die das Rechnungform-Template mit der Form zum Aktualisieren
                                kombiniert und gibt ein HttpResponse zurück mit dem gerenderten Text
    '''
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
    '''
                Gibt die Rechnunglöschen-Form an das Rechnunglöschen-Template weiter

                        Parameters:
                                request (HttpRequest): Ein Request-Objekt
                                pk (int): Primärschlussel der Rechnung

                        Returns:
                                render(): Methode, die das Rechnunglöschen-Template mit der Form zum Löschen
                                kombiniert und gibt ein HttpResponse zurück mit dem gerenderten Text
    '''
    rechnung = Rechnung.objects.get(id=pk)

    if request.method == "POST":
        rechnung.delete()
        return redirect('rechnungsliste')

    context = {"rechnung": rechnung}
    return render(request, 'crm/delete_rechnung.html', context)


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


def csv_download(request, pk):
    '''
                Schreibt den Inhalt einer Rechnung in eine CSV-Datei und lädt sie runter
                        Parameters:
                                request (HttpRequest): Ein Request-Objekt
                                pk (int): Primärschlussel der Rechnung

                        Returns:
                                response: CSV-Datei mit Inhalt der Rechnung als Download
    '''
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


class ViewPDF(View):

    def get(self, request, pk, *args, **kwargs):
        '''
                    Rendert die Besucherliste in eine PDF-Datei und öffnet sie im Browser
                            Parameters:
                                    self (object): Objekt
                                    request (HttpRequest): Ein Request-Objekt
                                    pk (int): Primärschlüssel der Rechnung

                            Returns:
                                    HttpResponse(): Methode, um eine HTTP-Response zu erstellen mit der PDF und
                                    sie im Browser zu öffnen
        '''
        rechnung = Rechnung.objects.get(id=pk)
        data = {"rechnung": rechnung, "datum": timezone.now()}
        pdf = render_to_pdf('crm/rechnung_pdf.html', data)
        return HttpResponse(pdf, content_type='application/pdf')


class DownloadPDF(View):

    def get(self, request, pk, *args, **kwargs):
        '''
                    Rendert die Rechnung in eine PDF-Datei und lädt sie herunter
                            Parameters:
                                    self (object): Objekt
                                    request (HttpRequest): Ein Request-Objekt
                                    pk (int): Primärschlüssel der Rechnung
                            Returns:
                                    HttpResponse(): Methode, um eine HTTP-Response zu erstellen mit der PDF und
                                    sie herunterzuladen
        '''
        rechnung = Rechnung.objects.get(id=pk)
        data = {"rechnung": rechnung, "datum": timezone.now()}
        pdf = render_to_pdf('crm/rechnung_pdf.html', data)

        response = HttpResponse(pdf, content_type='application/pdf')
        filename = "Rechnung_%s.pdf" % (rechnung.id)
        content = "attachment; filename='%s'" % (filename)
        response['Content-Disposition'] = content
        return response


def csv_download_kundenliste(request):
    '''
                Schreibt den Inhalt der Kundenliste in eine CSV-Datei und lädt sie runter
                        Parameters:
                                request (HttpRequest): Ein Request-Objekt

                        Returns:
                                response: CSV-Datei mit Inhalt der Kundenliste als Download
    '''
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

    def get(self, request, *args, **kwargs):
        '''
                    Rendert die Kundenliste in eine PDF-Datei und öffnet sie im Browser
                            Parameters:
                                    self (object): Objekt
                                    request (HttpRequest): Ein Request-Objekt

                            Returns:
                                    HttpResponse(): Methode, um eine HTTP-Response zu erstellen mit der PDF und
                                    sie im Browser zu öffnen
        '''
        kunden_liste = Kunde.objects.all()
        data = {"kunden_liste": kunden_liste, "datum": timezone.now()}
        pdf = render_to_pdf('crm/kundenliste_pdf.html', data)
        return HttpResponse(pdf, content_type='application/pdf')


class DownloadKundenlistePDF(View):

    def get(self, request, *args, **kwargs):
        '''
                    Rendert die Kundenliste in eine PDF-Datei und lädt sie herunter
                            Parameters:
                                    self (object): Objekt
                                    request (HttpRequest): Ein Request-Objekt
                            Returns:
                                    HttpResponse(): Methode, um eine HTTP-Response zu erstellen mit der PDF und
                                    sie herunterzuladen
        '''
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
        '''
                    Rendert die Auftragsliste in eine PDF-Datei und lädt sie herunter
                            Parameters:
                                    self (object): Objekt
                                    request (HttpRequest): Ein Request-Objekt
                            Returns:
                                    HttpResponse(): Methode, um eine HTTP-Response zu erstellen mit der PDF und
                                    sie herunterzuladen
        '''
        auftrags_liste = Auftrag.objects.all()
        data = {"auftrags_liste": auftrags_liste, "datum": timezone.now()}
        pdf = render_to_pdf('crm/auftragsliste_pdf.html', data)

        response = HttpResponse(pdf, content_type='application/pdf')
        filename = 'Auftragsliste.pdf'
        content = "attachment; filename='%s'" % (filename)
        response['Content-Disposition'] = content

        return response


def csv_download_auftragsliste(request):
    '''
                Schreibt den Inhalt der Auftragsliste in eine CSV-Datei und lädt sie runter
                        Parameters:
                                request (HttpRequest): Ein Request-Objekt

                        Returns:
                                response: CSV-Datei mit Inhalt der Auftragsliste als Download
    '''
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
