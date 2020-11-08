from django.test import SimpleTestCase
from django.urls import reverse, resolve
from crm.views import *

class TestUrls(SimpleTestCase):

    def test_crm_dashboard_url_is_resolved(self):
        url = reverse('crm_dashboard') # URL von crm_Dashboard bekommen
        #print(resolve(url)) # Gibt Meta-Daten über die URL von crm_dashboard (z.B. Funktion, mit der crm_dashboard angezeigt wird
        self.assertEquals(resolve(url).func, dashboard) # Ist diese Funktion aus resolve() die gleiche wie die Funktion aus crm.views ?

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

