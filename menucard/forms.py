from django.forms import ModelForm
from .models import *


class VorspeiseForm(ModelForm):
    class Meta:
        model = Vorspeise
        fields = '__all__'


class HauptspeiseForm(ModelForm):
    class Meta:
        model = Hauptspeise
        fields = '__all__'


class NachspeiseForm(ModelForm):
    class Meta:
        model = Nachspeise
        fields = '__all__'


class SnacksForm(ModelForm):
    class Meta:
        model = Snacks
        fields = '__all__'


class AlkfreieDrinksForm(ModelForm):
    class Meta:
        model = AlkoholfreieDrinks
        fields = '__all__'


class AlkhaltigeDrinksForm(ModelForm):
    class Meta:
        model = AlkoholhaltigeDrinks
        fields = '__all__'
