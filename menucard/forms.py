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
