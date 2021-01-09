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
        cls.client = Client()
        cls.browser = webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options)
        cls.user = User.objects.create_superuser(username="hallo123", password="dasisteintest123!")
        cls.group = Group(name='mitarbeiter')
        cls.group.save()
        cls.user.groups.add(cls.group)
        cls.user.save()
        force_login(cls.user, cls.browser, cls.live_server_url)

    @classmethod
    def tearDownClass(cls):
        cls.browser.quit()
        super().tearDownClass()

    def test_kunde_auftrag_rechnung(self):

        self.browser.get('%s%s' % (self.live_server_url, '/kundenliste'))
        self.browser.find_element_by_class_name("btn-primary").click()
        vorname_input = self.browser.find_element_by_name("vorname")
        vorname_input.send_keys('Max')
        nachname_input = self.browser.find_element_by_name("nachname")
        nachname_input.send_keys('Mustermann')
        email_input = self.browser.find_element_by_name("email")
        email_input.send_keys('max@mustermann.de')
        telefon_input = self.browser.find_element_by_name("telefon")
        telefon_input.send_keys('+4917666994073')
        self.browser.find_element_by_class_name("btn-success").click()
        self.browser.get('%s%s' % (self.live_server_url, '/auftragsliste'))
        self.browser.find_element_by_class_name("btn-primary").click()
        self.browser.find_element_by_xpath("//select[@name='kunde']/option[text()='Max Mustermann']").click()
        preis_input = self.browser.find_element_by_name("preis")
        preis_input.send_keys('600,00')
        self.browser.find_element_by_class_name("btn-success").click()
        self.browser.get('%s%s' % (self.live_server_url, '/rechnungsliste'))
        self.browser.find_element_by_class_name("btn-primary").click()
        self.browser.find_element_by_xpath("//select[@name='kunde']/option[text()='Max Mustermann']").click()

        self.browser.find_element_by_xpath(
            "//select[@name='auftrag']/option[text()='Auftragsnummer: 1, Kunde Max Mustermann']").click()
        self.browser.find_element_by_class_name("btn-success").click()
