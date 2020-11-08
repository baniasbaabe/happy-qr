from django.test import TestCase, Client
from django.urls import reverse
from crm.models import *

class TestViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.kundenliste_url = reverse("kundenliste")
        self.dashboard_url = reverse("crm_dashboard")
        self.mitarbeiterliste_url = reverse("mitarbeiterliste")

    def test_kundenliste_GET(self):


        response = self.client.get(self.kundenliste_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, "crm/kundenliste.html")

    def test_dashboard_GET(self):

        response = self.client.get(self.dashboard_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, "crm/dashboard.html")

    def test_mitarbeiterliste_GET(self):

        response = self.client.get(self.mitarbeiterliste_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, "crm/mitarbeiterliste.html")


