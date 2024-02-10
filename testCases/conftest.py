import time
import pytest
from selenium import webdriver

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--headless")

def pytest_addoption(parser):
    parser.addoption("--browser")


@pytest.fixture
def setup(request):

    browser = request.config.getoption("--browser")

    if browser == 'chrome':
        driver = webdriver.Chrome()

    elif browser == 'firefox':
        driver = webdriver.Firefox()

    elif browser == 'edge':
        driver = webdriver.Edge()

    else:
        # driver = webdriver.Chrome()
        driver = webdriver.Chrome(options=chrome_options)

    driver.get("https://admin-demo.nopcommerce.com/")
    time.sleep(2)

    yield driver
    driver.quit()


@pytest.fixture(params=[
    ('admin@yourstore.com', 'admin', 'pass'),
    ('admin1@yourstore.com', 'admin', 'fail'),
    ('admin@yourstore.com', '1admin', 'fail'),
    ('admin1@yourstore.com', '1admin', 'fail')
])

def DataforLogin(request):
    return request.param


# pytest -v -n=2 --html=htmlreports/myreportNew.html --alluredir="D:\E Drive Data\CREDENCE\9. YUSUF SIR - Automation Testing\0. PRACTICAL\PRACTICALS\NOP_Commerse\allureReport" --browser chrome  -p no:warnings





