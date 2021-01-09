from django.urls import reverse
from menucard.models import *
from django.contrib.auth.models import User, Group
from django.test import TestCase, Client



class TestViews(TestCase):

    def setUp(self):
        self.user = User.objects.create_superuser(username="user1", email="user1@example.de", password="Hallo12345")
        self.client = Client()

        group_name = "kunde"
        self.group = Group(name=group_name)
        self.group.save()

        self.user.groups.add(self.group)
        self.user.save()
        self.client.login(username="user1", password="Hallo12345")

        self.kunde = Kunde.objects.create(vorname="Kundevor", nachname="Kundenach", email=self.user.email,
                                          telefon="+4917666994073",
                                          notiz="hi", web="hi.de", template="Template 1")

        self.dashboard_url = reverse("menucard_dashboard")
        self.vorspeisen_url = reverse("vorspeisen")
        self.hauptspeisen_url = reverse("hauptspeisen")
        self.nachspeisen_url = reverse("nachspeisen")
        self.alkfreiedrinks_url = reverse("alkfreiedrinks")
        self.alkhaltigedrinks_url = reverse("alkoholhaltigedrinks")
        self.snacks_url = reverse("snacks")
        self.besucher_url = reverse("besucherdaten")

        self.vorspeisen_anlegen_url = reverse("vorspeisen_anlegen")
        self.nachspeisen_anlegen_url = reverse("nachspeisen_anlegen")
        self.snacks_anlegen_url = reverse("snacks_anlegen")
        self.alkfreiedrinks_anlegen_url = reverse("alkfreiedrinks_anlegen")
        self.alkhaltigedrinks_anlegen_url = reverse("alkoholhaltigedrinks_anlegen")
        self.hauptspeise_anlegen_url = reverse("hauptspeisen_anlegen")


        self.vorspeise1 = Vorspeise.objects.create(
            name = "Initialname",
            beschreibung="test",
            zusatzstoffe="1",
            preis=1.0,
            kundeId=self.kunde
        )

        self.hauptspeise1 = Hauptspeise.objects.create(
            name="Initialname",
            beschreibung="test",
            zusatzstoffe="1",
            preis=1.0,
            kundeId=self.kunde
        )

        self.nachspeise1 = Nachspeise.objects.create(
            name="Initialname",
            beschreibung="test",
            zusatzstoffe="1",
            preis=1.0,
            kundeId=self.kunde
        )

        self.snack1 = Snacks.objects.create(
            name="Initialname",
            beschreibung="test",
            zusatzstoffe="1",
            preis=1.0,
            kundeId=self.kunde
        )

        self.alkhaltigesdrink1 = AlkoholhaltigeDrinks.objects.create(
            name="Initialname",
            centiliter=1.0,
            zusatzstoffe="1",
            beschreibung="test",
            preis=1.0,
            kundeId=self.kunde
        )

        self.alkfreiesdrink1 = AlkoholfreieDrinks.objects.create(
            name="Initialname",
            liter=1.0,
            zusatzstoffe="1",
            beschreibung="test",
            preis=1.0,
            kundeId=self.kunde
        )

        self.besucher1 = Besucher.objects.create(
            vorname="Test",
            nachname="test",
            email="test@test.de",
            telefon="017666228621",
            strasse="Test",
            hausnummer=1,
            plz=12345,
            stadt="test",
            kundeId=self.kunde
        )


    def test_dashboard_GET(self):

        response = self.client.get(self.dashboard_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, "menucard/dashboard.html")

    def test_vorspeisen_GET(self):

        response = self.client.get(self.vorspeisen_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, "menucard/vorspeisen.html")

    def test_hauptspeisen_GET(self):

        response = self.client.get(self.hauptspeisen_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, "menucard/hauptspeisen.html")

    def test_nachspeisen_GET(self):

        response = self.client.get(self.nachspeisen_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, "menucard/nachspeisen.html")

    def test_alkfreiedrinks_GET(self):

        response = self.client.get(self.alkfreiedrinks_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, "menucard/alkfreiedrinks.html")

    def test_alkhaltigedrinks_GET(self):

        response = self.client.get(self.alkhaltigedrinks_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, "menucard/alkoholhaltigedrinks.html")

    def test_snacks_GET(self):

        response = self.client.get(self.snacks_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, "menucard/snacks.html")

    def test_besucher_GET(self):

        response = self.client.get(self.besucher_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, "menucard/besucher_daten.html")

    def test_CREATE_vorspeise(self):

        post_response = self.client.post(self.vorspeisen_anlegen_url, {
            "name": "Vorspeisename",
            "beschreibung": "Createbeschreibung",
            "preis": 1,
            "kundeId": self.kunde.id
        })
        self.assertEquals(post_response.status_code, 302)
        self.assertEqual(Vorspeise.objects.last().name, "Vorspeisename")


    def test_CREATE_hauptspeise(self):

        post_response = self.client.post(self.hauptspeise_anlegen_url, {
            "name": "Hauptspeisename",
            "beschreibung": "Createbeschreibung",
            "preis": 1,
            "kundeId": self.kunde.id
        })
        self.assertEquals(post_response.status_code, 302)
        self.assertEqual(Hauptspeise.objects.last().name, "Hauptspeisename")


    def test_CREATE_nachspeise(self):
        post_response = self.client.post(self.nachspeisen_anlegen_url, {
            "name":"Nachspeisename",
            "beschreibung":"Createbeschreibung",
            "Zusatzstoffe":"1",
            "preis":1.0,
            "kundeId": self.kunde.id
        })
        self.assertEquals(post_response.status_code, 302)
        self.assertEqual(Nachspeise.objects.last().name, "Nachspeisename")

    

    def test_CREATE_snacks(self):
        post_response = self.client.post(self.snacks_anlegen_url, {
            "name":"Snackname",
            "beschreibung":"Createbeschreibung",
            "Zusatzstoffe":"1",
            "preis":1.0,
            "kundeId": self.kunde.id
        })
        self.assertEquals(post_response.status_code, 302)
        self.assertEqual(Snacks.objects.last().name, "Snackname")

    def test_CREATE_alkfreiedrinks(self):
        post_response = self.client.post(self.alkfreiedrinks_anlegen_url, {
            "name": "Alkfreiedrinksname",
            "beschreibung": "Createbeschreibung",
            "liter":1.0,
            "Zusatzstoffe": "1",
            "preis": 1.0,
            "kundeId": self.kunde.id
        })
        self.assertEquals(post_response.status_code, 302)
        self.assertEqual(AlkoholfreieDrinks.objects.last().name, "Alkfreiedrinksname")


    def test_CREATE_alkhaltigedrinks(self):
        post_response = self.client.post(self.alkhaltigedrinks_anlegen_url, {
            "name": "Alkhaltigedrinksname",
            "beschreibung": "Createbeschreibung",
            "centiliter":1.0,
            "Zusatzstoffe": "1",
            "preis": 1.0,
            "kundeId": self.kunde.id
        })
        self.assertEquals(post_response.status_code, 302)
        self.assertEqual(AlkoholhaltigeDrinks.objects.last().name, "Alkhaltigedrinksname")

    def test_DELETE_vorspeise(self):

        count_bevor = Vorspeise.objects.count() - 1
        post_response = self.client.post(reverse('vorspeisen_loeschen', kwargs={"pk":self.vorspeise1.id}))
        self.assertEquals(post_response.status_code, 302)
        self.assertEquals(Vorspeise.objects.count(),count_bevor)

    def test_DELETE_besucher(self):

        count_bevor = Besucher.objects.count() - 1
        post_response = self.client.post(reverse('besucher_loeschen', kwargs={"pk": self.besucher1.id}))
        self.assertEquals(post_response.status_code, 302)
        self.assertEquals(Besucher.objects.count(), count_bevor)


    def test_DELETE_hauptspeise(self):

        count_bevor = Hauptspeise.objects.count() - 1
        post_response = self.client.post(reverse('hauptspeise_loeschen', kwargs={"pk": self.hauptspeise1.id}))
        self.assertEquals(post_response.status_code, 302)
        self.assertEquals(Hauptspeise.objects.count(), count_bevor)

    def test_DELETE_nachspeise(self):

        count_bevor = Nachspeise.objects.count() - 1
        post_response = self.client.post(reverse('nachspeisen_loeschen', kwargs={"pk": self.nachspeise1.id}))
        self.assertEquals(post_response.status_code, 302)
        self.assertEquals(Nachspeise.objects.count(), count_bevor)

    def test_DELETE_snacks(self):

        count_bevor = Snacks.objects.count() - 1
        post_response = self.client.post(reverse('snacks_loeschen', kwargs={"pk": self.snack1.id}))
        self.assertEquals(post_response.status_code, 302)
        self.assertEquals(Snacks.objects.count(), count_bevor)

    def test_DELETE_alkfreiedrinks(self):

        count_bevor = AlkoholfreieDrinks.objects.count() - 1
        post_response = self.client.post(reverse('alkfreiedrinks_loeschen', kwargs={"pk": self.alkfreiesdrink1.id}))
        self.assertEquals(post_response.status_code, 302)
        self.assertEquals(AlkoholfreieDrinks.objects.count(), count_bevor)

    def test_DELETE_alkhaltigedrinks(self):

        count_bevor = AlkoholhaltigeDrinks.objects.count() - 1
        post_response = self.client.post(reverse('alkoholhaltigedrinks_loeschen', kwargs={"pk": self.alkhaltigesdrink1.id}))
        self.assertEquals(post_response.status_code, 302)
        self.assertEquals(AlkoholhaltigeDrinks.objects.count(), count_bevor)

    def test_DELETE_alkhaltigedrinks(self):

        count_bevor = Besucher.objects.count() - 1
        post_response = self.client.post(reverse('besucher_loeschen', kwargs={"pk": self.besucher1.id}))
        self.assertEquals(post_response.status_code, 302)
        self.assertEquals(Besucher.objects.count(), count_bevor)

    def test_DOWNLOAD_QR(self):

        response = self.client.get(reverse('test_qr'))
        self.assertEquals(response.get('Content-Disposition'), 'attachment; filename="QRCode.pdf"')

    def test_DOWNLOAD_Besucherdaten_PDF(self):

        response = self.client.get(reverse('besucherliste_pdf_download'))
        filename = "Besucherliste.pdf"
        self.assertEquals(response.get('Content-Disposition'), "attachment; filename='%s'" % (filename))

    def test_DOWNLOAD_Besucherdaten_CSV(self):

        response = self.client.get(reverse('besucherliste_csv_download'))
        filename = "Besucherliste.csv"
        self.assertEquals(response.get('Content-Disposition'), "attachment; filename='%s'" % (filename))

