from selenium.webdriver.common.by import By


class Checkout:
    def __init__(self, driver):
        self.driver = driver

    country = (By.ID, 'country')
    selectcountry = (By.LINK_TEXT, 'India')
    finalsubmission = (By.XPATH, '//input[@class="btn btn-success btn-lg"]')

    def findcountry(self):
        return self.driver.find_element(*Checkout.country)

    def selectindia(self):
        return self.driver.find_element(*Checkout.selectcountry)

    def submission(self):
        return self.driver.find_element(*Checkout.finalsubmission)