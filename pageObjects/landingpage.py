from selenium.webdriver.common.by import By
from pageObjects.homepage import HomePage


class LandingPage:
    def __init__(self, driver):
        self.driver = driver

    shop = (By.LINK_TEXT, 'Shop')
    name = (By.NAME, 'name')
    email = (By.CSS_SELECTOR, "input[name='email']")
    password = ('id', 'exampleInputPassword1')
    chkbox = ('id', 'exampleCheck1')
    selectitem = (By.ID, 'exampleFormControlSelect1')
    submitbutton = (By.XPATH, "//input[@type='submit']")
    alertmsg = (By.CLASS_NAME, 'alert-success')

    def shoplink(self):
        self.driver.find_element(*LandingPage.shop).click()
        return HomePage(self.driver)

    def formame(self):
        return self.driver.find_element(*LandingPage.name)

    def foremail(self):
        return self.driver.find_element(*LandingPage.email)

    def formpassword(self):
        return self.driver.find_element(*LandingPage.password)

    def formchkbox(self):
        return self.driver.find_element(*LandingPage.chkbox)

    def formselect(self):
        return self.driver.find_element(*LandingPage.selectitem)

    def formsubmit(self):
        return self.driver.find_element(*LandingPage.submitbutton)

    def formalert(self):
        return self.driver.find_element(*LandingPage.alertmsg)