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
    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]

