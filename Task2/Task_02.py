import requests
import yaml

with open(r'C:\Users\bonda\YandexDisk\YandexDisk\Обучение\Automation_WEB_Python\Task2\config.yaml') as f:
	data = yaml.safe_load(f)

def check_id(token):
	res_get = requests.get(url=data["url_get"], headers={"X-Auth-Token": token}, params={"owner": "notMe"}).json()["data"]
	list_id = []
	for i in res_get:
		list_id.append(i['id'])
	return list_id

