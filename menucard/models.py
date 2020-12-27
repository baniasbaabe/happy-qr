from django.db import models
from crm.models import Kunde
from phonenumber_field.modelfields import PhoneNumberField


# Create your models here.


class Vorspeise(models.Model):
    name = models.CharField(max_length=55, null=False, blank=False)
    beschreibung = models.TextField(blank=True, default='')
    preis = models.DecimalField(max_length=8, max_digits=8, decimal_places=2, default=600.00)
    kundeId = models.ForeignKey(Kunde, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return f'{self.name}'


class Hauptspeise(models.Model):
    name = models.CharField(max_length=55, null=False, blank=False)
    beschreibung = models.TextField(blank=True, default='')
    preis = models.DecimalField(max_length=8, max_digits=8, decimal_places=2, default=600.00)
    kundeId = models.ForeignKey(Kunde, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return f'{self.name}'


class Nachspeise(models.Model):
    name = models.CharField(max_length=55, null=False, blank=False)
    beschreibung = models.TextField(blank=True, default='')
    preis = models.DecimalField(max_length=8, max_digits=8, decimal_places=2, default=600.00)
    kundeId = models.ForeignKey(Kunde, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return f'{self.name}'


class Snacks(models.Model):
    name = models.CharField(max_length=55, null=False, blank=False)
    beschreibung = models.TextField(blank=True, default='')
    preis = models.DecimalField(max_length=8, max_digits=8, decimal_places=2, default=600.00)
    kundeId = models.ForeignKey(Kunde, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return f'{self.name}'


class AlkoholfreieDrinks(models.Model):
    name = models.CharField(max_length=55, null=False, blank=False)
    liter = models.FloatField()
    beschreibung = models.TextField(blank=True, default='')
    preis = models.DecimalField(max_length=8, max_digits=8, decimal_places=2, default=600.00)
    kundeId = models.ForeignKey(Kunde, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return f'{self.name}'


class AlkoholhaltigeDrinks(models.Model):
    name = models.CharField(max_length=55, null=False, blank=False)
    centiliter = models.FloatField()
    beschreibung = models.TextField(blank=True, default='')
    preis = models.DecimalField(max_length=8, max_digits=8, decimal_places=2, default=600.00)
    kundeId = models.ForeignKey(Kunde, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return f'{self.name}'


class Besucher(models.Model):
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
