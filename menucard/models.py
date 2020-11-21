from django.db import models


# Create your models here.

class Vorspeise(models.Model):
    name = models.CharField(max_length=55, null=False, blank=False)
    beschreibung = models.TextField(blank=True, default='')
    preis = models.FloatField(blank=False)

    def __str__(self):
        return f'{self.name}'


class Hauptspeise(models.Model):
    name = models.CharField(max_length=55, null=False, blank=False)
    beschreibung = models.TextField(blank=True, default='')
    preis = models.FloatField(blank=False)

    def __str__(self):
        return f'{self.name}'


class Nachspeise(models.Model):
    name = models.CharField(max_length=55, null=False, blank=False)
    beschreibung = models.TextField(blank=True, default='')
    preis = models.FloatField(blank=False)

    def __str__(self):
        return f'{self.name}'


class Snacks(models.Model):
    name = models.CharField(max_length=55, null=False, blank=False)
    beschreibung = models.TextField(blank=True, default='')
    preis = models.FloatField(blank=False)

    def __str__(self):
        return f'{self.name}'


class AlkoholfreieDrinks(models.Model):
    name = models.CharField(max_length=55, null=False, blank=False)
    liter = models.FloatField()
    beschreibung = models.TextField(blank=True, default='')
    preis = models.FloatField(blank=False)

    def __str__(self):
        return f'{self.name}'


class AlkoholhaltigeDrinks(models.Model):
    name = models.CharField(max_length=55, null=False, blank=False)
    centiliter = models.FloatField()
    beschreibung = models.TextField(blank=True, default='')
    preis = models.FloatField(blank=False)

    def __str__(self):
        return f'{self.name}'


class Template(models.Model):
    TEMPLATE = [
        ('Standard', 'Standard'),
        ('Deluxe', 'Deluxe'),
        ('Modern', 'Modern')
    ]
    template = models.CharField(choices=TEMPLATE, default='Standard', max_length=20, blank=False, null=False)

    def __str__(self):
        return self.template