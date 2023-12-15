from BasePage import BasePage
from selenium.webdriver.common.by import By
import logging

class TestSearchLocators:
	LOCATOR_LOGIN_FIELD = (By.XPATH, """//*[@id="login"]/div[1]/label/input""")
	LOCATOR_PASS_FIELD = (By.XPATH, """//*[@id="login"]/div[2]/label/input""")
	LOCATOR_LOGIN_BTN = (By.XPATH, """//*[@id="login"]/div[3]/button""")
	LOCATOR_ERROR_FIELD = (By.XPATH, """//*[@id="app"]/main/div/div/div[2]/h2""")
	LOCATOR_RESULT_LOGIN = (By.XPATH, """//*[@id="app"]/main/div/div[1]/h1""")
	LOCATOR_CREATE_NEW_POST = (By.XPATH, """//*[@id="create-btn"]""")
	LOCATOR_POST_TITLE = (By.XPATH, """//*[@id="create-item"]/div/div/div[1]/div/label/input""")
	LOCATOR_POST_CONTENT = (By.XPATH, """//*[@id="create-item"]/div/div/div[3]/div/label/span/textarea""")
	LOCATOR_CREATE_POST_BTN = (By.XPATH, """//*[@id="create-item"]/div/div/div[7]/div/button""")
	LOCATOR_POST = (By.XPATH, """//*[@id="app"]/main/div/div[1]/h1""")
	LOCATOR_RES_CREATE = (By.XPATH, """//*[@id="app"]/main/div/div[3]/div[1]/a/h2""")
	LOCATOR_HOME = (By.XPATH, """//*[@id="app"]/main/nav/a/span""")
	LOCATOR_CONTACT = (By.XPATH, """//*[@id="app"]/main/nav/ul/li[2]""")
	LOCATOR_YOUR_NAME = (By.XPATH, """//*[@id="contact"]/div[1]/label/input""")
	LOCATOR_YOUR_EMAIL = (By.XPATH, """//*[@id="contact"]/div[2]/label/input""")
	LOCATOR_YOUR_CONTENT = (By.XPATH, """//*[@id="contact"]/div[3]/label/span/textarea""")
	LOCATOR_CONTACT_US_BTN = (By.XPATH, """//*[@id="contact"]/div[4]/button""")


class OperationsHelper(BasePage):

	def enter_login(self, word):
		logging.info(f"Ввод {word} в элемент {TestSearchLocators.LOCATOR_LOGIN_FIELD[1]}")
		login_field = self.find_element(TestSearchLocators.LOCATOR_LOGIN_FIELD)
		login_field.clear()
		login_field.send_keys(word)

	def enter_pass(self, word):
		logging.info(f"Ввод {word} в элемент {TestSearchLocators.LOCATOR_PASS_FIELD[1]}")
		pass_field = self.find_element((TestSearchLocators.LOCATOR_PASS_FIELD))
		pass_field.clear()
		pass_field.send_keys(word)

	def click_login_button(self):
		logging.info("Нажимает кнопку логин")
		self.find_element(TestSearchLocators.LOCATOR_LOGIN_BTN).click()

	def get_error_text(self):
		error_field = self.find_element(TestSearchLocators.LOCATOR_ERROR_FIELD, time=2)
		text = error_field.text
		logging.info(f"Мы нашли текст {text} в ошибке {TestSearchLocators.LOCATOR_ERROR_FIELD[1]}")
		return text

	def get_text_blog(self):
		text_field = self.find_element(TestSearchLocators.LOCATOR_RESULT_LOGIN, time=2)
		text = text_field.text
		logging.info(f"We find text {text} in error field {TestSearchLocators.LOCATOR_RESULT_LOGIN[1]}")
		return text

	def click_nwe_post_button(self):
		logging.info(f"Click new post button")
		self.find_element(TestSearchLocators.LOCATOR_CREATE_NEW_POST).click()

	def enter_title_post(self, word):
		logging.info(f"Send {word} to element {TestSearchLocators.LOCATOR_POST_TITLE[1]}")
		login_field = self.find_element(TestSearchLocators.LOCATOR_POST_TITLE)
		login_field.clear()
		login_field.send_keys(word)

	def enter_content_post(self, word):
		logging.info(f"Send {word} to element {TestSearchLocators.LOCATOR_POST_CONTENT[1]}")
		login_field = self.find_element(TestSearchLocators.LOCATOR_POST_CONTENT)
		login_field.clear()
		login_field.send_keys(word)

	def click_create_nwe_post_button(self):
		logging.info(f"Click new post button")
		self.find_element(TestSearchLocators.LOCATOR_CREATE_POST_BTN).click()

	def post(self):
		post_field = self.find_element(TestSearchLocators.LOCATOR_POST, time=2)
		text = post_field.text
		logging.info(f"We find text {text} in error field {TestSearchLocators.LOCATOR_POST[1]}")
		return text

	def get_res_create_text(self):
		enter_field = self.find_element(TestSearchLocators.LOCATOR_RES_CREATE, time=2)
		text = enter_field.text
		logging.info(f'We find text {text} in error field {TestSearchLocators.LOCATOR_RES_CREATE[1]}')
		return text

	def click_contact(self):
		logging.info('Click contact button')
		self.find_element(TestSearchLocators.LOCATOR_CONTACT).click()

	def contact_us_name(self, word):
		logging.info(f'Send "{word}" to element {TestSearchLocators.LOCATOR_YOUR_NAME[1]}')
		title_field = self.find_element(TestSearchLocators.LOCATOR_YOUR_NAME)
		title_field.clear()
		title_field.send_keys(word)

	def contact_us_email(self, word):
		logging.info(f'Send "{word}" to element {TestSearchLocators.LOCATOR_YOUR_EMAIL[1]}')
		title_field = self.find_element(TestSearchLocators.LOCATOR_YOUR_EMAIL)
		title_field.clear()
		title_field.send_keys(word)

	def contact_us_content(self, word):
		logging.info(f'Send "{word}" to element {TestSearchLocators.LOCATOR_YOUR_CONTENT[1]}')
		title_field = self.find_element(TestSearchLocators.LOCATOR_YOUR_CONTENT)
		title_field.clear()
		title_field.send_keys(word)

	def click_contact_us(self):
		logging.info('Click create contact button')
		self.find_element(TestSearchLocators.LOCATOR_CONTACT_US_BTN).click()

	def alert(self):
		alert = self.driver.switch_to.alert
		return alert.text