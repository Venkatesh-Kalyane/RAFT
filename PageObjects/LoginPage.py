from selenium import webdriver

class Login:
    textbox_username_xpath = "//*[@id='Email']"
    textbox_password_xpath = "//*[@id='Password']"
    button_login_xpath = "//*[@class='button-1 login-button']"
    link_logout_linktext = "Logout"

    def __init__(self, driver):
        self.driver = driver

    def setUsername(self, username):
        self.driver.find_element_by_xpath(self.textbox_username_xpath).clear()
        self.driver.find_element_by_xpath(self.textbox_username_xpath).send_keys(username)

    def setpassword(self, password):
        self.driver.find_element_by_xpath(self.textbox_password_xpath).clear()
        self.driver.find_element_by_xpath(self.textbox_password_xpath).send_keys(password)

    def clicklogin(self):
        self.driver.find_element_by_xpath(self.button_login_xpath).click()

    def clicklogout(self):
        self.driver.find_element_by_link_text(self.link_logout_linktext).click()





