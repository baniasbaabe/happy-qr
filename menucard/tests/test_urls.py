from django.test import TestCase, Client
from django.urls import reverse, resolve
from menucard.views import *
from django.contrib.auth.models import User, Permission,Group


class TestUrls(TestCase):
    def setUp(self):

        self.user = User.objects.create_superuser(username="user1",email="user1@example.de",password="Hallo12345")
        self.client = Client()

        group_name = "mitarbeiter"
        self.group = Group(name=group_name)
        self.group.save()


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
