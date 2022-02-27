from selenium.webdriver.common.by import By

from pageObjects.cartpage import Cart


class HomePage:
    def __init__(self, driver):
        self.driver = driver
    products = (By.XPATH, "//div[@class='card h-100']")
    productname = (By.XPATH, "div/h4/a")
    checkoutbutton = (By.XPATH, '//a[@class="nav-link btn btn-primary"]')
    addpdt = (By.XPATH, 'div/button')

    def allproducts(self):
        return self.driver.find_elements(*HomePage.products)

    def addbutton(self, product):
        return product.find_element(*HomePage.addpdt)

    def prodname(self, product):
        return product.find_element(*HomePage.productname)

    def checkoutBut(self):
        self.driver.find_element(*HomePage.checkoutbutton).click()
        cart = Cart(self.driver)
        return cart
