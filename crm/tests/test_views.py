from django.test import TestCase, Client
from django.urls import reverse
from crm.models import *
from django.contrib.auth.models import User, Permission,Group

class TestViews(TestCase):

    def setUp(self):

        '''
        self.user = User.objects.create_superuser(username="user1",email="user1@example.de",password="Hallo12345")
        self.client = Client()

        group_name = "mitarbeiter"
        self.group = Group(name=group_name)
        self.group.save()


        self.kundenliste_url = reverse("kundenliste")


        self.dashboard_url = reverse("crm_dashboard")
        self.mitarbeiterliste_url = reverse("mitarbeiterliste")
        self.auftragsliste_url = reverse("auftragsliste")
        self.rechnungsliste_url = reverse("rechnungsliste")
        self.mitarbeiteranlegen_url = reverse("mitarbeiter_anlegen")
        self.auftraganlegen_url = reverse("auftrag_anlegen")
        self.rechnunganlegen_url = reverse("rechnung_anlegen")


        self.kunde1 = Kunde.objects.create(
            vorname="TestVorname",
            nachname="Testnachname",
            email="kunde@kunde.de",
            telefon="+4912345678910",
            web="kunde.de",
            notiz="Beispielnotiz"
        )
        self.mitarbeiter1 = Mitarbeiter.objects.create(
            vorname="Testvorname",
            nachname="Testnachname",
            email="test@gmail.com",
            telefon="+4912345678910"
        )

        self.auftrag1 = Auftrag.objects.create(
            kunde=self.kunde1,
            produkt='Digital Menucard',
            status='Eingegangen',
            preis=600.00,
            notiz="Notizentest"
        )

        self.rechnung1 = Rechnung.objects.create(
            kunde=self.kunde1,
            auftrag=self.auftrag1
        )


    def test_kundenliste_GET(self):
        self.user.groups.add(self.group)
        self.user.save()
        self.client.login(username="user1", password="Hallo12345")

        response = self.client.get(self.kundenliste_url, follow=True)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, template_name="crm/kundenliste.html")


    def test_dashboard_GET(self):
        response = self.client.get(self.dashboard_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, "crm/dashboard.html")

    def test_mitarbeiterliste_GET(self):
        response = self.client.get(self.mitarbeiterliste_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, "crm/mitarbeiterliste.html")

    def test_auftragsliste_GET(self):
        response = self.client.get(self.auftragsliste_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, "crm/auftragsliste.html")
        
        

    def test_auftraganlegen_GET(self):
        response = self.client.get(self.auftraganlegen_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, "crm/auftrag_form.html")

    def test_rechnunganlegen_GET(self):
        response = self.client.get(self.rechnunganlegen_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, "crm/rechnung_form.html")

    def test_mitarbeiteranlegen_GET(self):
        response = self.client.get(self.mitarbeiteranlegen_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, "crm/mitarbeiter_form.html")
        
    

    def test_CREATE_mitarbeiter(self):
        Mitarbeiter.objects.all().delete()
        post_response = self.client.post(reverse("mitarbeiter_anlegen"), {
            "vorname": "Hallo",
            "nachname": "Hi",
            "telefon": "+4917611111111",
            "email": "ma@ma.de"
        })
        self.assertEquals(post_response.status_code, 302)
        self.assertEqual(Mitarbeiter.objects.last().vorname, "Hallo")
        self.assertEquals(Mitarbeiter.objects.count(), 1)

    def test_CREATE_kunde(self):
        Kunde.objects.all().delete()
        post_response = self.client.post(reverse("kunde_anlegen"), {
            "vorname": "Hallo",
            "nachname": "Hi",
            "telefon": "+4917611111111",
            "email": "ma@ma.de",
            "web": "kunde.de",
            "notiz": "Beispiel"
        })
        self.assertEquals(post_response.status_code, 302)
        self.assertEqual(Kunde.objects.last().vorname, "Hallo")
        self.assertEquals(Kunde.objects.count(), 1)

    
    def test_UPDATE_auftrag(self):

        response = self.client.post(
            reverse('auftrag_aktualisieren', kwargs={'pk':self.auftrag1.id}),
            {'kunde': self.kunde1, 'produkt': 'Digital Menucard', 'status':'Eingegangen', 'auftrag_vom':self.auftrag1.auftrag_vom,
             'preis':100.00 ,'notiz':'Beispielnotiz1'})

        self.assertEqual(response.status_code, 302)

        self.auftrag1.refresh_from_db()
        self.assertEqual(self.auftrag1.notiz, 'Beispielnotiz1')
    

    def test_UPDATE_kunde(self):
        response = self.client.post(
            reverse('kunde_aktualisieren', kwargs={'pk': self.kunde1.id}),
            {'vorname': 'Update', 'nachname': 'Mustermann', 'telefon': "+4917611111111",
             "email": "hallo@test.de", "web": "test.de", "notiz": "Beispielnotiz"})

        self.assertEqual(response.status_code, 302)

        self.kunde1.refresh_from_db()
        self.assertEqual(self.kunde1.vorname, 'Update')

    def test_UPDATE_mitarbeiter(self):
        response = self.client.post(
            reverse('mitarbeiter_aktualisieren', kwargs={'pk': self.mitarbeiter1.id}),
            {'vorname': 'Update', 'nachname': 'Mustermann', 'telefon': "+4917611111111",
             "email": "hallo@test.de"})

        self.assertEqual(response.status_code, 302)

        self.mitarbeiter1.refresh_from_db()
        self.assertEqual(self.mitarbeiter1.vorname, 'Update')

    def test_DELETE_mitarbeiter(self):
        mitarbeiter = self.mitarbeiter1

        post_response = self.client.post(reverse('mitarbeiter_loeschen', kwargs={"pk": mitarbeiter.id}))
        self.assertEquals(post_response.status_code, 302)
        self.assertEquals(Mitarbeiter.objects.count(), 0)

    def test_DELETE_kunde(self):
        kunde = self.kunde1

        post_response = self.client.post(reverse('kunde_loeschen', kwargs={"pk": kunde.id}))
        self.assertEquals(post_response.status_code, 302)
        self.assertEquals(Kunde.objects.count(), 0)

    def test_DELETE_auftrag(self):
        auftrag = self.auftrag1

        post_response = self.client.post(reverse('auftrag_loeschen', kwargs={"pk": auftrag.id}))
        self.assertEquals(post_response.status_code, 302)
        self.assertEquals(Auftrag.objects.count(), 0)

    def test_DELETE_rechnung(self):
        rechnung = self.rechnung1

        post_response = self.client.post(reverse('rechnung_loeschen', kwargs={"pk": rechnung.id}))
        self.assertEquals(post_response.status_code, 302)
        self.assertEquals(Rechnung.objects.count(), 0)
    '''

