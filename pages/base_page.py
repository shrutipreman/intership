from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
class Page:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout=15)

    def open_url(self, url):
        self.driver.get(url)

    def find_element(self, *locator):
        return self.driver.find_element(*locator)

    def find_elements(self, *locator):
        return self.driver.find_elements(*locator)

    def click(self, *locator):
        self.driver.find_element(*locator).click()

    def input_text(self, text, *locator):
        self.driver.find_element(*locator).send_keys(text)

    def wait_and_click(self, *locator):
        self.wait.until(EC.element_to_be_clickable(locator),
            message='Element by locator {locator} not clickable').click()