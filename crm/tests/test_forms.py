from django.test import SimpleTestCase
from crm.forms import *

class TestForms(SimpleTestCase):

    def test_kunde_form_valid_data(self):
        form = KundeForm(data={
            'vorname':'VornameKunde',
            'nachname':'NachnameKunde',
            'email':'email@mail.com',
            'telefon':'+4917666666666',
            'web':'kunde.kunde.de',
            'notiz':'Notizen'})

        self.assertTrue(form.is_valid())

    def test_kunde_form_invalid_data(self):
        form = KundeForm(data={
           })

        self.assertFalse(form.is_valid())

    def test_mitarbeiter_form_valid_data(self):
        form = MitarbeiterForm(data={
            'vorname':'VornameMA',
            'nachname':'NachnameMA',
            'email':'email@mail.com',
            'telefon':'+4917666666666'
            })

        self.assertTrue(form.is_valid())

    def test_mitarbeiter_form_invalid_data(self):
        form = KundeForm(data={
            })

        self.assertFalse(form.is_valid())
