from pyvirtualdisplay import Display
import pytest
from selenium.webdriver import Chrome
from sys import platform
from selenium import webdriver

capabilities = {
    "browserName": "chrome",
    "screenResolution": "1280x1024x24",
    "version": "75.0",
    "enableVNC": True,
}
@pytest.yield_fixture(scope='function')
def driver():
    wd = webdriver.Remote(
        command_executor="http://localhost:4444/wd/hub/",
        desired_capabilities=capabilities
    )
    yield wd
    wd.quit()