from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium import webdriver

class TestKundeSeite(StaticLiveServerTestCase):

    @classmethod
    def setUp(cls):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--disable-gpu')
        cls.browser = webdriver.Chrome(r"crm/tests/chromedriver",options=chrome_options)

    @classmethod
    def tearDownClass(cls):
        cls.browser.quit()
        super().tearDownClass()

    def test_kunde_anlegen(self):
        self.browser.get('%s%s' % (self.live_server_url, '/crm/kunde_anlegen'))
        vorname_input = self.browser.find_element_by_name("vorname")
        vorname_input.send_keys('Max')
        nachname_input = self.browser.find_element_by_name("nachname")
        nachname_input.send_keys('Mustermann')
        email_input = self.browser.find_element_by_name("email")
        email_input.send_keys('max@hotmail.de')
        telefon_input = self.browser.find_element_by_name("telefon")
        telefon_input.send_keys('+4917666994073')
        web_input = self.browser.find_element_by_name("web")
        web_input.send_keys('max.de')
        notiz_input = self.browser.find_element_by_name("notiz")
        notiz_input.send_keys('Beispielnotiz')
        self.browser.find_element_by_xpath('//input[@value="Speichern"]').click()
        print("Selenium test durchgeführt")
