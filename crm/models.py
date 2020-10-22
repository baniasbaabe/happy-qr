from django.db import models


# Create your models here.

class Mitarbeiter(models.Model):
    vorname = models.CharField(max_length=45, null=False)
    nachname = models.CharField(max_length=45, null=False)
    email = models.EmailField()

    def __str__(self):
        return f'{self.vorname} {self.nachname}'
