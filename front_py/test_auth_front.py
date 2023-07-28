import unittest
import pytest
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from fixture.application import Application
from model.group import Group


@pytest.fixture(scope="session")
def app(request):
    fixture = Application()
    #request.addfinalazer(fixture.teardown_method)
    return fixture

def test_autorization(app, login="9803876814", telcode="0000"):
     # авторизация юзера
    app.open_page()
    time.sleep(1)
    app.driver.find_element(By.CSS_SELECTOR, ".nav-bar-profile").click()
    app.driver.find_element(By.CSS_SELECTOR, ".TextField_text-field-input__OMhtf:nth-child(1)").send_keys(
    login)
    time.sleep(1)
    #app.driver.find_element(By.CSS_SELECTOR, ".TextField_text-field-input__OMhtf:nth-child(1)").send_keys(
    #Keys.ENTER)
    app.driver.find_element(By.CSS_SELECTOR, ".TextField_text-field-input__OMhtf:nth-child(1)").send_keys(
    telcode)
    app.driver.find_element(By.CSS_SELECTOR, ".TextField_text-field-input__OMhtf:nth-child(1)").send_keys(
    Keys.ENTER)
    time.sleep(1)
    #app.driver.find_element(By.CSS_SELECTOR, ".TextField_text-field-input__OMhtf:nth-child(1)").send_keys(
    #Keys.ENTER)
    #app.driver.find_element(By.CSS_SELECTOR, ".Modal_modal-overlay__FAHhp").click()
