import pytest
from selenium.webdriver.common.by import By
from fixture.application import Application
import time

@pytest.fixture(scope="session")
def app(request):
    fixture = Application()
    #request.addfinalazer(fixture.teardown_method)
    return fixture


def test_site_rules(app):
    app.driver.get("https://zc-qa-test.win/site_rules/")
    if app.driver.find_element(By.CSS_SELECTOR, ".SiteRules_title__lCyjz").is_displayed():
        print("Заголовок H1 отображается")
    else:
        print("error")
    if app.driver.find_element(By.CSS_SELECTOR, ".SiteRules_subtitle__XYqIY").is_displayed():
        print(("Заголовок H2 отображается"))
    assert app.driver.title == "Правила пользования сайтом Здравсити.", "Заголовок не соответсвует"
    app.driver.quit()

