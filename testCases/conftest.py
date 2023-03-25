import pytest
from selenium import webdriver
from pytest import mark

@pytest.fixture()
def setup(browser):
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    if browser == 'chrome':
        driver = webdriver.Chrome(options=options)
        print("Launching Chrome Browser")
    elif browser == 'firefox':
        driver = webdriver.Firefox()
        print("Launching Firefox Browser")
    else:
        driver = webdriver.Chrome(options=options)
    return driver

def pytest_addoption(parser):       # This will get the value from CLI
    parser.addoption("--browser")

@pytest.fixture()     # This will return the browser value to setup menthod
def browser(request):
    return request.config.getoption("--browser")

############Pytest HTML Report######################

# This is a hook for Adding environment info to HTML Report
def pytest_configure(config):
    config._metadata['Project Name'] = 'Nop Commerce'
    config._metadata['Modul Name'] = 'Customers'
    config._metadata['Tester'] = 'Kristian'

@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)