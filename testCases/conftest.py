import pytest
from selenium import webdriver

@pytest.fixture()
def setup():
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    driver = webdriver.Chrome(options=options)
    return driver