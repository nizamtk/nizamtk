from selenium.webdriver.common.by import By

from pageObjects.checkout import Checkout


class Cart:
    def __init__(self, driver):
        self.driver = driver

    proceed = (By.XPATH, '//button[@class="btn btn-success"]')

    def proceedButton(self):
        self.driver.find_element(*Cart.proceed).click()
        checkout = Checkout(self.driver)
        return checkout