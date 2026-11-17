import pytest
from appium import webdriver
from appium.options.android import UiAutomator2Options

@pytest.fixture
def driver():
    options = UiAutomator2Options().load_capabilities({
        "platformName": "Android",
        "appium:automationName": "UiAutomator2",
        "appium:deviceName": "Android de ejemplo",
        "appium:app": "/ruta/de/ShopGo.apk",
    })

    app_driver = webdriver.Remote("http://127.0.0.1:4723", options=options)
    yield app_driver
    app_driver.quit()