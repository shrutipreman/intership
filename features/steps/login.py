from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@given('Open the main page')
def open_reelly(context):
    context.app.login_page.open()

@when('Log in to the page')
def input_login(context):
    context.app.login_page.login()

