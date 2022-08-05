import pytest
from selenium import webdriver
from selenium.webdriver.firefox.options import Options

@pytest.fixture()
def setup(browser):
    if browser=='firefox':
        driver = webdriver.Firefox(executable_path="C:\\Gekodriver\\geckodriverwin64\\geckodriver.exe")
        print("Launching firefox browser.........")
    elif browser=='edge':
        driver = webdriver.Edge(executable_path= "C:\\Edge\\edgedriver_win32\\msedgedriver.exe")
        print("Launching edge browser.........")
    elif browser=='ie':
        driver = webdriver.Ie(executable_path="C:\\IE\\IEDriverServer\\IEDriverServer.exe")
        print("Launching ie browser.........")
    else:
        driver = webdriver.Chrome(executable_path="C:\\Chrome\\chromedriver_win32\\chromedriver.exe")
    return driver

def pytest_addoption(parser):    # This will get the value from CLI /hooks
    parser.addoption("--browser")

@pytest.fixture()
def browser(request):  # This will return the Browser value to setup method
    return request.config.getoption("--browser")

########### pytest HTML Report ################

# It is hook for Adding Environment info to HTML Report
def pytest_configure(config):
    config._metadata['Project Name'] = 'nop Commerce'
    config._metadata['Module Name'] = 'Login Page'
    config._metadata['Tester'] = 'Venkatesh Kalyane'

# It is hook for delete/Modify Environment info to HTML Report
@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)




