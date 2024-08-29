from selenium.webdriver.common.by import By
from pages.base_page import Page
from time import sleep

class MainPage(Page):

    OFFPLAN_PAGE = (By.CSS_SELECTOR, ".menu-text-link-leaderboard.w--current")
    SALE_STATUS_BTN = (By.CSS_SELECTOR,".select-field-3.w-select[wized='saleStatusFilter']")
    SIDE_OFFPLAN_BTN = (By.XPATH, "//a[@class='_1-link-menu w-inline-block w--current']//div[@class='menu-button-text'] [text()='Off-plan']")
    ANNOUNCED_BTN = (By.CSS_SELECTOR,"option[value='Announced']")
    PRODUCTS =(By.CSS_SELECTOR,".project-image")
    STATUS_ANNOUNCED =(By.XPATH,"//div[text()='Announced']")

    def off_plan(self):
        self.click(*self.SIDE_OFFPLAN_BTN)
        sleep(5)
    def right_page(self):
        expected_result = 'Off-plan'
        actual_result = self.driver.find_element(*self.OFFPLAN_PAGE).text
        assert expected_result in actual_result, f'Expected text did not match'
        print('Test case passed')

    def announced(self):
        self.click(*self.SALE_STATUS_BTN)
        sleep(5)
        self.click(*self.ANNOUNCED_BTN)
        sleep(5)

    def verify_tag(self):
        for PRODUCT in self.PRODUCTS:
            sleep(5)
            expected_result = 'Announced'
            actual_result = self.driver.find_element(*self.STATUS_ANNOUNCED).text
            assert expected_result in actual_result, f'Expected text did not match'
            print('Test case passed')
            sleep(5)
