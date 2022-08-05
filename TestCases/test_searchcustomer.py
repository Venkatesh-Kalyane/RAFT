import pytest
import time
from PageObjects.LoginPage import Login
from Utilities.readproperties import configRead
from Utilities.customlogger import LogGen
from PageObjects.searchCustomer import searchCustomer

class Test_TC03_serachCustomer:
    baseURL = configRead.getbaseURL()
    username = configRead.getusername()
    password = configRead.getpassword()
    logger = LogGen.loggen()

    @pytest.mark.sanity
    #@pytest.mark.regression
    def test_searchcustomer(self,setup):
        self.logger.info("*************TC03_serachCustomer****************")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.lp= Login(self.driver)
        self.lp.setUsername(self.username)
        self.lp.setpassword(self.password)
        self.lp.clicklogin()
        self.driver.save_screenshot(".//Screenshots//TC03//" + "01_Home page.png")
        self.logger.info("*************Login Successful***************")

        self.customer = searchCustomer(self.driver)
        self.customer.searchCustomermenu()
        self.customer.searchSubCustomermenu()
        self.driver.save_screenshot(".//Screenshots//TC03//" + "02_Search page.png")
        time.sleep(3)
        self.customer.setEmail("mahi@gmail.com")
        self.customer.setfirstname("mahi")
        self.customer.setlastname("nani")
        self.driver.save_screenshot(".//Screenshots//TC03//" + "03_Entered Data.png")
        self.customer.clicksearchbutton()
        self.driver.save_screenshot(".//Screenshots//TC03//" + "04_Result.png")
        time.sleep(3)

        self.driver.close()


