import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
#from application import Application

#@pytest.fixture()
#def app(request):
   # fixture = Application()
   # request.addfinalazer(fixture.teardown_method)
   # return fixture

class TestAuthorization():
    def setup_method(self):
        self.driver = webdriver.Firefox()
        #self.driver.implicitly_wait(60)
        #self.app = Application()

    def teardown_method(self):
        self.driver.quit()

    def open_page(self):
        self.driver.get("https://zc-qa-test.win/")
        self.driver.set_window_size(1200, 800)

    def test_autorization(self, login="9803876814", telcode="0000"):
        # авторизация юзера
        self.open_page()
        time.sleep(1)
        self.driver.find_element(By.CSS_SELECTOR, ".nav-bar-profile").click()
        self.driver.find_element(By.CSS_SELECTOR, ".TextField_text-field-input__OMhtf:nth-child(1)").send_keys(
            login)
        self.driver.find_element(By.CSS_SELECTOR, ".TextField_text-field-input__OMhtf:nth-child(1)").send_keys(login)
        time.sleep(2)
        self.driver.find_element(By.CSS_SELECTOR, ".TextField_text-field-input__OMhtf:nth-child(1)").send_keys(
            Keys.ENTER)
        self.driver.find_element(By.CSS_SELECTOR, ".TextField_text-field-input__OMhtf:nth-child(1)").send_keys(telcode)
        time.sleep(2)
        self.driver.find_element(By.CSS_SELECTOR, ".TextField_text-field-input__OMhtf:nth-child(1)").send_keys(
            Keys.ENTER)
        self.driver.find_element(By.CSS_SELECTOR, ".Modal_modal-overlay__FAHhp").click()

