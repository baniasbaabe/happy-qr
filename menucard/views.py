from django.contrib import messages
from django.shortcuts import render, redirect

# Create your views here.
from menucard.forms import *
from menucard.models import Vorspeise, Hauptspeise, Nachspeise, Snacks, AlkoholfreieDrinks, AlkoholhaltigeDrinks


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
