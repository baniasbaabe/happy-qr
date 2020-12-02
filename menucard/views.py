from django.contrib import messages
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect

# Create your views here.
from crm.models import Auftrag
from menucard.forms import *
from menucard.models import Vorspeise, Hauptspeise, Nachspeise, Snacks, AlkoholfreieDrinks, AlkoholhaltigeDrinks

from crm.decoraters import *


def logout_view(request):
    logout(request)
    messages.info(request, 'Sie haben sich erfolgreich ausgeloggt.')
    return redirect('login')


# DASHBOARD
@login_required(login_url='login')
@genehmigte_user(allowed_roles=['kunde'])
def dashboard(request):
    kunde = Kunde.objects.get(email=request.user.email)
    auftrag = request.user.kunde.auftrag_set.first()

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
    kunde = Kunde.objects.get(email=request.user.email)
    vorspeise = kunde.vorspeise_set.all()
    context = {'vorspeise': vorspeise}
    return render(request, 'menucard/vorspeisen.html', context)


@login_required(login_url='login')
@genehmigte_user(allowed_roles=['kunde'])
def vorspeisen_anlegen(request):
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
    kunde = Kunde.objects.get(email=request.user.email)
    hauptspeise = kunde.hauptspeise_set.all()

    context = {'hauptspeisen': hauptspeise}
    return render(request, 'menucard/hauptspeisen.html', context)


@login_required(login_url='login')
@genehmigte_user(allowed_roles=['kunde'])
def hauptspeisen_anlegen(request):
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
    kunde = Kunde.objects.get(email=request.user.email)
    nachspeise = kunde.nachspeise_set.all()

    context = {'nachspeisen': nachspeise}
    return render(request, 'menucard/nachspeisen.html', context)


@login_required(login_url='login')
@genehmigte_user(allowed_roles=['kunde'])
def nachspeisen_anlegen(request):
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
    kunde = Kunde.objects.get(email=request.user.email)
    snacks = kunde.snacks_set.all()

    context = {'snack': snacks}
    return render(request, 'menucard/snacks.html', context)


@login_required(login_url='login')
@genehmigte_user(allowed_roles=['kunde'])
def snacks_anlegen(request):
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
    kunde = Kunde.objects.get(email=request.user.email)
    alkdrink = kunde.alkoholhaltigedrinks_set.all()

    context = {'alkdrink': alkdrink}
    return render(request, 'menucard/alkoholhaltigedrinks.html', context)


@login_required(login_url='login')
@genehmigte_user(allowed_roles=['kunde'])
def alkoholhaltigedrinks_anlegen(request):
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
    alkdrink = AlkoholhaltigeDrinks.objects.get(id=pk)
    form = AlkhaltigeDrinksForm(instance=alkdrink)

    if request.method == 'POST':
        form = AlkfreieDrinksForm(request.POST, instance=alkdrink)
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
    kunde = Kunde.objects.get(email=request.user.email)
    softdrink = kunde.alkoholfreiedrinks_set.all()

    context = {'softdrink': softdrink}
    return render(request, 'menucard/alkfreiedrinks.html', context)


@login_required(login_url='login')
@genehmigte_user(allowed_roles=['kunde'])
def alkfreiedrinks_anlegen(request):
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
    softdrink = AlkoholfreieDrinks.objects.get(id=pk)

    if request.method == "POST":
        softdrink.delete()
        return redirect('alkfreiedrinks')

    context = {"softdrink": softdrink}
    return render(request, 'menucard/alkfreiedrinks_loeschen.html', context)


@login_required(login_url='login')
@genehmigte_user(allowed_roles=['kunde'])
def menucard(request, email):
    kunde = Kunde.objects.get(email=request.user.email)
    vorspeisen = kunde.vorspeise_set.all()
    hauptspeise = Hauptspeise.objects.all()
    nachspeise = Nachspeise.objects.all()
    snacks = Snacks.objects.all()
    softdrink = AlkoholfreieDrinks.objects.all()
    alkdrinks = AlkoholhaltigeDrinks.objects.all()
    template = kunde.template

    context = {
        'vorspeisen': vorspeisen,
        'hauptspeise': hauptspeise,
        'nachspeise': nachspeise,
        'snacks': snacks,
        'softdrink': softdrink,
        'alkdrinks': alkdrinks,
        'template': template,
        'kunde': kunde.email
    }
    return render(request, 'menucard/menucard.html', context)
