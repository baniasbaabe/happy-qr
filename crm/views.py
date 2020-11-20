from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.utils import timezone
from .models import *
from .forms import *
from io import BytesIO
from django.template.loader import get_template
from django.views import View
from xhtml2pdf import pisa
import csv


# Funktion um dashboard.html anzuzeigen mit sämtlichen Mitarbeitern
def dashboard(request):
    # Objekt erstellen
    mitarbeiter = Mitarbeiter.objects.all()

    # Objekt in der HTML Datei zur Verfügung stellen
    context= {
        'mitarbeiter':mitarbeiter,
    }

    # Ausgabe der HTML Datei
    return render(request, 'crm/dashboard.html', context)


# Start Kunden CRUD-Methoden-----------------------------------------------------------------------------------------

def kundenliste(request):  #hole alle kunden aus DB
    kunden = Kunde.objects.all()

    context = {"kunden": kunden,

               }
    return render(request, 'crm/kundenliste.html', context)


def KundeAnlegen(request):
    form = KundeForm()
    if request.method == "POST":
        form = KundeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('kundenliste')
    context = {'form': form}

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

    context = {"kunde": kunde}
    return render(request, 'crm/delete_kunde.html', context)


# Ende Kunden CRUD-Methoden-----------------------------------------------------------------------------------------

# Start Mitarbeiter CRUD-Methoden-----------------------------------------------------------------------------------------

def mitarbeiterliste(request): #hole alle Mitarbeiter aus DB
    mitarbeiter = Mitarbeiter.objects.all()

    context = {"mitarbeiter": mitarbeiter,

               }
    return render(request, 'crm/mitarbeiterliste.html', context)


def mitarbeiterAnlegen(request):
    form = MitarbeiterForm()
    if request.method == "POST":
        form = MitarbeiterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('mitarbeiterliste')
    context = {'form': form}

    return render(request, 'crm/mitarbeiter_form.html', context)


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


def mitarbeiterLoeschen(request, pk):
    mitarbeiter = Mitarbeiter.objects.get(id=pk)

    if request.method == "POST":
        mitarbeiter.delete()
        return redirect('mitarbeiterliste')

    context = {"mitarbeiter": mitarbeiter}
    return render(request, 'crm/delete_mitarbeiter.html', context)

# Ende Mitarbeiter CRUD-Methoden-----------------------------------------------------------------------------------------

def auftragsliste(request):  #hole alle Aufträge aus DB
    auftraege = Auftrag.objects.all()

    context = {"auftraege":auftraege,

               }
    return render(request, 'crm/auftragsliste.html', context)

def auftragAnlegen(request):

    form = AuftragForm()

    if request.method == "POST":
        form = AuftragForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('auftragsliste')

    context = {'form': form}

    return render(request, "crm/auftrag_form.html", context)

def auftragAktualisieren(request, pk):
    auftrag =Auftrag.objects.get(id=pk)
    form =AuftragForm(instance=auftrag)


    if request.method == "POST":
        form = AuftragForm(request.POST, instance=auftrag)
        if form.is_valid():
            form.save()
            return redirect('auftragsliste')

    context = {'form': form}

    return render(request, "crm/auftrag_form.html", context)

def auftragLoeschen(request, pk):
    auftrag = Auftrag.objects.get(id=pk)

    if request.method == "POST":
        auftrag.delete()
        return redirect('auftragsliste')

    context = {"auftrag":auftrag}
    return render(request, 'crm/delete_auftrag.html', context)

def rechnungsliste(request):  #hole alle Rechnungen aus DB
    rechnungen = Rechnung.objects.all()

    context = {"rechnungen":rechnungen,

               }
    return render(request, 'crm/rechnungsliste.html', context)

def rechnungAnlegen(request):

    form = RechnungForm()

    if request.method == "POST":
        form = RechnungForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('rechnungsliste')

    context = {'form': form}

    return render(request, "crm/rechnung_form.html", context)

def rechnungAktualisieren(request, pk):
    auftrag = Rechnung.objects.get(id=pk)
    form =RechnungForm(instance=auftrag)


    if request.method == "POST":
        form = AuftragForm(request.POST, instance=auftrag)
        if form.is_valid():
            form.save()
            return redirect('rechnungsliste')

    context = {'form': form}

    return render(request, "crm/rechnung_form.html", context)

def rechnungLoeschen(request, pk):
    rechnung = Rechnung.objects.get(id=pk)

    if request.method == "POST":
        rechnung.delete()
        return redirect('rechnungsliste')

    context = {"rechnung":rechnung}
    return render(request, 'crm/delete_rechnung.html', context)

def render_to_pdf(template_src, context_dict):

    template = get_template(template_src)
    html  = template.render(context_dict)
    result = BytesIO()
    pdf = pisa.pisaDocument(BytesIO(html.encode("ISO-8859-1")), result)
    if not pdf.err:
        return HttpResponse(result.getvalue(), content_type='application/pdf')
    return None

def csv_download(request, pk):

    rechnung = Rechnung.objects.get(id=pk)

    response = HttpResponse(content_type='text/csv')
    filename = "Rechnung_%s.csv" %(rechnung.id)
    content = "attachment; filename='%s'" % (filename)
    response['Content-Disposition'] = content

    writer = csv.writer(response, delimiter =",")
    writer.writerow(["Vorname", "Nachname", "EMail", "Telefon","Web", "Produkt","Preis"])

    writer.writerow([rechnung.kunde.vorname, rechnung.kunde.nachname, rechnung.kunde.email,
                     rechnung.kunde.telefon, rechnung.kunde.web, rechnung.auftrag.produkt,
                     rechnung.auftrag.preis])

    return response

#Opens up page as PDF
class ViewPDF(View):
    from .models import Kunde, Rechnung, Auftrag
    def get(self, request,pk,*args, **kwargs):
        rechnung = Rechnung.objects.get(id=pk)
        data = {"rechnung":rechnung, "datum":timezone.now()}
        pdf = render_to_pdf('crm/rechnung_pdf.html', data)
        return HttpResponse(pdf, content_type='application/pdf')


class DownloadPDF(View):
    def get(self, request, pk,*args, **kwargs):
        rechnung = Rechnung.objects.get(id=pk)
        data = {"rechnung": rechnung, "datum": timezone.now()}
        pdf = render_to_pdf('crm/rechnung_pdf.html', data)

        response = HttpResponse(pdf, content_type='application/pdf')
        filename = "Rechnung_%s.pdf" %(rechnung.id)
        content = "attachment; filename='%s'" %(filename)
        response['Content-Disposition'] = content
        return response