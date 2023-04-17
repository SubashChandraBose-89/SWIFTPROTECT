import pytest
from selenium import webdriver
from PageObjects.Swift_Login import SwiftLogin
from Utilities.readProperties import ReadConfig
from Utilities.Logger import LogGenerator


class Test_Login_TC:
    baseURL = ReadConfig.getURL()
    username = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()
    logger = LogGenerator.logenerator()

    @pytest.mark.sanity
    def test_login(self):
        self.driver = webdriver.Chrome()
        self.logger.info("SWIFT PROTECT -> LOGIN TEST INITIATED")
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        self.swftLogin = SwiftLogin(self.driver)
        self.driver.implicitly_wait(30)
        self.swftLogin.setUsername(self.username)
        self.swftLogin.setPassword(self.password)
        self.swftLogin.login()
        self.logger.info("SWIFT PROTECT -> LOGIN CREDENTIALS ENTERED")
        self.swftLogin.dismissAlert()
        title_name = self.driver.title
        if title_name == "Home":
            assert True
            self.logger.info("SWIFT PROTECT -> LOGIN FUNCTION SUCCESSFUL")
            self.driver.close()
        else:
            self.logger.error("SWIFT PROTECT -> LOGIN FUNCTION FAILED")
            assert False


