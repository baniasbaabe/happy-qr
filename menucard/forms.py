from django.forms import ModelForm
from django import forms
from .models import *


class VorspeiseForm(ModelForm):
    """
            Eine Klasse zur Repräsentation einer Vorspeise

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
                model : Vorspeise
                    Vorspeiseobjekt
                fields : string
                    Felder der Vorspeise
                widgets : dictionary
                    Die unsichtbaren Felder


        """
        model = Vorspeise  # Verwendet die Attribute der Klasse Vorspeise als Input-Felder
        fields = '__all__'  # Ausgabe aller Felder
        widgets = {'kundeId': forms.HiddenInput()}  # Zeige das Input-Feld 'kundeId' nicht im Formular


class HauptspeiseForm(ModelForm):
    """
            Eine Klasse zur Repräsentation einer Hauptspeiseform

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
                model : Hauptspeise
                    Hauptspeiseobjekt
                fields : string
                    Felder der Hauptspeise
                widgets : dictionary
                    Die unsichtbaren Felder


        """
        model = Hauptspeise
        fields = '__all__'
        widgets = {'kundeId': forms.HiddenInput()}


class NachspeiseForm(ModelForm):
    """
            Eine Klasse zur Repräsentation einer Nachspeiseform

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
                model : Nachspeise
                    Nachspeiseobjekt
                fields : string
                    Felder der Nachspeise
                widgets : dictionary
                    Die unsichtbaren Felder


        """
        model = Nachspeise
        fields = '__all__'
        widgets = {'kundeId': forms.HiddenInput()}


class SnacksForm(ModelForm):
    """
            Eine Klasse zur Repräsentation einer Snackform

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
                model : Snacks
                    Snacksobjekt
                fields : string
                    Felder der Snacks
                widgets : dictionary
                    Die unsichtbaren Felder


        """
        model = Snacks
        fields = '__all__'
        widgets = {'kundeId': forms.HiddenInput()}


class AlkfreieDrinksForm(ModelForm):
    """
            Eine Klasse zur Repräsentation einer Alkfreiendrinkform

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
                model : AlkfreieDrinks
                    Alkfreiedrinksobjekt
                fields : string
                    Felder der Alkfreiendrinks
                widgets : dictionary
                    Die unsichtbaren Felder


        """
        model = AlkoholfreieDrinks
        fields = '__all__'
        labels = {
            'name': 'Name',

        }
        widgets = {'kundeId': forms.HiddenInput()}


class AlkhaltigeDrinksForm(ModelForm):
    """
            Eine Klasse zur Repräsentation einer Alkhaltigendrinkform

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
                model : Alkoholhaltigedrinks
                    Alkoholhaltigedrinksobjekt
                fields : string
                    Felder der Alkoholhaltigendrinks
                widgets : dictionary
                    Die unsichtbaren Felder


        """
        model = AlkoholhaltigeDrinks
        fields = '__all__'
        widgets = {'kundeId': forms.HiddenInput()}


class TemplateForm(ModelForm):
    """
            Eine Klasse zur Repräsentation einer Templateform

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
                    Template-Feld


        """
        model = Kunde
        fields = ['template']


class ProfilForm(ModelForm):
    """
            Eine Klasse zur Repräsentation einer Profilform

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
                    Web- und Telefon-Feld


        """
        model = Kunde
        fields = ['web', 'telefon']


class CovidForm(ModelForm):
    """
            Eine Klasse zur Repräsentation einer Covidform

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
                model : Besucher
                    Besucherobjekt
                fields : string
                    Felder des Besuchers
                labels : dictionary
                    Umbenennung der Labels bei der Form
                widgets : dictionary
                    Die unsichtbaren Felder


        """
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
