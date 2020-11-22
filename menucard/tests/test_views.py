from django.test import TestCase, Client
from django.urls import reverse
from menucard.models import *

class TestViews(TestCase):

    def setUp(self):
        self.client = Client()

        self.vorspeise1 = Vorspeise.objects.create(
            name = "Testname",
            beschreibung="Testbeschreibung",
            preis=1
        )

        self.hauptspeise1 = Hauptspeise.objects.create(
            name="Testname",
            beschreibung="Testbeschreibung",
            preis=1
        )

        self.nachspeise1 = Nachspeise.objects.create(
            name="Testname",
            beschreibung="Testbeschreibung",
            preis=1
        )

        self.snacks1 = Snacks.objects.create(
            name="Testname",
            beschreibung="Testbeschreibung",
            preis=1
        )

        self.alkoholfreiedrinks1 = AlkoholfreieDrinks.objects.create(
            name="Testname",
            beschreibung="Testbeschreibung",
            liter=1,
            preis=1
        )

        self.alkoholhaltigedrinks1 = AlkoholhaltigeDrinks.objects.create(
            name="Testname",
            beschreibung="Testbeschreibung",
            centiliter=1,
            preis=1
        )

    def test_CREATE_vorspeise(self):
        post_response = self.client.post(reverse("vorspeisen_anlegen"), {
            "name":"Vorspeisename",
            "beschreibung":"Createbeschreibung",
            "preis":1
        })
        self.assertEquals(post_response.status_code, 302)
        self.assertEqual(Vorspeise.objects.last().name, "Vorspeisename")
        self.assertEquals(Vorspeise.objects.count(), 2)

    def test_CREATE_hauptspeise(self):
        post_response = self.client.post(reverse("hauptspeisen_anlegen"), {
            "name":"Hauptspeisename",
            "beschreibung":"Createbeschreibung",
            "preis":1
        })
        self.assertEquals(post_response.status_code, 302)
        self.assertEqual(Hauptspeise.objects.last().name, "Hauptspeisename")
        self.assertEquals(Hauptspeise.objects.count(), 2)

    def test_CREATE_nachspeise(self):
        post_response = self.client.post(reverse("nachspeisen_anlegen"), {
            "name":"Nachspeisename",
            "beschreibung":"Createbeschreibung",
            "preis":1
        })
        self.assertEquals(post_response.status_code, 302)
        self.assertEqual(Nachspeise.objects.last().name, "Nachspeisename")
        self.assertEquals(Nachspeise.objects.count(), 2)

    def test_CREATE_snacks(self):
        post_response = self.client.post(reverse("snacks_anlegen"), {
            "name":"Snackname",
            "beschreibung":"Createbeschreibung",
            "preis":1
        })
        self.assertEquals(post_response.status_code, 302)
        self.assertEqual(Snacks.objects.last().name, "Snackname")
        self.assertEquals(Snacks.objects.count(), 2)

    def test_CREATE_alkfreiedrinks(self):
        post_response = self.client.post(reverse("alkfreiedrinks_anlegen"), {
            "name":"Alkfreiedrinksname",
            "beschreibung":"Createbeschreibung",
            "liter":1,
            "preis":1
        })
        self.assertEquals(post_response.status_code, 302)
        self.assertEqual(AlkoholfreieDrinks.objects.last().name, "Alkfreiedrinksname")
        self.assertEquals(AlkoholfreieDrinks.objects.count(), 2)

    def test_CREATE_alkhaltigedrinks(self):
        post_response = self.client.post(reverse("alkoholhaltigedrinks_anlegen"), {
            "name": "Alkhaltigedrinksname",
            "beschreibung": "Createbeschreibung",
            "centiliter": 1,
            "preis": 1
        })
        self.assertEquals(post_response.status_code, 302)
        self.assertEqual(AlkoholhaltigeDrinks.objects.last().name, "Alkhaltigedrinksname")
        self.assertEquals(AlkoholhaltigeDrinks.objects.count(), 2)


    def test_DELETE_vorspeise(self):

        vorspeise = self.vorspeise1

        post_response = self.client.post(reverse('vorspeisen_loeschen', kwargs={"pk":vorspeise.id}))
        self.assertEquals(post_response.status_code, 302)
        self.assertEquals(Vorspeise.objects.count(),0)

    def test_DELETE_hauptspeise(self):
        hauptspeise = self.hauptspeise1

        post_response = self.client.post(reverse('hauptspeise_loeschen', kwargs={"pk": hauptspeise.id}))
        self.assertEquals(post_response.status_code, 302)
        self.assertEquals(Hauptspeise.objects.count(), 0)

    def test_DELETE_nachspeise(self):
        nachspeise = self.nachspeise1

        post_response = self.client.post(reverse('nachspeisen_loeschen', kwargs={"pk": nachspeise.id}))
        self.assertEquals(post_response.status_code, 302)
        self.assertEquals(Nachspeise.objects.count(), 0)

    def test_DELETE_snacks(self):
        snacks = self.snacks1

        post_response = self.client.post(reverse('snacks_loeschen', kwargs={"pk": snacks.id}))
        self.assertEquals(post_response.status_code, 302)
        self.assertEquals(Snacks.objects.count(), 0)

    def test_DELETE_alkfreiedrinks(self):
        alkfreiedrinks = self.alkoholfreiedrinks1

        post_response = self.client.post(reverse('alkfreiedrinks_loeschen', kwargs={"pk": alkfreiedrinks.id}))
        self.assertEquals(post_response.status_code, 302)
        self.assertEquals(AlkoholfreieDrinks.objects.count(), 0)

    def test_DELETE_alkhaltigedrinks(self):
        alkhaltigedrinks = self.alkoholhaltigedrinks1

        post_response = self.client.post(reverse('alkoholhaltigedrinks_loeschen', kwargs={"pk": alkhaltigedrinks.id}))
        self.assertEquals(post_response.status_code, 302)
        self.assertEquals(AlkoholhaltigeDrinks.objects.count(), 0)




