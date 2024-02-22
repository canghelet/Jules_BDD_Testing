from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from time import sleep


class Forgot_password_page(BasePage):
    EMAIL_INPUT = (By.XPATH, '//input[@placeholder="Enter your email"]')
    SEND_EMAIL_BTN = (By.XPATH, '//span[text() = "Send email"]/parent::button')
    EMAIL_ERROR = (By.XPATH, '//p[contains(text(), "email")]')

    def set_email(self, email):
        self.wait_for_elem(*self.EMAIL_INPUT)
        self.driver.find_element(*self.EMAIL_INPUT).send_keys(email)
        sleep(1)

    def click_send_email_btn(self):
        self.driver.find_element(*self.SEND_EMAIL_BTN).click()

    def verify_email_error_msg(self):
       actual =  self.driver.find_element(*self.EMAIL_ERROR).text
       expected = 'Please enter a valid email address!'
       self.assertEqual(actual, expected, 'The error message is incorrect!' )