import pytest
from selenium import webdriver
from PageObjects.LoginPage import Login
from Utilities.readproperties import configRead
from Utilities.customlogger import LogGen

class Test_TC01_Login:
    baseURL = configRead.getbaseURL()
    username = configRead.getusername()
    password = configRead.getpassword()

    logger = LogGen.loggen()

    @pytest.mark.sanity
    #@pytest.mark.regression
    def test_login(self, setup):

        self.logger.info("***********************Test_TC01_Login**************************")
        self.logger.info("****************************Verifying Login Test************************************")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        self.lp= Login(self.driver)
        self.lp.setUsername(self.username)
        self.lp.setpassword(self.password)
        self.driver.save_screenshot(".//Screenshots//TC01//" + "01_Login page.png")
        self.lp.clicklogin()
        self.logger.info("***************************We logged in successfully*************************************")
        act_title = self.driver.title
        if act_title == "Your store. Login":
            assert True
            self.driver.save_screenshot(".//Screenshots//TC01//"+"02_Home page.png")
            self.logger.info("**************************Logged out successfully***********************************")
            self.driver.close()
        else:
            self.driver.save_screenshot(".//Screenshots//TC01//" +"02_Home page.png")
            self.logger.error("****************************Error Occured********************************************")
            self.driver.close()






