from django.db import models
from crm.models import Kunde
from phonenumber_field.modelfields import PhoneNumberField


# Create your models here.


class Vorspeise(models.Model):
    """
        Eine Klasse zur Repräsentation einer Vorspeise

        ...

        Attributes
        ----------
        name : charfield
            Name der Vorspeise
        beschreibung : textfield
            Beschreibung der Vorspeise
        zusatzstoffe : charfield
            Enthaltene Zusatzstoffe der Vorspeise
        preis : decimalfield
            Preis mit 2 Nachkommastellen
        kundeId : foreignkey
            Fremdschlüssel des Kunden

        Methods
        -------
        __str__():
            Gibt den Namen der Vorspeise aus
        """
    name = models.CharField(max_length=55, null=False, blank=False)
    beschreibung = models.TextField(blank=True, default='')
    zusatzstoffe = models.CharField(max_length=55, null=True, blank=True, default='')
    preis = models.DecimalField(max_length=8, max_digits=8, decimal_places=2, default='')
    kundeId = models.ForeignKey(Kunde, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return f'{self.name}'


class Hauptspeise(models.Model):
    """
        Eine Klasse zur Repräsentation einer Hauptspeise

        ...

        Attributes
        ----------
        name : charfield
            Name der Hauptspeise
        beschreibung : textfield
            Beschreibung der Hauptspeise
        zusatzstoffe : charfield
            Enthaltene Zusatzstoffe der Hauptspeise
        preis : decimalfield
            Preis mit 2 Nachkommastellen
        kundeId : foreignkey
            Fremdschlüssel des Kunden

        Methods
        -------
        __str__():
            Gibt den Namen der Hauptspeise aus
        """
    name = models.CharField(max_length=55, null=False, blank=False)
    beschreibung = models.TextField(blank=True, default='')
    zusatzstoffe = models.CharField(max_length=55, null=True, blank=True, default='')
    preis = models.DecimalField(max_length=8, max_digits=8, decimal_places=2, default='')
    kundeId = models.ForeignKey(Kunde, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return f'{self.name}'


class Nachspeise(models.Model):
    """
        Eine Klasse zur Repräsentation einer Nachspeise

        ...

        Attributes
        ----------
        name : charfield
            Name der Nachspeise
        beschreibung : textfield
            Beschreibung der Nachspeise
        zusatzstoffe : charfield
            Enthaltene Zusatzstoffe der Nachspeise
        preis : decimalfield
            Preis mit 2 Nachkommastellen
        kundeId : foreignkey
            Fremdschlüssel des Kunden

        Methods
        -------
        __str__():
            Gibt den Namen der Nachspeise aus
        """
    name = models.CharField(max_length=55, null=False, blank=False)
    beschreibung = models.TextField(blank=True, default='')
    zusatzstoffe = models.CharField(max_length=55, null=True, blank=True, default='')
    preis = models.DecimalField(max_length=8, max_digits=8, decimal_places=2, default="")
    kundeId = models.ForeignKey(Kunde, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return f'{self.name}'


class Snacks(models.Model):
    """
        Eine Klasse zur Repräsentation eines Snacks

        ...

        Attributes
        ----------
        name : charfield
            Name der Vorspeise
        beschreibung : textfield
            Beschreibung des Snacks
        zusatzstoffe : charfield
            Enthaltene Zusatzstoffe des Snacks
        preis : decimalfield
            Preis mit 2 Nachkommastellen
        kundeId : foreignkey
            Fremdschlüssel des Kunden

        Methods
        -------
        __str__():
            Gibt den Namen des Snacks aus
        """
    name = models.CharField(max_length=55, null=False, blank=False)
    beschreibung = models.TextField(blank=True, default='')
    zusatzstoffe = models.CharField(max_length=55, null=True, blank=True, default='')
    preis = models.DecimalField(max_length=8, max_digits=8, decimal_places=2, default="")
    kundeId = models.ForeignKey(Kunde, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return f'{self.name}'


class AlkoholfreieDrinks(models.Model):
    """
        Eine Klasse zur Repräsentation eines alkoholfreien Drinks

        ...

        Attributes
        ----------
        name : charfield
            Name des alkoholfreien Drinks
        liter : decimalfield
            Füllmenge mit 2 Nachkommastellen in liter
        beschreibung : textfield
            Beschreibung der Vorspeise
        zusatzstoffe : charfield
            Enthaltene Zusatzstoffe des alkoholfreien Drinks
        preis : decimalfield
            Preis mit 2 Nachkommastellen
        kundeId : foreignkey
            Fremdschlüssel des Kunden

        Methods
        -------
        __str__():
            Gibt den Namen des alkoholfreien Drinks aus
        """
    name = models.CharField(max_length=55, null=False, blank=False)
    liter = models.DecimalField(max_length=8, max_digits=8, decimal_places=2, default="")
    beschreibung = models.TextField(blank=True, default='')
    zusatzstoffe = models.CharField(max_length=55, null=True, blank=True, default='')
    preis = models.DecimalField(max_length=8, max_digits=8, decimal_places=2, default="")
    kundeId = models.ForeignKey(Kunde, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return f'{self.name}'


class AlkoholhaltigeDrinks(models.Model):
    """
        Eine Klasse zur Repräsentation eines alkoholfreien Drinks

        ...

        Attributes
        ----------
        name : charfield
            Name des alkoholfreien Drinks
        liter : decimalfield
            Füllmenge mit 2 Nachkommastellen in centiliter
        beschreibung : textfield
            Beschreibung des alkoholhaltigen Drinks
        zusatzstoffe : charfield
            Enthaltene Zusatzstoffe des alkoholhaltigen Drinks
        preis : decimalfield
            Preis mit 2 Nachkommastellen
        kundeId : foreignkey
            Fremdschlüssel des Kunden

        Methods
        -------
        __str__():
            Gibt den Namen des alkoholhaltigen Drinks aus
        """
    name = models.CharField(max_length=55, null=False, blank=False)
    centiliter = models.DecimalField(max_length=8, max_digits=8, decimal_places=2, default="")
    beschreibung = models.TextField(blank=True, default='')
    zusatzstoffe = models.CharField(max_length=55, null=True, blank=True, default="")
    preis = models.DecimalField(max_length=8, max_digits=8, decimal_places=2, default="")
    kundeId = models.ForeignKey(Kunde, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return f'{self.name}'


class Besucher(models.Model):
    """
        Eine Klasse zur Repräsentation eines Besuchers

        ...

        Attributes
        ----------
        vorname : charfield
            Vorname des Besuchers
        nachname : decimalfield
            Nachname des Besuchers
        email : emailfield
            Email-Adresse des Besuchers
        telefon : phonenumberfield
            Telefonnummer des Besuchers
        strasse : charfield
            Straße des Besuchers
        hausnummer : charfield
            Hausnummer des Besuchers
        plz : charfield
            PLZ des Besuchers
        stadt : charfield
            Ort des Besuchers
        besucht_am : datetimefield
            Datum der Erstellung des Besuchers
        kundeId : foreignkey
            Fremdschlüssel des Kunden

        Methods
        -------
        __str__():
            Gibt den Vor- und Nachnamen des Besuchers aus
        """
    vorname = models.CharField(max_length=45, null=False)
    nachname = models.CharField(max_length=45, null=False)
    email = models.EmailField(null=True, blank=True)
    telefon = PhoneNumberField(null=True, blank=True)
    strasse = models.CharField(max_length=45, null=False)
    hausnummer = models.CharField(max_length=5, null=False)
    plz = models.CharField(max_length=45, null=False)
    stadt = models.CharField(max_length=45, null=False)
    besucht_am = models.DateTimeField(auto_now_add=True, null=True)
    kundeId = models.ForeignKey(Kunde, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return f'{self.vorname} {self.nachname}'
