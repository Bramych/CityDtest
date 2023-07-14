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
from application import Application

class TestAutorization():
  def setUp(self):
    self.app=Application()
  
  def test_autorization(self, login = "+(980) 387 68 14", telcode = "0000"):
    #авторизация юзера
    self.open_page()
    element = self.driver.find_element(By.CSS_SELECTOR, "a > img")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    self.driver.find_element(By.CSS_SELECTOR, ".nav-bar-profile").click()
    self.driver.find_element(By.CSS_SELECTOR, ".TextField_text-field-input__OMhtf:nth-child(1)").send_keys(login)
    time.sleep(2)
    self.driver.find_element(By.CSS_SELECTOR, ".TextField_text-field-input__OMhtf:nth-child(1)").send_keys(Keys.ENTER)
    time.sleep(2)
    self.driver.find_element(By.CSS_SELECTOR, ".TextField_text-field-input__OMhtf:nth-child(1)").send_keys(telcode)
    self.driver.find_element(By.CSS_SELECTOR, ".TextField_text-field-input__OMhtf:nth-child(1)").send_keys(Keys.ENTER)


