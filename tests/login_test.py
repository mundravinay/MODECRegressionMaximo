import allure
import pytest
from Pages.loginPage import LoginPage
from Pages.homePage import HomePage
from utils import utils as utils
import moment


@pytest.mark.usefixtures("test_setup")
class TestLogin():

    def test_login(self):
        driver = self.driver
        driver.get(utils.URL)
        login = LoginPage(driver)
        login.enter_username(utils.USERNAME)
        login.enter_password(utils.PASSWORD)
        login.click_login()

    def test_logout(self):
        global driver
        try:
            driver = self.driver
            homepage = HomePage(driver)
            homepage.click_logout()
            x = driver.title
            print(x)
            assert x == "Start Center"
            # Start Center

        except AssertionError as error:
            print("Assertion error occured")
            print(error)
            currTime = moment.now().strftime("%d-%m-%Y_%H-%M-%S")
            testName = utils.whoami()
            screenshotsName = testName + "_" + currTime
            allure.attach(self.driver.get_screenshot_as_png(), name=screenshotsName,
                          attachment_type=allure.attachment_type.PNG)
            driver.get_screenshot_as_file(
                "C:/Users/Vinay/PycharmProjects/MODECRegressionMaximo/screenshots/" + screenshotsName + ".png")
            raise
        except:
            print("There was an exception")
            currTime = moment.now().strftime("%d-%m-%Y_%H-%M-%S")
            testName = utils.whoami()
            screenshotsName = testName + "_" + currTime
            allure.attach(self.driver.get_screenshot_as_png(), name=screenshotsName,
                          attachment_type=allure.attachment_type.PNG)
            raise
        else:
            print("No Exceptions occurred")
        finally:
            print("Login successful")
