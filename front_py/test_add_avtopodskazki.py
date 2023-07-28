import unittest
import pytest
from selenium.webdriver.common.by import By
from fixture.application import Application



@pytest.fixture(scope="session")
def app(request):
    fixture = Application()
    #request.addfinalazer(fixture.teardown_method)
    return fixture

def test_addcardavtpdzk(app):
    #Добавить из автоподсказок
    app.open_page()
    app.driver.find_element(By.ID, "desktopSearchInput").click()
    app.driver.find_element(By.CSS_SELECTOR, "li:nth-child(2) .Button_button__4em_S").click()