import pytest
import yaml
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager


with open("testdata.yaml") as f:
	testdata = yaml.safe_load(f)

@pytest.fixture(scope='session')
def browser():
    browser = testdata["browser"]
    if browser == 'firefox':
        service = Service(executable_path=GeckoDriverManager().install())
        options = webdriver.FirefoxOptions()
        driver = webdriver.Firefox(service=service, options=options)
    elif browser == 'chrome':
        service = Service(executable_path=ChromeDriverManager().install())
        options = webdriver.ChromeOptions()
        driver = webdriver.Chrome(service=service, options=options)
    yield driver
    driver.quit()


# @pytest.fixture()
# def log_xpath():
# 	return """//*[@id="login"]/div[1]/label/input"""
#
# @pytest.fixture()
# def pass_xpath():
# 	return """//*[@id="login"]/div[2]/label/input"""
#
# @pytest.fixture()
# def btn_xpath():
# 	return """//*[@id="login"]/div[3]/button"""
#
# @pytest.fixture()
# def result_xpath():
# 	return """//*[@id="app"]/main/div/div/div[2]/h2"""
#
# @pytest.fixture()
# def result_login():
# 	return """//*[@id="app"]/main/div/div[1]/h1"""
#
# @pytest.fixture()
# def btn_new_post():
# 	return """//*[@id="create-btn"]"""
#
# @pytest.fixture()
# def title():
# 	return """//*[@id="create-item"]/div/div/div[1]/div/label/input"""
#
# @pytest.fixture()
# def btn_save():
# 	return """//*[@id="create-item"]/div/div/div[7]/div/button/span"""
#
# @pytest.fixture()
# def result_post():
# 	return """//*[@id="app"]/main/div/div[1]/h1"""
#
# @pytest.fixture()
# def site():
# 	my_site = Site(testdata["address"])
# 	yield my_site
# 	my_site.close()
