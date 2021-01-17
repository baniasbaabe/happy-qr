from django.contrib.staticfiles.testing import StaticLiveServerTestCase, LiveServerTestCase
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
from crm.models import *
from django.test import Client
from django.contrib.auth.models import User, Group
from seleniumlogin import force_login


class TestKundeSeite(LiveServerTestCase):

    @classmethod
    def setUp(cls):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--disable-gpu')
        cls.browser = webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options)
        cls.user = User.objects.create_superuser(username="Kunde", password="dasisteintest123!", email="test@testmail.de")
        cls.kunde = Kunde.objects.create(user=cls.user, vorname="Kunde", nachname="Kunde", email="test@testmail.de")
        cls.auftrag = Auftrag.objects.create(kunde=cls.kunde, status="Abgeschlossen", preis=100.00)
        cls.group = Group(name='kunde')
        cls.group.save()
        cls.user.groups.add(cls.group)
        cls.user.save()
        force_login(cls.user, cls.browser, cls.live_server_url)

    @classmethod
    def tearDownClass(cls):
        cls.browser.quit()
        super().tearDownClass()

    def test_dashboard(self):

        self.browser.get('%s%s' % (self.live_server_url, '/menucard'))
        self.browser.find_element_by_xpath("/html/body/div/div[3]/div/div[1]/div[1]/div/a").click() #Vorspeise anzeigen
        self.browser.find_element_by_xpath("/html/body/div/div[2]/div/div/a[2]").click() # Produkt anlegen
        name_input = self.browser.find_element_by_name("name")
        name_input.send_keys('Salat')
        beschreibung_input = self.browser.find_element_by_name("beschreibung")
        beschreibung_input.send_keys('Testbeschreibung')
        zusatzstoff_input = self.browser.find_element_by_name("zusatzstoffe")
        zusatzstoff_input.send_keys('1')
        preis_input = self.browser.find_element_by_name("preis")
        preis_input.send_keys('10.0')
        self.browser.find_element_by_xpath("/html/body/div/div[2]/div[1]/div/form/button").click() # Speichern
        self.browser.find_element_by_xpath("//html/body/div/div[3]/div/div/table/tbody/tr[1]/td[5]/a").click() # Ändern
        name_input = self.browser.find_element_by_name("name")
        name_input.send_keys('Geändert')
        self.browser.find_element_by_xpath("/html/body/div/div[2]/div[1]/div/form/input[3]").click() # Speichern
        self.browser.find_element_by_xpath("/html/body/div/div[3]/div/div/table/tbody/tr[1]/td[6]/a").click()  # Mülleimer
        self.browser.find_element_by_xpath("/html/body/div/div[2]/div/div/div/form/button").click()  # Löschen
        self.browser.find_element_by_xpath("/html/body/div/div[2]/div/div/a[1]").click() # Zurück zum Dashboard
        self.browser.find_element_by_xpath('//*[@id="id_template"]').click() # Template Dropdown
        self.browser.find_element_by_xpath('//*[@id="id_template"]/option[2]').click() # Template 2
        self.browser.find_element_by_xpath('/html/body/div/div[4]/div/div/div[2]/form/button').click() # Speichern
        self.browser.find_element_by_xpath('/html/body/div/div[2]/div/div/a[1]').click()

