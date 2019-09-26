class HomePage():

    def __init__(self, driver):
        self.driver = driver

        self.logout_button_id = "titlebar_hyperlink_8-lbsignout_image"

    def click_logout(self):
        self.driver.find_element_by_id(self.logout_button_id).click()
