from django.forms import ModelForm
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms



class KundeForm(ModelForm):
    class Meta:
        model = Kunde
        fields = '__all__'


class MitarbeiterForm(ModelForm):
    class Meta:
        model = Mitarbeiter
        fields = '__all__'

class AuftragForm(ModelForm):
    class Meta:
        model = Auftrag
        fields = "__all__"

class RechnungForm(ModelForm):
    class Meta:
        model = Rechnung
        fields = "__all__"

class CreateUserForm(UserCreationForm):
    first_name = forms.CharField(required=True, label='Vorname')
    last_name = forms.CharField(required=True, label='Nachname')
    email = forms.EmailField(required=True, label='E-Mail')

    class Meta:
        model = User
        fields = ["username", "first_name", "last_name", "email", "password1", "password2"]

