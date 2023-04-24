import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from PageObjects.Swift_FieldInterview import SwiftFieldInterview
from PageObjects.Swift_Login import SwiftLogin
from PageObjects.Swift_SearchFieldInterview import SwiftSearchFI
from Utilities.readProperties import ReadConfig
from Utilities.Logger import LogGenerator


class Test_SearchFieldInterview:
    baseURL = ReadConfig.getURL()
    username = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()
    logger = LogGenerator.logenerator()

    @pytest.mark.sanity
    def test_TC004_DeleteTest(self):
        self.driver = webdriver.Chrome()
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        self.swftLogin = SwiftLogin(self.driver)
        self.driver.implicitly_wait(30)
        self.swftLogin.setUsername(self.username)
        self.swftLogin.setPassword(self.password)
        self.swftLogin.login()
        self.swftLogin.dismissAlert()
        self.logger.info("SWIFT PROTECT -> SEARCH DATA TEST INITIATED")
        self.title_name = self.driver.title
        print("Title name -> "+self.title_name+" Login Successful")
        self.FI = SwiftFieldInterview(self.driver, WebDriverWait)
        self.driver.implicitly_wait(20)
        self.FI.clickAgencyRecords()
        self.FI.clickFieldInterviews()
        self.FI.getTitle1()
        print("Field Interview Page Opened")
        self.SFI = SwiftSearchFI(self.driver, WebDriverWait)
        for i in range(50):
            self.SFI.selectReport()
            time.sleep(2)
            self.driver.find_element(By.ID, "btnDeleteButton").click()
            time.sleep(2)
            self.driver.find_element(By.XPATH, "//button[contains(text(), 'Yes')]").click()
            time.sleep(2)
