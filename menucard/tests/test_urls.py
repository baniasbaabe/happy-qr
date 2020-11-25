from django.test import SimpleTestCase
from django.urls import reverse, resolve
from menucard.views import *

class TestUrls(SimpleTestCase):

    def test_vorspeisen_is_resolved(self):
        url = reverse('vorspeisen')
        self.assertEquals(resolve(url).func, vorspeisen)

    def test_vorspeisen_anlegen_is_resolved(self):
        url = reverse('vorspeisen_anlegen')
        self.assertEquals(resolve(url).func, vorspeisen_anlegen)

    def test_hauptspeisen_is_resolved(self):
        url = reverse('hauptspeisen')
        self.assertEquals(resolve(url).func, hauptspeisen)

    def test_hauptspeisen_anlegen_is_resolved(self):
        url = reverse('hauptspeisen_anlegen')
        self.assertEquals(resolve(url).func, hauptspeisen_anlegen)

    def test_nachspeisen_is_resolved(self):
        url = reverse('nachspeisen')
        self.assertEquals(resolve(url).func, nachspeisen)

    def test_nachspeisen_anlegen_is_resolved(self):
        url = reverse('nachspeisen_anlegen')
        self.assertEquals(resolve(url).func, nachspeisen_anlegen)
