from django.test import SimpleTestCase
from django.urls import reverse, resolve
from crm.views import dashboard, kundenliste

class TestUrls(SimpleTestCase):

    def test_crm_dashboard_url_is_resolved(self):
        url = reverse('crm_dashboard') # URL von crm_Dashboard bekommen
        print(resolve(url)) # Gibt Meta-Daten über die URL von crm_dashboard (z.B. Funktion, mit der crm_dashboard angezeigt wird
        self.assertEquals(resolve(url).func, dashboard) # Ist diese Funktion aus resolve() die gleiche wie die Funktion aus crm.views ?

    def test_kundenliste_is_resolved(self):
        url = reverse('kundenliste')
        print(resolve(url))
        self.assertEquals(resolve(url).func, kundenliste)