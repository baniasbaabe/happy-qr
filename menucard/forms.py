from django.forms import ModelForm
from django import forms
from .models import *


class VorspeiseForm(ModelForm):
    class Meta:
        model = Vorspeise
        fields = '__all__'
        widgets = {'kundeId': forms.HiddenInput()}


class HauptspeiseForm(ModelForm):
    class Meta:
        model = Hauptspeise
        fields = '__all__'
        widgets = {'kundeId': forms.HiddenInput()}


class NachspeiseForm(ModelForm):
    class Meta:
        model = Nachspeise
        fields = '__all__'
        widgets = {'kundeId': forms.HiddenInput()}


class SnacksForm(ModelForm):
    class Meta:
        model = Snacks
        fields = '__all__'
        widgets = {'kundeId': forms.HiddenInput()}


class AlkfreieDrinksForm(ModelForm):
    class Meta:
        model = AlkoholfreieDrinks
        fields = '__all__'
        labels = {
            'name' : 'Name',

        }
        widgets = {'kundeId': forms.HiddenInput()}


class AlkhaltigeDrinksForm(ModelForm):
    class Meta:
        model = AlkoholhaltigeDrinks
        fields = '__all__'
        widgets = {'kundeId': forms.HiddenInput()}


class TemplateForm(ModelForm):
    class Meta:
        model = Kunde
        fields = ['template']


class ProfilForm(ModelForm):
    class Meta:
        model = Kunde
        fields = ['web', 'telefon']


class CovidForm(ModelForm):
    class Meta:
        model = Besucher
        fields = "__all__"
        labels = {
            'email': 'E-Mail',
            'strasse': 'Straße',
            'plz': 'PLZ',
            'stadt': 'Ort'
        }
        widgets = {
            'kundeId': forms.HiddenInput(),
        }
