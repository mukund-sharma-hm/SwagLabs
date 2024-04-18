import sys
import pytest
from selenium import webdriver
from utilities import ReadConfiguration


@pytest.fixture()
def setup_and_teardown(request):
    driver = None
    browser = ReadConfiguration.read_configuration("basic info", "browser")
    if browser.__eq__("chrome"):
        driver = webdriver.Chrome()
    elif browser.__eq__("edge"):
        driver = webdriver.Edge()
    elif browser.__eq__("firefox"):
        driver = webdriver.Firefox()
    else:
        print("Provide a valid browser name from this list chrome/firefox/edge")

    driver.maximize_window()

    app_url = ReadConfiguration.read_configuration("basic info", "url")
    driver.get(app_url)
    request.cls.driver = driver
    yield
    driver.quit()
