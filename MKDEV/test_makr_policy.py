import pytest
from selenium.webdriver.common.by import By
from fixture.application import Application
import time

@pytest.fixture(scope="session")
def app(request):
    fixture = Application()
    #request.addfinalazer(fixture.teardown_method)
    return fixture


def test_marketing_policy(app):
    app.driver.get("https://zc-qa-test.win/marketing-policy/")
    if app.driver.find_element(By.CSS_SELECTOR, ".MarketingPolicy_title__vHkJu").is_displayed():
        print("Заголовок H1 отображается")
    else:
        print("error")
    if app.driver.find_element(By.CSS_SELECTOR, ".MarketingPolicy_subtitle__afPcB").is_displayed():
        print(("Заголовок H2 отображается"))
    assert app.driver.title == "Маркетинговая политика онлайн-сервиса Здравсити", "Заголовок не соответсвует"

