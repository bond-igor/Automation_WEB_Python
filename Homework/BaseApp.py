import logging
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:

	def __init__(self, driver, url):
		self.driver = driver
		self.base_url = url

	def find_element(self, locator, time=3):
		try:
			element = WebDriverWait(self.driver, time).until(EC.presence_of_element_located(locator),
		                                              message=f"Элемент с локатором {locator} не найден")
		except:
			logging.exception("Ошибка при поиске элемента")
			element = None
		return element

	def get_element_property(self, locator, property):
		element = self.find_element(locator)
		if element:
			return element.value_of_css_property(property)
		else:
			logging.error((f"Свойство {property} не найдено у элемента с локатором {locator}"))
			return None

	def go_to_site(self):
		try:
			start_browsung = self.driver.get(self.base_url)
		except:
			logging.exception(("Ошибка открытия сайта"))
			start_browsung = None
		return start_browsung

	def get_alert_text(self):
		try:
			alert = self.driver.switch_to.alert
			return alert.text
		except:
			logging.exception("исключение с предупреждением")