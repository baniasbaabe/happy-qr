from django.forms import ModelForm
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms


class KundeForm(ModelForm):
    """
            Eine Klasse zur Repräsentation einer Kundenform

            ...

            Classes
            ----------
            Meta:
                Felderdefinitionen der Form

    """
    class Meta:
        """
                Eine Klasse zur Repräsentation der Metadaten

                ...

                Attributes
                ----------
                model : Kunde
                    Kundenobjekt
                fields : string
                    Felder des Kunden
                widgets : dictionary
                    Die unsichtbaren Felder


        """
        model = Kunde
        fields = '__all__'
        widgets = {'user': forms.HiddenInput(),
                   'template': forms.HiddenInput()}


class MitarbeiterForm(ModelForm):
    """
            Eine Klasse zur Repräsentation einer Mitarbeiterform

            ...

            Classes
            ----------
            Meta:
                Felderdefinitionen der Form

    """
    class Meta:
        """
                Eine Klasse zur Repräsentation der Metadaten

                ...

                Attributes
                ----------
                model : Kunde
                    Mitarbeiterobjekt
                fields : string
                    Felder des Mitarbeiters



        """
        model = Mitarbeiter
        fields = '__all__'


class AuftragForm(ModelForm):
    """
            Eine Klasse zur Repräsentation einer Auftragform

            ...

            Classes
            ----------
            Meta:
                Felderdefinitionen der Form

    """
    class Meta:
        """
                Eine Klasse zur Repräsentation der Metadaten

                ...

                Attributes
                ----------
                model : Auftrag
                    Kundenobjekt
                fields : string
                    Felder des Auftrags



        """
        model = Auftrag
        fields = "__all__"


class RechnungForm(ModelForm):
    """
            Eine Klasse zur Repräsentation einer Rechnungform

            ...

            Classes
            ----------
            Meta:
                Felderdefinitionen der Form

    """
    class Meta:
        """
                Eine Klasse zur Repräsentation der Metadaten

                ...

                Attributes
                ----------
                model : Rechnung
                    Kundenobjekt
                fields : string
                    Felder der Rechnung



        """
        model = Rechnung
        fields = "__all__"


class CreateUserForm(UserCreationForm):
    """
            Eine Klasse zur Repräsentation einer Django-Userform

            ...

            Attributes
             ----------
            first_name : charfield
                Vorname des Users
            last_name : charfield
                Nachname des Users
            email : emailfield
                Email-Adresse des Users

            Classes
            ----------
            Meta:
                Felderdefinitionen der Form

    """
    first_name = forms.CharField(required=True, label='Vorname')
    last_name = forms.CharField(required=True, label='Nachname')
    email = forms.EmailField(required=True, label='E-Mail')

    class Meta:
        """
                Eine Klasse zur Repräsentation der Metadaten

                ...

                Attributes
                ----------
                model : User
                    Kundenobjekt
                fields : string
                    Felder des Users



        """
        model = User
        fields = ["username", "first_name", "last_name", "email", "password1", "password2"]
