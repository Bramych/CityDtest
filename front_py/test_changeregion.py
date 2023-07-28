import pytest
from selenium.webdriver.common.by import By
from fixture.application import Application


@pytest.fixture(scope="session")
def app(request):
    fixture = Application()
    #request.addfinalazer(fixture.teardown_method)
    return fixture


def test_changeregion(app):
    #Смена региона
    app.open_page()
    app.driver.find_element(By.CSS_SELECTOR, ".sc-14cf5ab-0 > span").click()
    app.driver.find_element(By.CSS_SELECTOR, ".TextField_text-field-input__OMhtf:nth-child(1)").click()
    app.driver.find_element(By.CSS_SELECTOR, ".TextField_text-field-input__OMhtf:nth-child(1)").clear()
    app.driver.find_element(By.CSS_SELECTOR, ".TextField_text-field-input__OMhtf:nth-child(1)").send_keys("Ирку")
    app.driver.find_element(By.CSS_SELECTOR, "li:nth-child(2) > .RegionAutocomplete_region-autocomplete-suggestion___5xPE").click()
    app.driver.find_element(By.CSS_SELECTOR, ".sc-44235671-3 > .Button_button__4em_S").click()