from django.db import models
from crm.models import Kunde

# Create your models here.

class Vorspeise(models.Model):
    name = models.CharField(max_length=55, null=False, blank=False)
    beschreibung = models.TextField(blank=True, default='')
    preis = models.FloatField(blank=False)
    kundeId = models.ForeignKey(Kunde,null=True,on_delete=models.SET_NULL)

    def __str__(self):
        return f'{self.name}'


class Hauptspeise(models.Model):
    name = models.CharField(max_length=55, null=False, blank=False)
    beschreibung = models.TextField(blank=True, default='')
    preis = models.FloatField(blank=False)
    kundeId = models.ForeignKey(Kunde,null=True,on_delete=models.SET_NULL)

    def __str__(self):
        return f'{self.name}'


class Nachspeise(models.Model):
    name = models.CharField(max_length=55, null=False, blank=False)
    beschreibung = models.TextField(blank=True, default='')
    preis = models.FloatField(blank=False)
    kundeId = models.ForeignKey(Kunde,null=True,on_delete=models.SET_NULL)

    def __str__(self):
        return f'{self.name}'


class Snacks(models.Model):
    name = models.CharField(max_length=55, null=False, blank=False)
    beschreibung = models.TextField(blank=True, default='')
    preis = models.FloatField(blank=False)
    kundeId = models.ForeignKey(Kunde,null=True,on_delete=models.SET_NULL)

    def __str__(self):
        return f'{self.name}'


class AlkoholfreieDrinks(models.Model):
    name = models.CharField(max_length=55, null=False, blank=False)
    liter = models.FloatField()
    beschreibung = models.TextField(blank=True, default='')
    preis = models.FloatField(blank=False)
    kundeId = models.ForeignKey(Kunde,null=True,on_delete=models.SET_NULL)

    def __str__(self):
        return f'{self.name}'


class AlkoholhaltigeDrinks(models.Model):
    name = models.CharField(max_length=55, null=False, blank=False)
    centiliter = models.FloatField()
    beschreibung = models.TextField(blank=True, default='')
    preis = models.FloatField(blank=False)
    kundeId = models.ForeignKey(Kunde,null=True,on_delete=models.SET_NULL)

    def __str__(self):
        return f'{self.name}'

