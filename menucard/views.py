from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect

# Create your views here.
from menucard.forms import *
from menucard.models import Vorspeise, Hauptspeise, Nachspeise, Snacks, AlkoholfreieDrinks, AlkoholhaltigeDrinks


# DASHBOARD
def dashboard(request):
    count_vorspeisen = Vorspeise.objects.count()
    count_hauptspeisen = Hauptspeise.objects.count()
    count_nachspeisen = Nachspeise.objects.count()
    count_snacks = Snacks.objects.count()
    count_alkfreidrinks = AlkoholfreieDrinks.objects.count()
    count_alkdrinks = AlkoholhaltigeDrinks.objects.count()

    context = {
        'count_vorspeisen': count_vorspeisen,
        'count_hauptspeisen': count_hauptspeisen,
        'count_nachspeisen': count_nachspeisen,
        'count_snacks': count_snacks,
        'count_alkfreidrinks': count_alkfreidrinks,
        'count_alkdrinks': count_alkdrinks,
    }
    return render(request, 'menucard/dashboard.html', context)


# VORSPEISEN CRUD
def vorspeisen(request):
    vorspeise = Vorspeise.objects.all()
    context = {'vorspeise': vorspeise}
    return render(request, 'menucard/vorspeisen.html', context)


def vorspeisen_anlegen(request):
    vorspeise = Vorspeise()
    form = VorspeiseForm(initial={'vorspeise': vorspeise})

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


def vorspeisen_loeschen(request, pk):
    vorspeise = Vorspeise.objects.get(id=pk)

    if request.method == "POST":
        vorspeise.delete()
        return redirect('vorspeisen')

    context = {"vorspeise": vorspeise}
    return render(request, 'menucard/vorspeise_loeschen.html', context)


# HAUPTSPEISEN CRUD
def hauptspeisen(request):
    hauptspeise = Hauptspeise.objects.all()
    context = {'hauptspeisen': hauptspeise}
    return render(request, 'menucard/hauptspeisen.html', context)


def hauptspeisen_anlegen(request):
    hauptspeise = Hauptspeise()
    form = HauptspeiseForm(initial={'hauptspeise': hauptspeise})

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


def hauptspeise_loeschen(request, pk):
    hauptspeise = Hauptspeise.objects.get(id=pk)

    if request.method == "POST":
        hauptspeise.delete()
        return redirect('hauptspeisen')

    context = {"hauptspeise": hauptspeise}
    return render(request, 'menucard/hauptspeise_loeschen.html', context)


# NACHSPEISEN CRUD
def nachspeisen(request):
    nachspeise = Nachspeise.objects.all()
    context = {'nachspeisen': nachspeise}
    return render(request, 'menucard/nachspeisen.html', context)


def nachspeisen_anlegen(request):
    nachspeise = Nachspeise()
    form = VorspeiseForm(initial={'nachspeisen': nachspeisen})

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


def nachspeisen_loeschen(request, pk):
    nachspeise = Nachspeise.objects.get(id=pk)

    if request.method == "POST":
        nachspeise.delete()
        return redirect('nachspeisen')

    context = {"nachspeise": nachspeise}
    return render(request, 'menucard/nachspeise_loeschen.html', context)


# SNACKS CRUD
def snacks(request):
    snack = Snacks.objects.all()
    context = {'snack': snack}
    return render(request, 'menucard/snacks.html', context)


def snacks_anlegen(request):
    snack = Snacks()
    form = SnacksForm(initial={'snack': snack})

    if request.method == "POST":
        form = SnacksForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('snacks')
        else:
            messages.info(request, 'Bitte überprüfen Sie Ihre Eingabe.')

    context = {'form': form}
    return render(request, "menucard/snacks_anlegen.html", context)


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


def snacks_loeschen(request, pk):
    snack = Snacks.objects.get(id=pk)

    if request.method == "POST":
        snack.delete()
        return redirect('snacks')

    context = {"snack": snack}
    return render(request, 'menucard/snacks_loeschen.html', context)


# ALKOHOLHALTIGE GETRÄNKE CRUD
def alkoholhaltigedrinks(request):
    alkdrink = AlkoholhaltigeDrinks.objects.all()
    context = {'alkdrink': alkdrink}
    return render(request, 'menucard/alkoholhaltigedrinks.html', context)


def alkoholhaltigedrinks_anlegen(request):
    alkdrink = AlkoholhaltigeDrinks()
    form = AlkhaltigeDrinksForm(initial={'alkdrink': alkdrink})

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


def alkoholhaltigedrinks_loeschen(request, pk):
    alkdrink = AlkoholhaltigeDrinks.objects.get(id=pk)

    if request.method == "POST":
        alkdrink.delete()
        return redirect('alkoholhaltigedrinks')

    context = {"alkdrink": alkdrink}
    return render(request, 'menucard/alkoholhaltigedrinks_loeschen.html', context)


# ALKOHOLFREIE GETRÄNKE CRUD
def alkfreiedrinks(request):
    softdrink = AlkoholfreieDrinks.objects.all()
    context = {'softdrink': softdrink}
    return render(request, 'menucard/alkfreiedrinks.html', context)


def alkfreiedrinks_anlegen(request):
    softdrink = AlkoholfreieDrinks()
    form = AlkfreieDrinksForm(initial={'softdrink': softdrink})

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


def alkfreiedrinks_loeschen(request, pk):
    softdrink = AlkoholfreieDrinks.objects.get(id=pk)

    if request.method == "POST":
        softdrink.delete()
        return redirect('alkfreiedrinks')

    context = {"softdrink": softdrink}
    return render(request, 'menucard/alkfreiedrinks_loeschen.html', context)


def menucard(request):
    vorspeisen = Vorspeise.objects.all()
    hauptspeise = Hauptspeise.objects.all()
    nachspeise = Nachspeise.objects.all()
    snacks = Snacks.objects.all()
    softdrink = AlkoholfreieDrinks.objects.all()
    alkdrinks = AlkoholhaltigeDrinks.objects.all()

    context = {
        'vorspeisen': vorspeisen,
        'hauptspeise': hauptspeise,
        'nachspeise': nachspeise,
        'snacks': snacks,
        'softdrink': softdrink,
        'alkdrinks': alkdrinks,
    }
    return render(request, 'menucard/menucard.html', context)
