import pytest
from selenium import webdriver
from pageObjects.LoginPage import Login
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from utilities import ExcelUtils
import time

class Test_002_DDT_Login:
    baseUrl = ReadConfig.getApplicationUrl()
    path = './/TestData/LoginData.xlsx'
    # username = ReadConfig.getUserEmail()
    # password = ReadConfig.getPassword()


    logger = LogGen.loggen()

    def test_Login_DDT(self, setup):
        self.logger.info("****************Test_002_DDT_Login******************")
        self.logger.info("****************Verifying Login Test******************")
        self.driver = setup
        self.driver.get(self.baseUrl)
        self.lp = Login(self.driver)



        # get data from excel file
        self.rows = ExcelUtils.getRowCount(self.path, 'Sheet1')
        print('Number of rows...', self.rows)
        lst_status = []  # Empty list variable
        for r in range(2, self.rows+1):
            self.username = ExcelUtils.readData(self.path, 'Sheet1', r, 1)
            self.password = ExcelUtils.readData(self.path, 'Sheet1', r, 2)
            self.exp = ExcelUtils.readData(self.path, 'Sheet1', r, 3)

            self.lp.setUserName(self.username)
            self.lp.setPassword(self.password)
            self.lp.clickLogin()
            time.sleep(5)

            act_title = self.driver.title
            exp_title = "Dashboard / nopCommerce administration"

            if act_title == exp_title:
                if self.exp == 'Pass':
                    assert True
                    self.logger.info("****************Login Test is Passed******************")
                    self.lp.clickLogout()
                    lst_status.append("Pass")
                elif self.exp == 'Fail':
                    self.logger.info("****************Login Test is Failed******************")
                    self.lp.clickLogout()
                    lst_status.append("Fail")
            elif act_title != exp_title:
                if self.exp == 'Pass':
                    self.logger.info("****************Login Test is Failed******************")
                    lst_status.append("Fail")
                elif self == 'Fail':
                    self.logger.info("****************Login Test is Passed******************")
                    lst_status.append("Pass")

        if "Fail" not in lst_status:
            self.logger.info("-------------------Login DDT test passed-----------------")
            self.driver.close()
            assert True
        else:
            self.logger.info("-------------------Login DDT test failed-----------------")
            self.driver.close()
            assert False

        self.logger.info("-------------------End of DDT Test-----------------")
        self.logger.info("-------------------Completed TC_Login_002_DDT-----------------")

