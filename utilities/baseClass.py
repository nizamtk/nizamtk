import inspect

import pytest
import logging
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select

from pageObjects import landingpage


@pytest.mark.usefixtures("setup")
class BaseClass:
    def verifylinkpresense(self, text):
        wait = WebDriverWait(self.driver, 7)
        wait.until(EC.presence_of_element_located((By.LINK_TEXT, text)))

    def dropdownselection(self, text, form):
        SelectObj = Select(form)
        SelectObj.select_by_index(1)
        SelectObj.select_by_visible_text(text)


    def getlogger(self):

        loggerName = inspect.stack()[1][3]
        logger = logging.getLogger(loggerName)
        fileHandler = logging.FileHandler("utilities/logfile.log")
        formatter = logging.Formatter("%(asctime)s :%(levelname)s : %(name)s :%(message)s")
        fileHandler.setFormatter(formatter)

        logger.addHandler(fileHandler)

        logger.setLevel(logging.DEBUG)
        return logger