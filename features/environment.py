from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from webdriver_manager.firefox import GeckoDriverManager
from app.application import Application


def browser_init(context, scenario_name):
    """
    :param context: Behave context
    """

    #Chrome browser
    #driver_path = ChromeDriverManager().install()
    #service = Service(driver_path)
    #context.driver = webdriver.Chrome(service=service)

    #Firefox browser
    #driver_path = GeckoDriverManager().install()
    #service = Service(driver_path)
    #context.driver = webdriver.Firefox(service=service)

    # Headless
    #options = webdriver.ChromeOptions()
    #options.add_argument('headless')
    #service = Service(ChromeDriverManager().install())
    #context.driver = webdriver.Chrome(options=options, service=service)

    ### BROWSERSTACK ###
    # Register for BrowserStack, then grab it from https://www.browserstack.com/accounts/settings
   #bs_user = 'shrutiprem_ndUArm'
   #bs_key = 'Xzst8mjdg4ExRqZLAyS1'
  #url = f'http://{bs_user}:{bs_key}@hub-cloud.browserstack.com/wd/hub'

   #options = Options()
   #bstack_options = {
    #   "os": "OS X",
     #  "osVersion": "Monterey",
      # 'browserName': 'edge',
     #  'sessionName': scenario_name
  # }
   #options.set_capability('bstack:options', bstack_options)
   #context.driver = webdriver.Remote(command_executor=url, options=options)
    chrome_options = Options()
    mobile_emulation = {"deviceName": "Nexus 5"}
    #chrome_options = webdriver.ChromeOptions()
    chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)
    #driver = webdriver.Remote(command_executor='http://127.0.0.1:4444/wd/hub',
    #desired_capabilities=chrome_options.to_capabilities())
    driver_path = ChromeDriverManager().install()
    service = Service(driver_path)
    context.driver = webdriver.Chrome(service=service, options=chrome_options)

    context.driver.maximize_window()
    context.driver.implicitly_wait(4)

    context.app = Application(context.driver)


def before_scenario(context, scenario):
    print('\nStarted scenario: ', scenario.name)
    browser_init(context, scenario.name)


def before_step(context, step):
    print('\nStarted step: ', step)


def after_step(context, step):
    if step.status == 'failed':
        print('\nStep failed: ', step)


def after_scenario(context, feature):
    context.driver.quit()
