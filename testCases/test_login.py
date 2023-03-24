import pytest
from selenium import webdriver
from pageObjects.LoginPage import Login
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen

class Test_001_Login:
    baseUrl = ReadConfig.getApplicationUrl()
    username = ReadConfig.getUserEmail()
    password = ReadConfig.getPassword()

    # baseUrl = "https://admin-demo.nopcommerce.com"
    # username = "admin@yourstore.com"
    # password = "admin"

    logger = LogGen.loggen()

    def test_homePageTitle(self, setup):
        self.logger.info("****************Test__001__Login******************")
        self.logger.info("**************Verifying Home Page Title***********")
        self.driver = setup
        self.driver.get(self.baseUrl)
        act_title = self.driver.title
        if act_title =="Your store. Login":
            assert True
            self.driver.close()
            self.logger.info("**************Home Page Title is Passed***********")
        else:
            self.driver.save_screenshot(".\\Screenshots\\"+"test_homePage.Title.png")
            self.driver.close()
            self.logger.error("**************Home Page Title is Failed***********")
            assert False


    def test_Login(self, setup):
        self.logger.info("****************Verifying Login Test******************")
        self.driver = setup
        self.driver.get(self.baseUrl)
        self.lp = Login(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        act_title = self.driver.title
        if act_title =="Dashboard / nopCommerce administration":
            assert True
            self.driver.close()
            self.logger.info("****************Login Test is Passed******************")
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_Login.png")
            self.driver.close()
            self.logger.error("****************Login Test is Failed******************")
            assert False

