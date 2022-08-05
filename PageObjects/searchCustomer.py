from selenium import webdriver

class searchCustomer:

    lnkCustomers_menu_xpath = "/html/body/div[3]/aside/div/div[4]/div/div/nav/ul/li[4]/a"
    lnkCustomers_menuitem_xpath = "/html/body/div[3]/aside/div/div[4]/div/div/nav/ul/li[4]/ul/li[1]/a"
    input_email_xpath = "//input[@id='SearchEmail']"
    input_firstname_xpath = "//input[@id='SearchFirstName']"
    input_lastname_xpath = "//input[@id='SearchLastName']"
    button_search_xpath ="//button[@id='search-customers']"

    def __init__(self,driver):
        self.driver = driver

    def searchCustomermenu(self):
        self.driver.find_element_by_xpath(self.lnkCustomers_menu_xpath).click()

    def searchSubCustomermenu(self):
        self.driver.find_element_by_xpath(self.lnkCustomers_menuitem_xpath).click()

    def setEmail(self,email):
        self.driver.find_element_by_xpath(self.input_email_xpath).send_keys(email)

    def setfirstname(self,firstname):
        self.driver.find_element_by_xpath(self.input_firstname_xpath).send_keys(firstname)

    def setlastname(self,lastname):
        self.driver.find_element_by_xpath(self.input_lastname_xpath).send_keys(lastname)

    def clicksearchbutton(self):
        self.driver.find_element_by_xpath(self.button_search_xpath).click()






