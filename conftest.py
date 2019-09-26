# conftest.py file is created at the project root and is used to define the fixtures that are injected into tests which are common
# Fixtures are a potential and common use of conftest.py
# The fixtures that you will define will be shared among all tests in your test suite
import pytest


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome", help="Type browser name chrome or firefox")


@pytest.fixture(scope="class")
def test_setup(request):
    from selenium import webdriver
    browser = request.config.getoption("--browser")

    if browser == 'chrome':
        driver = webdriver.Chrome(
            executable_path="C:/Users/Vinay/PycharmProjects/MODECRegressionMaximo/drivers/chromedriver.exe")
    elif browser == 'firefox':
        driver = webdriver.Firefox(
            executable_path="C:/Users/Vinay/PycharmProjects/MODECRegressionMaximo/drivers/geckodriver.exe")

    driver.implicitly_wait(5)
    driver.maximize_window()
    request.cls.driver = driver
    # TearDown
    yield
    driver.close()
    driver.quit()
    print("LoginLogout Test completed")
