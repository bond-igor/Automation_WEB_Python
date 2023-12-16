import yaml, time
from testpage import OperationsHelper
import logging

with open("testdata.yaml") as f:
	testdata = yaml.safe_load(f)


def test_step_1(browser):
    logging.info("Тест 1 запущен")
    testpage = OperationsHelper(browser, testdata["address"])
    testpage.go_to_site()
    testpage.enter_login('test')
    testpage.enter_pass('test')
    testpage.click_login_button()
    assert testpage.get_error_text() == '401'

def test_step2(browser):
	logging.info("Тест 2 запущен")
	testpage = OperationsHelper(browser, testdata['address'])
	testpage.go_to_site()
	testpage.enter_login(testdata["login"])
	testpage.enter_pass(testdata["password"])
	testpage.click_login_button()

	assert testpage.get_text_blog() == "Blog"


def test_step3(browser):
	# залогинится
	logging.info("Тест 3 запущен")
	testpage = OperationsHelper(browser, testdata['address'])
	testpage.go_to_site()
	try:
		testpage.enter_login(testdata["login"])
		testpage.enter_pass(testdata["password"])
		testpage.click_login_button()
	except:
		pass
	# создания поста
	testpage.click_nwe_post_button()
	testpage.enter_title_post("new title")
	testpage.enter_content_post("content")
	testpage.click_create_nwe_post_button()

	time.sleep(3)

	# Проверка наличия названия поста на странице
	assert testpage.post() == "new title"

def test_step_4(browser):
	logging.info("Тест 4 запущен")
	testpage = OperationsHelper(browser, testdata['address'])
	testpage.go_to_site()
	#добавим модуль try/except что бы тест можно было запускать отдельно от других
	try:
		testpage.enter_login(testdata['login'])
		testpage.enter_pass(testdata['password'])
		testpage.click_login_button()
	except:
		pass
	testpage.click_contact()
	time.sleep(testdata['sleep_time'])
	testpage.contact_us_name("ivan")
	testpage.contact_us_email("test@mail.ru")
	testpage.contact_us_content("Hello World")
	testpage.click_contact_us()
	time.sleep(testdata['sleep_time'])
	assert testpage.alert() == 'Form successfully submitted'