import logging

import pytest
import requests
import yaml
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from email_report import send_email

with open("testdata.yaml") as f:
	test_data = yaml.safe_load(f)

@pytest.fixture(scope='session')
def browser():
    browser = test_data["browser"]
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
    send_email()


@pytest.fixture
def token():
    try:
        response = requests.post(url=test_data['url_post'], data={"username": test_data['login'], "password":
            test_data['password']})
        if response.status_code == 200:
            return response.json()["token"]
        else:
            logging.error(f"Ошибка входа в систему. Код состояния: {response.status_code}")
            return None
    except:
        logging.exception(f"Исключение при входе в систему")
        return None

@pytest.fixture
def required_id(token):
    try:
        res_get = requests.get(url="https://test-stand.gb.ru/api/posts", headers={"X-Auth-Token": token}, params={"owner": "notMe"})
        if res_get.status_code == 200:
            return res_get.json()["data"][0]['id']
        else:
            logging.error(f"Ошибка запроса ID. Код состояния: {res_get.status_code}")
            return None
    except:
        logging.exception(f"Исключение при выполнении запроса")
        return None

