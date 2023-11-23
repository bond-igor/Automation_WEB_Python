from zeep import Client, Settings
import yaml

with open(r'C:\Users\bonda\YandexDisk\YandexDisk\Обучение\Automation_WEB_Python\Task1\config.yaml') as f:
	data = yaml.safe_load(f)

def check_word(word):
	settings = Settings(strict=False)
	client = Client(wsdl=data["url"], settings=settings)
	return client.service.checkText(word)[0]["s"]

res = check_word("table")

print(res)