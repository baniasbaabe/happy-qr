from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.auth.models import User


# Create your models here.

class Mitarbeiter(models.Model):
    """
        Eine Klasse zur Repräsentation eines Mitarbeiters

        ...

        Attributes
        ----------
        vorname : charfield
            Vorname des Mitarbeiters
        nachname : decimalfield
            Nachname des Mitarbeiters
        email : emailfield
            Email-Adresse des Mitarbeiters
        telefon : phonenumberfield
            Telefonnummer des Mitarbeiters

        Methods
        -------
        __str__():
            Gibt den Vor- und Nachnamen des Mitarbeiters aus
        """
    vorname = models.CharField(max_length=45, null=False)
    nachname = models.CharField(max_length=45, null=False)
    email = models.EmailField()
    telefon = PhoneNumberField(null=True, blank=True)

    def __str__(self):
        return f'{self.vorname} {self.nachname}'


class Kunde(models.Model):
    """
        Eine Klasse zur Repräsentation eines Besuchers

        ...

        Attributes
        ----------
        user : user
            Django-User des Kunden
        vorname : charfield
            Vorname des Kunden
        nachname : decimalfield
            Nachname des Kunden
        email : emailfield
            Email-Adresse des Kunden
        telefon : phonenumberfield
            Telefonnummer des Kunden
        web : charfield
            Website des Kunden
        notiz : textfield
            Notizen für den Kunden
        template : charfield
            Ausgewähltes Template des Kunden

        Methods
        -------
        __str__():
            Gibt den Vor- und Nachnamen des Kunden aus
        """
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
    """
        Eine Klasse zur Repräsentation eines Auftrags

        ...

        Attributes
        ----------
        kunde : foreignkey
            Fremdschlüssel des Kunden
        produkt : charfield
            Enthaltenes Produkt des Auftrags
        status : charfield
            Status des Auftrags
        auftrag_vom : datetimefield
            Datum der Erstellung des Auftrags
        telefon : phonenumberfield
            Telefonnummer des Kunden
        preis : decimalfield
            Preis des Auftrags
        notiz : textfield
            Notizen für den Auftrag

        Methods
        -------
        __str__():
            Gibt die Auftragsnummer und den Namen des Kunden aus
        """
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
    preis = models.DecimalField(max_length=8, max_digits=8, decimal_places=2, default='')
    notiz = models.TextField(null=True, blank=True)

    def __str__(self):
        return f'Auftragsnummer: {self.id}, Kunde {self.kunde}'


class Rechnung(models.Model):
    """
        Eine Klasse zur Repräsentation eines Auftrags

        ...

        Attributes
        ----------
        kunde : foreignkey
            Fremdschlüssel des Kunden
        auftrag : foreignkey
            Fremdschlüssel des Auftrags
        datum : datefield
            Datum der Erstellung der Rechnung

        Methods
        -------
        __str__():
            Gibt die Rechnungsnummer und den Vor- und Nachnamen des Kunden aus
        """
    kunde = models.ForeignKey(Kunde, null=True, on_delete=models.SET_NULL)
    auftrag = models.ForeignKey(Auftrag, null=True, on_delete=models.SET_NULL)
    datum = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'Rechnungsnummer: {self.id}, Kunde: {self.kunde}'
