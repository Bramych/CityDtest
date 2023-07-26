import unittest
import pytest
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from fixture.application import Application
from model.group import Group


@pytest.fixture
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

def test_addcardavtpdzk(app):
    app.open_page()
    app.driver.find_element(By.ID, "desktopSearchInput").click()
    app.driver.find_element(By.CSS_SELECTOR, "li:nth-child(2) .Button_button__4em_S").click()

def test_changeregion(app):
    app.open_page()
    app.driver.find_element(By.CSS_SELECTOR, ".sc-14cf5ab-0 > span").click()
    app.driver.find_element(By.CSS_SELECTOR, ".TextField_text-field-input__OMhtf:nth-child(1)").click()
    app.driver.find_element(By.CSS_SELECTOR, ".TextField_text-field-input__OMhtf:nth-child(1)").clear()
    app.driver.find_element(By.CSS_SELECTOR, ".TextField_text-field-input__OMhtf:nth-child(1)").send_keys("Ирку")
    app.driver.find_element(By.CSS_SELECTOR, "li:nth-child(2) > .RegionAutocomplete_region-autocomplete-suggestion___5xPE").click()
    app.driver.find_element(By.CSS_SELECTOR, ".sc-44235671-3 > .Button_button__4em_S").click()