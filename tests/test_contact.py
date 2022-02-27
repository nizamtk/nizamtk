import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from pageObjects.landingpage import LandingPage
from testData.homepagetestdata import HomepageTestData
from utilities.baseClass import BaseClass


class Testform(BaseClass):
    def test_contact(self, getData):
        log = self.getlogger()
        landingpage = LandingPage(self.driver)
        landingpage.formame().send_keys(getData["First Name"])
        log.info("Fetched data for name field is:" + getData["First Name"])
        landingpage.foremail().send_keys(getData["Email"])
        landingpage.formpassword().send_keys(getData["Password"])
        landingpage.formchkbox().click()
        self.dropdownselection(getData["Gender"], landingpage.formselect())
        landingpage.formsubmit().click()
        message = landingpage.formalert().text

        assert 'Success!' in message
        self.driver.refresh()

    #@pytest.fixture(params=[("Nizam", "nizam.tk@outlook.com", "QuickTeam", "Male"),("Amjada", "Nusrin@outlook.com", "T", "Female")])
    @pytest.fixture(params=HomepageTestData.homeData)
    def getData(self, request):
        return request.param
