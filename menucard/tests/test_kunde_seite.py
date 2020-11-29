from django.contrib.staticfiles.testing import StaticLiveServerTestCase, LiveServerTestCase
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
from crm.models import *

class TestKundeSeite(StaticLiveServerTestCase):

    @classmethod
    def setUp(cls):
        chrome_options = webdriver.ChromeOptions()
        #chrome_options.add_argument('--no-sandbox')
        #chrome_options.add_argument('--headless')
        #chrome_options.add_argument('--disable-gpu')
        cls.browser = webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options)

    @classmethod
    def tearDownClass(cls):
        cls.browser.quit()
        super().tearDownClass()

    def test_kunde_anlegen(self):
        self.browser.get('%s%s' % (self.live_server_url, '/crm/register'))
        username_input = self.browser.find_element_by_name("username")
        username_input.send_keys('Max')
        first_name_input = self.browser.find_element_by_name("first_name")
        first_name_input.send_keys('Max')
        last_name_input = self.browser.find_element_by_name("last_name")
        last_name_input.send_keys('Mustermann')
        email_input = self.browser.find_element_by_name("email")
        email_input.send_keys('max@mustermann.de')
        password1_input = self.browser.find_element_by_name("password1")
        password1_input.send_keys('iijwqneUU21!')
        password2_input = self.browser.find_element_by_name("password2")
        password2_input.send_keys('iijwqneUU21!')
        self.browser.find_element_by_class_name("btn-primary").click()

'''
class TestMenuCardSeite(StaticLiveServerTestCase):

    @classmethod
    def setUp(cls):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--disable-gpu')
        cls.browser = webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options)
        cls.browser.implicitly_wait(10)

    @classmethod
    def tearDownClass(cls):
        cls.browser.quit()
        super().tearDownClass()

    def menucard_sehen(self):
        self.browser.get('%s%s' % (self.live_server_url, '/crm/login'))
        username_input = self.browser.find_element_by_name("username")
        username_input.send_keys('Max')
        first_name_input = self.browser.find_element_by_name("first_name")
        first_name_input.send_keys('Max')
        last_name_input = self.browser.find_element_by_name("last_name")
        last_name_input.send_keys('Mustermann')
        email_input = self.browser.find_element_by_name("email")
        email_input.send_keys('max@mustermann.de')
        password1_input = self.browser.find_element_by_name("password1")
        password1_input.send_keys('Hallo12345!')
        password2_input = self.browser.find_element_by_name("password2")
        password2_input.send_keys('Hallo12345!')
        self.browser.find_element_by_xpath('//input[@value="Registrieren"]').click()
'''