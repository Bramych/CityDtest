#from fixture.session import SessionHelper
from selenium.webdriver.firefox.webdriver import WebDriver

class Application:

    def __init__(self):
        self.driver = WebDriver()
        self.driver.implicitly_wait(1)
        #self.session = SessionHelper(self)

    def teardown_method(self):
        self.driver.quit()

    def open_page(self):
        self.driver.get("https://zc-qa-test.win/")
        self.driver.set_window_size(1200, 800)