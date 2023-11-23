import pytest
import yaml
import requests

with open(r'C:\Users\bonda\YandexDisk\YandexDisk\Обучение\Automation_WEB_Python\Task2\config.yaml') as f:
	data = yaml.safe_load(f)

@pytest.fixture
def token():
	return requests.post(url=data['url_post'], data={"username": data['login'], "password": data['password']}).json()["token"]

@pytest.fixture
def required_id(token):
	res_get = requests.get(url="https://test-stand.gb.ru/api/posts", headers={"X-Auth-Token": token}, params={"owner": "notMe"})
	return res_get.json()["data"][0]['id']

