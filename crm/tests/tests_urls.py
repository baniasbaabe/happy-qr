from django.test import TestCase, Client
from django.urls import reverse, resolve
from crm.views import *
from django.contrib.auth.models import User, Permission, Group


class TestUrls(TestCase):
    def setUp(self):
        self.user = User.objects.create_superuser(username="user1", email="user1@example.de", password="Hallo12345")
        self.client = Client()

        group_name = "mitarbeiter"
        self.group = Group(name=group_name)
        self.group.save()

    def test_crm_dashboard_url_is_resolved(self):
        url = reverse('crm_dashboard')  # URL von crm_Dashboard bekommen
        self.assertEquals(resolve(url).func,
                          dashboard)  # Ist diese Funktion aus resolve() die gleiche wie die Funktion aus crm.views ?

    def test_kundenliste_is_resolved(self):
        url = reverse('kundenliste')
        self.assertEquals(resolve(url).func, kundenliste)

    def test_kunde_anlegen_is_resolved(self):
        url = reverse('kunde_anlegen')
        self.assertEquals(resolve(url).func, KundeAnlegen)

    def test_mitarbeiterliste_is_resolved(self):
        url = reverse("mitarbeiterliste")
        self.assertEquals(resolve(url).func, mitarbeiterliste)

    def test_mitarbeiter_anlegen_is_resolved(self):
        url = reverse("mitarbeiter_anlegen")
        self.assertEquals(resolve(url).func, mitarbeiterAnlegen)

    def test_auftrag_anlegen_is_resolved(self):
        url = reverse("auftrag_anlegen")
        self.assertEquals(resolve(url).func, auftragAnlegen)

    def test_rechnung_anlegen_is_resolved(self):
        url = reverse("rechnung_anlegen")
        self.assertEquals(resolve(url).func, rechnungAnlegen)

    def test_rechnungsliste_is_resolved(self):
        url = reverse("rechnungsliste")
        self.assertEquals(resolve(url).func, rechnungsliste)

    def test_auftragsliste_is_resolved(self):
        url = reverse("auftragsliste")
        self.assertEquals(resolve(url).func, auftragsliste)
