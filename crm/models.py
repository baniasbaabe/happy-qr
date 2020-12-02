from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.auth.models import User


# Create your models here.

class Mitarbeiter(models.Model):
    vorname = models.CharField(max_length=45, null=False)
    nachname = models.CharField(max_length=45, null=False)
    email = models.EmailField()
    telefon = PhoneNumberField(null=True, blank=True)

    def __str__(self):
        return f'{self.vorname} {self.nachname}'


class Kunde(models.Model):
    TEMPLATE = [
        ('Template 1', 'Template 1'),
        ('Template 2', 'Template 2'),
        ('Template 3', 'Template 3')
    ]

    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
    vorname = models.CharField(max_length=45, null=False)
    nachname = models.CharField(max_length=45, null=False)
    email = models.EmailField(null=True, blank=True)
    telefon = PhoneNumberField(null=True, blank=True)
    web = models.CharField(max_length=200, null=True, blank=True)
    notiz = models.TextField(null=True, blank=True)
    template = models.CharField(max_length=20, choices=TEMPLATE, default='Template 1')

    def __str__(self):
        return f'{self.vorname} {self.nachname}'


class Auftrag(models.Model):
    PRODUKT = [
        ('Digital Menucard', 'Digital Menucard')
    ]

    STATUS = [
        ('Eingegangen', 'Eingegangen'),
        ('In Bearbeitung', 'In Bearbeitung'),
        ('Abgeschlossen', 'Abgeschlossen')
    ]

    kunde = models.ForeignKey(Kunde, null=True, on_delete=models.SET_NULL)
    produkt = models.CharField(max_length=45, choices=PRODUKT, default='Digital Menucard')
    status = models.CharField(max_length=45, choices=STATUS, default='Eingegangen')
    auftrag_vom = models.DateTimeField(auto_now_add=True, null=True)
    preis = models.FloatField(null=False, default=600.00)
    notiz = models.TextField(null=True, blank=True)

    def __str__(self):
        return f'Auftragsnummer: {self.id}, Kunde {self.kunde}'


class Rechnung(models.Model):
    kunde = models.ForeignKey(Kunde, null=True, on_delete=models.SET_NULL)
    auftrag = models.ForeignKey(Auftrag, null=True, on_delete=models.SET_NULL)
    datum = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'Rechnungsnummer: {self.id}, Kunde: {self.kunde}'
