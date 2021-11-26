import pytest
# import chromedriver_autoinstaller
from selenium import webdriver
import webdriver_manager
from webdriver_manager.chrome import ChromeDriverManager
# from webdriver_manager.firefox import FirefoxManager

@pytest.fixture()
def setup(browser):
    # chromedriver_autoinstaller.install()  # Check if the current version of chromedriver exists
    # and if it doesn't exist, download it automatically,
    # then add chromedriver to path


    # driver.get("http://www.python.org")
    driver = None
    if browser=='chrome':
        driver=webdriver.Chrome(ChromeDriverManager().install())
        print("Launching chrome browser.........")
    elif browser=='firefox':
        driver = webdriver.Firefox()
        print("Launching firefox browser.........")
    else:
        driver=webdriver.Chrome(ChromeDriverManager().install())
        print("Launching chrome browser.........")
    yield driver
    driver.quit()

def pytest_addoption(parser):    # This will get the value from CLI /hooks
    parser.addoption("--browser")

@pytest.fixture()
def browser(request):  # This will return the Browser value to setup method
    return request.config.getoption("--browser")

########### pytest HTML Report ################

# It is hook for Adding Environment info to HTML Report
# def pytest_configure(config):
#     config._metadata['Project Name'] = 'Selenium Python'
#     config._metadata['Module Name'] = 'Testing'
#     config._metadata['Tester'] = 'Arihant'

# It is hook for delete/Modify Environment info to HTML Report
@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)