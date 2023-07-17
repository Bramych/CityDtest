
from selenium import webdriver

class Application:

    def __init__(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(60)

    def teardown_method(self):
        self.driver.quit()

    def open_page(self):
        self.driver.get("https://zc-qa-test.win/")
        self.driver.set_window_size(1200, 800)