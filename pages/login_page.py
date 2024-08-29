from selenium.webdriver.common.by import By
from pages.base_page import Page
from time import sleep


class LoginPage(Page):
    EMAIL_FIELD = (By.CSS_SELECTOR, ".input.w-input[name='email-2']")
    PASSWORD_FIELD = (By.CSS_SELECTOR, ".input.w-input[placeholder='Password']")
    CONTINUE_BTN = (By.CSS_SELECTOR, ".login-button.w-button")
    def open(self):
        self.open_url('https://soft.reelly.io/sign-in')
        sleep(5)
    def login(self):
        self.input_text('shruti_17_preman@hotmail.com', *self.EMAIL_FIELD)
        self.input_text('careeristReelly@2024', *self.PASSWORD_FIELD)
        self.click(*self.CONTINUE_BTN)
        sleep(6)

