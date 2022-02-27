from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from pageObjects.landingpage import LandingPage
from utilities.baseClass import BaseClass

Chrome_options: Options = webdriver.ChromeOptions()
Chrome_options.add_argument("--start-maximized")
Chrome_options.add_argument("--headless")


class TestOne(BaseClass):
    def test_e2e(self):
        log = self.getlogger()
        landingpage = LandingPage(self.driver)
        homepage = landingpage.shoplink()
        products = homepage.allproducts()
        for product in products:
            productName = homepage.prodname(product).text
            if productName == "Blackberry":
                log.info("The value passed by if condition is:"+productName)
                homepage.addbutton(product).click()
                break
        cart = homepage.checkoutBut()
        checkout = cart.proceedButton()
        log.info("Send key value Ind")
        checkout.findcountry().send_keys('ind')
        self.verifylinkpresense("India")
        checkout.selectindia().click()

        self.driver.execute_script('document.getElementById("checkbox2").click();')

        checkout.submission().click()

        #print(driver.find_element(By.XPATH, '//div[@class="alert alert-success alert-dismissible"]').text)

        successString = 'Success! Thank you! Your order will be delivered in next few weeks :-).'

        assert "Success! Thanks you!" in successString

        self.driver.get_screenshot_as_file('screen.png')
