from django.test import TestCase
from crm.forms import *
from django.contrib.auth.models import User, Permission,Group
from django.test import TestCase, Client

class TestForms(TestCase):
    def setUp(self):

        self.user = User.objects.create_superuser(username="user1",email="user1@example.de",password="Hallo12345")
        self.client = Client()

        group_name = "mitarbeiter"
        self.group = Group(name=group_name)
        self.group.save()


    def test_kunde_form_valid_data(self):
        self.user.groups.add(self.group)
        self.user.save()
        self.client.login(username="user1", password="Hallo12345")
        form = KundeForm(data={
            'vorname':'VornameKunde',
            'nachname':'NachnameKunde',
            'email':'email@mail.com',
            'telefon':'+4917666666666',
            'web':'kunde.kunde.de',
            'notiz':'Notizen',
            'template':'Template 1'})

        self.assertTrue(form.is_valid())


    def test_kunde_form_invalid_data(self):
        self.user.groups.add(self.group)
        self.user.save()
        self.client.login(username="user1", password="Hallo12345")
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
