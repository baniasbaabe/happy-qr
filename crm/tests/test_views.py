from django.test import TestCase, Client
from django.urls import reverse
from crm.models import *

class TestViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.list_url = reverse("kundenliste")
        self.dashboard_url = reverse("crm_dashboard")

    def test_kundenliste_GET(self):


        response = self.client.get(self.list_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, "crm/kundenliste.html")

    def test_dashboard_GET(self):

        response = self.client.get(self.dashboard_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, "crm/dashboard.html")

