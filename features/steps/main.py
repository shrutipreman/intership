from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@when('Click on “off plan” at the left side menu')
def click_off_plan(context):
    context.app.main_page.off_plan()

@when('Verify the right page opens')
def verify_right_page(context):
    context.app.main_page.right_page()

@when('Filter by sale status of “Announced”')
def filter_announced(context):
    context.app.main_page.announced()

@then('Verify each product contains the Announced tag')
def verify_announced_tag(context):
    context.app.main_page.verify_tag()
