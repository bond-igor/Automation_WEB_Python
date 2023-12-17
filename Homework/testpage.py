from BaseApp import BasePage
from selenium.webdriver.common.by import By
import logging
import yaml
import requests

with open('testdata.yaml') as f:
    test_data = yaml.safe_load(f)

class TestSearchLocators:
	dictloc = dict()
	with open("locators.yaml") as f:
		locators = yaml.safe_load(f)
	for locator in locators["xpath"].keys():
		dictloc[locator] = (By.XPATH, locators["xpath"][locator])
	for locator in locators["css"].keys():
		dictloc[locator] = (By.CSS_SELECTOR, locators["css"][locator])


class OperationsHelper(BasePage):

	def enter_text_into_field(self, locator, word, description=None):
		if description:
			element_name = description
		else:
			element_name = locator
		logging.info(f"Отправлено '{word}' элементу {element_name}")
		field = self.find_element(locator)
		if not field:
			logging.error(f"Элемент {locator} не найден")
			return False
		try:
			field.clear()
			field.send_keys(word)
		except:
			logging.exception(f"исключение при работе с {locator}")
			return False
		return True

	def get_text_from_element(self, locator, description=None):
		if description:
			element_name = description
		else:
			element_name = locator
		field = self.find_element(locator, time=10)
		if not field:
			return None
		try:
			text = field.text
		except:
			logging.exception(f'Исключение при получении теста из {element_name}')
			return None
		logging.info(f'Мы находим текст {text} в поле {element_name}')
		return text

	def click_button(self, locator, description=None):
		if description:
			element_name = description
		else:
			element_name = locator
		button = self.find_element(locator)
		if not button:
			return False
		try:
			button.click()
		except:
			logging.exception(f'Исключение при клике')
			return False
		logging.info(f'Нажимаем {element_name} кнопку')
		return True

#ВВОД ТЕКСТА
	def enter_login(self, word):
		self.enter_text_into_field(TestSearchLocators.dictloc["LOCATOR_LOGIN_FIELD"], word, description="Login form")

	def enter_pass(self, word):
		self.enter_text_into_field(TestSearchLocators.dictloc["LOCATOR_PASS_FIELD"], word, description="Password form")

	def enter_title(self, word):
		self.enter_text_into_field(TestSearchLocators.dictloc["LOCATOR_TITLE_FIELD"], word, description="title form")

	def enter_description(self, word):
		self.enter_text_into_field(TestSearchLocators.dictloc["LOCATOR_DESCRIPTION_FIELD"], word,
		                           description="description form")

	def enter_content_post(self, word):
		self.enter_text_into_field(TestSearchLocators.dictloc["LOCATOR_POST_CONTENT"], word,
		                           description="post content form")

	def enter_contact_name(self, word):
		self.enter_text_into_field(TestSearchLocators.dictloc["LOCATOR_YOUR_NAME"], word,
		                           description="name form")

	def enter_contact_mail(self, word):
		self.enter_text_into_field(TestSearchLocators.dictloc["LOCATOR_YOUR_EMAIL"], word,
		                           description="email form")

	def enter_contact_content(self, word):
		self.enter_text_into_field(TestSearchLocators.dictloc["LOCATOR_YOUR_CONTENT"], word,
		                           description="contact content form")

	def enter_title_post(self, word):
		self.enter_text_into_field((TestSearchLocators.dictloc["LOCATOR_CREATE_TITLE"]), word, description=f"Send {word} to element")



	#ПОЛУЧЕНИЕ ТЕКСТА
	def get_res_text(self):
		return self.get_text_from_element(TestSearchLocators.dictloc["LOCATOR_RES_CREATE"], description="result")

	def get_error_text(self):
		return self.get_text_from_element(TestSearchLocators.dictloc["LOCATOR_ERROR_FIELD"], description="error label")

	def get_user_text(self):
		return self.get_text_from_element(TestSearchLocators.dictloc["LOCATOR_HELLO"],
		                                  description="user profile name")

	def get_text_blog(self):
		return self.get_text_from_element(TestSearchLocators.dictloc["LOCATOR_LOGIN_ENTER"],
		                                  description="We find text {text} in error field")

	def get_res_create_text(self):
		return self.get_text_from_element(TestSearchLocators.dictloc['LOCATOR_POST'], description='error create')

	def get_alert(self):
		logging.info("Get alert text")
		text = self.get_alert_text()
		logging.info(text)
		return text

#КЛИК
	def click_login_button(self):
		self.click_button(TestSearchLocators.dictloc["LOCATOR_LOGIN_BTN"], description="login")

	def click_new_post_btn(self):
		self.click_button(TestSearchLocators.dictloc["LOCATOR_CREATE_NEW_POST"], description="new post")

	def click_save_btn(self):
		self.click_button(TestSearchLocators.dictloc["LOCATOR_CREATE_POST_BTN"], description="save post")

	def click_contact_send_btn(self):
		self.click_button(TestSearchLocators.dictloc["LOCATOR_CONTACT_SEND"], description="contact")

	def contact_contact_link(self):
		self.click_button(TestSearchLocators.dictloc["LOCATOR_CONTACT"], description="contact save")

	def click_contact(self):
		self.click_button(TestSearchLocators.dictloc["LOCATOR_CONTACT_US_BTN"], description="Click contact button")


def check_id(token):
	try:
		res_get = requests.get(url=test_data["url_get"], headers={"X-Auth-Token": token}, params={"owner": "notMe"})
		if res_get.status_code == 200:
			list_id = []
			for i in res_get.json()["data"]:
				list_id.append(i['id'])
			return list_id
		else:
			logging.error(f"Ошибка при извлечении данных. Код состояния: {res_get.status_code}")
	except:
		logging.exception(f"Исключение при выполнении запроса")
